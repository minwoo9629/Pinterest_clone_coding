from django.forms import ModelForm
from commentapp.models import Comment

class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(CommentCreationForm, self).__init__(*args, **kwargs)
        # self.fields['content'].widget.attrs.update({'id':'comment_input','placeholder':'댓글 입력','label':'','rows':'1','cols':'20'})
        self.fields['content'].label = ''
        self.fields['content'].widget.attrs['rows'] = 1
        self.fields['content'].widget.attrs['cols'] = 20
        self.fields['content'].widget.attrs['placeholder'] = '댓글입력'
        self.fields['content'].widget.attrs['id'] = 'comment_input'