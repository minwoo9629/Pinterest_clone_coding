from django.forms import ModelForm
from projectapp.models import Project
from django import forms

class ProjectCreationForm(ModelForm):
    image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Project
        fields = ['image', 'title', 'description']
        labels = {
            'image' : '',
            'title' : '',
            'description' : '',
        }
    
    def __init__(self, *args, **kwargs):
        super(ProjectCreationForm,self).__init__(*args,**kwargs)
        self.fields['image'].widget.attrs.update({'class':'form-control', 'id':'input_project_img','onchange':'upload_img(this)'})
        self.fields['title'].widget.attrs.update({'class':'input_title form-control', 'placeholder':'제목'})
        self.fields['description'].widget.attrs.update({'class':'input_description form-control', 'placeholder':'프로젝트를 소개해 주세요', 'rows':1})