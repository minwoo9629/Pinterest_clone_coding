from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.http import JsonResponse

class AccountPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(AccountPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control old_password material-icons',
            'autofocus': False,
            'placeholder':'lock 기존 비밀번호 입력',
        })
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control new_password1 material-icons',
            'placeholder':'lock 새로운 비밀번호 입력',
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control new_password2 material-icons',
            'placeholder':'lock 비밀번호 확인',
        })

class AccountCreateForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].error_messages = {'required':'아이디를 입력해주세요.'}
        self.fields['password1'].error_messages = {'required':'비밀번호를 입력해주세요.'}
        self.fields['password2'].error_messages = {'required':'비밀번호를 입력해주세요.'}

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password != password2:
            self.add_error('password1', '비밀번호가 다릅니다.')
            self.add_error('password2', '비밀번호가 다릅니다.')

        try:
            User.objects.get(username=username)
            self.add_error('username','이미 가입된 아이디입니다.')
        except:
            pass

    