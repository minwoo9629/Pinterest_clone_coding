from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.http import JsonResponse

class AccountPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(AccountPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = '기존 비밀번호'
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control old_password',
            'autofocus': False,
        })
        self.fields['new_password1'].label = '새로운 비밀번호'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control new_password1',
        })
        self.fields['new_password2'].label = '새로운 비밀번호 확인'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control new_password2',
        })
    
    def clean_old_password(self):
        """
        Validates that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            self.error_messages['password_incorrect'] = '잘못된 비밀번호 입니다.'
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                self.error_messages['password_mismatch'] = '비밀번호가 일치하지 않습니다.'
                raise forms.ValidationError(self.error_messages['password_mismatch'],code='password_mismatch',)
        return password2

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

    