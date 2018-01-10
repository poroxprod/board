import post
from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm, ContactForm
from django.core.mail import EmailMessage


# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-published_date')[:100]
    premium = Post.objects.all().filter(premium=True).order_by('-published_date')[:5]
    return render(request, 'post_list.html', {'posts': posts, 'premium': premium})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_add.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def contactform(reguest, pk):
    post = get_object_or_404(Post, pk=pk)
    # return HttpResponse(img)
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST, reguest.FILES)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = post.title
            to = post.email
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message'] + '\n' + 'Почтовый адрес отправителя: ' + sender
            photo = reguest.FILES['photo']
            recepients = [to]
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            try:
                mail = EmailMessage(subject, message, 'metrika.aion-fly.ru@yandex.ru', recepients)
                mail.attach(photo.name, photo.read(), photo.content_type)
                mail.send()
                return redirect('post_detail', pk=post.pk)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
        # return redirect('post_detail', pk=post.pk)

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(reguest, 'send.html', {'form': form, 'post': post})

def about(request):
    return render(request,'about.html')
