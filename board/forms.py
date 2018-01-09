from django import forms
from .models import Post


class ContactForm(forms.Form):
    # subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    sender = forms.EmailField(label='Email')
    message = forms.CharField(label='Текст сообщения', widget=forms.Textarea(attrs={'class': 'form-control'}))
    # copy = forms.BooleanField(required=False)
    #img = forms.ImageField()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'email', 'photo')
