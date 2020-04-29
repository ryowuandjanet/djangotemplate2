from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title=forms.CharField(label='標題',widget=forms.TextInput(
        attrs={
            "placeholder":"請輸入標題",
            "class":"form-control col-md-6"
        }))
    body=forms.CharField(label='內文',widget=forms.Textarea(
        attrs={
            "placeholder":"請輸入內文",
            "class":"form-control col-md-6",
            "rows":20,
            "cols":120
        }))
    class Meta:
        model=Post
        fields='__all__'