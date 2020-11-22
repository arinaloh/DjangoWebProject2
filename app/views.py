"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from.forms import OtzyvForm
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Blog
from .models import Comment # использование модели комментариев
from .forms import CommentForm # использование формы ввода комментария
from .forms import BlogForm


def links(request):
	"""Reners the links page."""
	assert isinstance(request, HttpRequest) 
	return render(
        request,
        'app/links.html',
        {
            'title':'Полезные ресурсы',
            'message':'Это может быть интересно для Вас',
            'year':datetime.now().year,
        }
	)


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Как можно с нами связаться',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Сведения о нас',
            'year':datetime.now().year,
        }
    )

def otzyv(request):
    assert isinstance(request, HttpRequest) 
    data = None
    gender={'1': 'мужской','2':'женский'}
    if request.method == 'POST':
        form = OtzyvForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['gender'] = gender[ form.cleaned_data['gender'] ]
            data['Forwho'] = form.cleaned_data['Forwho']
            data['Cause'] = form.cleaned_data['Cause']
            data['Feedback'] = form.cleaned_data['Feedback']
            if(form.cleaned_data['notice']== True):
                data['notice'] = 'Да'
            else:
                data['notice'] = 'Нет'
            data['email'] = form.cleaned_data['email']
            form = None 
    else:
        form = OtzyvForm()
    return render(
        request,
        'app/otzyv.html',
        {
            'title':'Отзыв',
            'form':form,
            'data':data
        }
        )

def registration(request):
    """Renders the registration page."""
    assert isinstance(request, HttpRequest)
    if request.method == "POST": 
        regform = UserCreationForm (request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True 
            reg_f.is_superuser = False 
            reg_f.date_joined = datetime.now() 
            reg_f.last_login = datetime.now() 
            reg_f.save()
            return redirect('login') 
    else:
        regform = UserCreationForm()
    return render(
        request,
        'app/registration.html',
        {
            'title':'Регистрация',
            'regform': regform, 
            'year':datetime.now().year,
        }
    ) 

def blog(request):

    """Renders the blog page."""
    posts = Blog.objects.all() 
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title':'Блог',
            'posts': posts, 
            'year':datetime.now().year,
        }
    )

def blogpost(request, parametr):

    """Renders the blogpost page."""
    post_1 = Blog.objects.get(id=parametr) 
    comments = Comment.objects.filter(post=parametr)
    if request.method == "POST": 
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now() 
            comment_f.post = Blog.objects.get(id=parametr) 
            comment_f.save() 
            return redirect('blogpost', parametr=post_1.id) 
    else:
        form = CommentForm() 
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {
            'title': post_1,
            'post_1': post_1,
            'comments': comments,
            'form': form, 
            'year':datetime.now().year,
        }
    )

def newpost(request):
    """Renders the newpost page."""
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user
            blog_f.save()
            return redirect('blog')
    else:
        blogform = BlogForm() 
    return render(
        request,
        'app/newpost.html',
        {
            'title':'Добавление статьи',
            'blogform': blogform,
            'year':datetime.now().year,
        }
    )

def videopost(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Видео',
            'year':datetime.now().year,
        }
    )