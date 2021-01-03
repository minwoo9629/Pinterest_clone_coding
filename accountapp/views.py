from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from accountapp.forms import AccountUpdateForm
from accountapp.decorators import account_ownership_check

# 리스트 안에 decorator로 만들어 사용할 수 있다.
check_ownership = [login_required,account_ownership_check]

@login_required
def hello(request):
    if request.method == 'POST':
        return redirect('accountapp:hello')
    else:
        return render(request, 'accountapp/hello.html')

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    template_name = 'accountapp/detail.html'
    context_object_name = "target_user"

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