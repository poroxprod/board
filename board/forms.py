from django import forms
from .models import Post


class ContactForm(forms.Form):
    sender = forms.EmailField(label='Email')
    message = forms.CharField(label='Текст сообщения', widget=forms.Textarea(attrs={'class': 'form-control'}))
    photo = forms.ImageField(label='Фото')


class PostForm(forms.ModelForm):
    class Meta:

        model = Post
        fields = ('title', 'text', 'city', 'metro', 'email','photo')
