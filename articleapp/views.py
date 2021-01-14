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
from django.http import JsonResponse
import json
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
        like = Like.objects.filter(user=self.request.user, article=self.get_object())
        if like.exists():
            context['user_like_flag'] = True
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

    def get_success_url(self):
        return reverse_lazy('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(article_ownership_check, 'get')
@method_decorator(article_ownership_check, 'post')
class ArticleDeleteView(DeleteView, FormMixin):
    model = Article
    template_name = 'articleapp/delete.html'
    success_url = reverse_lazy('articleapp:list')


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 5
    block_size = 5

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        start_index =  int((context['page_obj'].number - 1) / self.block_size) * self.block_size
        end_index = min(start_index + self.block_size, len(context['paginator'].page_range))
        context['page_range'] = context['paginator'].page_range[start_index:end_index]

        return context

@login_required
@require_POST
def Article_like(request):
    pk = request.POST.get('pk', None)
    article = get_object_or_404(Article, pk=pk)
    like, like_existence = Like.objects.get_or_create(user=request.user, article=article)

    if not like_existence:
        like.delete()
        message = "False"
    else:
        message = "True"
    context = {'like_count':article.like_count,'message':message, 'nickname': request.user.profile.nickname}

    return JsonResponse(context)
        