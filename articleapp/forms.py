from django.forms import ModelForm
from django import forms
from articleapp.models import Article
from projectapp.models import Project
class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                         'style': 'heigth: auto; text-align: left;'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    class Meta:
        model = Article
        fields = ['title', 'project', 'content', 'image']

    def __init__(self, *args, **kwargs):
        super(ArticleCreationForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['project'].label = "테마"
        self.fields['content'].label = "내용"
        self.fields['image'].label = "사진"