from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView,UpdateView, DeleteView, ListView
from django.views.generic.base import View
from django.views.generic.edit import FormMixin
from articleapp.models import Article, Like
from articleapp.forms import ArticleCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from articleapp.decorators import article_ownership_check
from commentapp.forms import CommentCreationForm
from django.http import JsonResponse, HttpResponse, Http404
import json, os, mimetypes, urllib
from django.conf import settings
# Create your views here.

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'
    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        if self.request.FILES:
            if 'image' in self.request.FILES.keys():
                temp_article.filename = self.request.FILES['image'].name
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('articleapp:detail', kwargs={'pk':self.object.pk})

class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            like = Like.objects.filter(user=self.request.user, article=self.get_object())
            if like.exists():
                context['user_like_flag'] = True
            else:
                context['user_like_flag'] = False
        else:
            context['user_like_flag'] = False
        return context


@method_decorator(article_ownership_check, 'get')
@method_decorator(article_ownership_check, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'
    context_object_name = 'target_article'

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs['pk'])
        os.remove(os.path.join(settings.MEDIA_ROOT, article.image.path))

        temp_article = form.save(commit=False)
        if self.request.FILES:
            if 'image' in self.request.FILES.keys():
                temp_article.filename = self.request.FILES['image'].name
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(article_ownership_check, 'get')
@method_decorator(article_ownership_check, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/delete.html'
    success_url = reverse_lazy('articleapp:list')


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 20
    block_size = 5

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        start_index =  int((context['page_obj'].number - 1) / self.block_size) * self.block_size
        end_index = min(start_index + self.block_size, len(context['paginator'].page_range))
        context['page_range'] = context['paginator'].page_range[start_index:end_index]

        return context

@login_required
@require_POST
def Article_like(request, pk):
    article = get_object_or_404(Article, pk=pk)
    like, like_existence = Like.objects.get_or_create(user=request.user, article=article)

    if not like_existence:
        like.delete()
        message = "False"
    else:
        message = "True"
    context = {'like_count':article.like_count,'message':message ,'pk':pk}

    return JsonResponse(context)

def Article_image_download(request, pk):
    article = get_object_or_404(Article, pk=pk)
    url = article.image.url[1:]
    file_url = urllib.parse.unquote(url)
    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            quote_file_url = urllib.parse.quote(article.filename.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404
        