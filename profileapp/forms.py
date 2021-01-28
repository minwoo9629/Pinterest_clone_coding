from django.forms import ModelForm
from profileapp.models import Profile
from django import forms


class ProfileCreationForm(ModelForm):
    image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']
        labels = {
            'nickname' : '',
            'message' : '',
            'image' : '',
        }

    def __init__(self, *args, **kwargs):
        super(ProfileCreationForm,self).__init__(*args,**kwargs)
        self.fields['nickname'].widget.attrs.update({'class':'input_nickname form-control', 'placeholder':'닉네임'})
        self.fields['message'].widget.attrs.update({'class':'input_message form-control', 'placeholder':'자신을 소개해주세요.'})
        self.fields['image'].widget.attrs.update({'class':'form-control', 'id':'input_myimg','onchange':'upload_img(this)'})