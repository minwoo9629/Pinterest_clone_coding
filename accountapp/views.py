from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from django.http import JsonResponse, HttpResponse
from accountapp.forms import AccountUpdateForm
from accountapp.decorators import account_ownership_check
from articleapp.models import Article
# 리스트 안에 decorator로 만들어 사용할 수 있다.
check_ownership = [login_required,account_ownership_check]

class JsonableResponseMixin:
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            data = {'message':'ID 또는 PW가 틀립니다.'}
            return JsonResponse(data=data, status=400)
        else:
            return response
    
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            return response
        else:
            return response

class AccountLoginView(JsonableResponseMixin, LoginView):
    template_name = 'accountapp/login.html'

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    template_name = 'accountapp/detail.html'
    context_object_name = "target_user"

    paginate_by = 10
    block_size = 5
    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        context = super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)
        start_index = int((context['page_obj'].number -1 ) / self.block_size) * self.block_size
        end_index = min(start_index + self.block_size, len(context['paginator'].page_range))
        context['page_range'] = context['paginator'].page_range[start_index:end_index]

        return context

# 일반 function에서 사용하는 decorator를 class 내 method에 사용할 수 있도록 변환해주는 decorator
@method_decorator(check_ownership, 'get')
@method_decorator(check_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello')
    template_name = 'accountapp/update.html'

@method_decorator(check_ownership, 'get')
@method_decorator(check_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'