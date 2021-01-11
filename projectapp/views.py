from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
# Create your views here.
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk':self.object.pk})



class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    paginate_by = 10
    block_size = 5
    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(project=self.get_object())
        context = super(ProjectDetailView, self).get_context_data(object_list=object_list, **kwargs)
        start_index =  int((context['page_obj'].number - 1) / self.block_size) * self.block_size
        end_index = min(start_index + self.block_size, len(context['paginator'].page_range))
        context['page_range'] = context['paginator'].page_range[start_index:end_index]
        project = self.object
        user = self.request.user
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None

        context['subscription'] = subscription
        return context


class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
        