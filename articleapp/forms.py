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
        self.fields['title'].widget.attrs.update({'class':'input_title','placeholder':'제목 추가'})
        self.fields['content'].widget.attrs.update({'class':'input_content','placeholder':'사진에 대해 설명해 보세요.','rows':'1','columns':'40'})
        self.fields['image'].widget.attrs.update({'id':'input_img','onchange':'upload_img(this)','oninvalid':'alert("사진을 첨부해주세요!")'})
        self.fields['project'].widget.attrs.update({'class':'input_project'})