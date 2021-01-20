from django.forms import ModelForm
from django import forms
from articleapp.models import Article
from projectapp.models import Project
class ArticleCreationForm(ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    class Meta:
        model = Article
        fields = ['title', 'project', 'content', 'image']

    def __init__(self, *args, **kwargs):
        super(ArticleCreationForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "제목 추가"
        self.fields['title'].widget.attrs['class'] = "input_title"

        self.fields['content'].widget.attrs['placeholder'] = "사진에 대해 설명해 보세요."
        self.fields['content'].widget.attrs['class'] = "input_content"
        self.fields['content'].widget.attrs['rows'] = 1
        self.fields['content'].widget.attrs['columns'] = 40