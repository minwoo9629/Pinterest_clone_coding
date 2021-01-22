from django.forms import ModelForm
from django import forms
from articleapp.models import Article
from projectapp.models import Project
class ArticleCreationForm(ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    image = forms.ImageField(widget=forms.FileInput)
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

        self.fields['image'].widget.attrs['id'] = "input_img"
        self.fields['image'].widget.attrs['onchange'] = "upload_img(this)"
        self.fields['image'].widget.attrs['oninvalid'] = "alert('사진을 첨부해주세요!')"

        self.fields['project'].widget.attrs['class'] = "input_project"