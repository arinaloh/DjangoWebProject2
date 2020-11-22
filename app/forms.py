"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=200,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class OtzyvForm(forms.Form):
	name = forms.CharField(label='Ваше имя', min_length=2, max_length=20)
	gender = forms.ChoiceField(label='Ваш пол',
						  choices=[('1','мужской'),('2','женский')],
						  widget=forms.RadioSelect,initial=1)
	Forwho = forms.CharField(label='Для кого приобретали цветы?', min_length=2, max_length=20)
	Cause = forms.CharField(label='По какому случаю?', min_length=2, max_length=20)	
	Feedback = forms.CharField(label='Оставьте отзыв.Помогите нам стать лучше для Вас', 
							widget=forms.Textarea(attrs={'rows':12, 'cols':20}))
	notice = forms.BooleanField(label='Получать новости нашего магазина по e-mail?',
							 required=False)
	email = forms.EmailField(label='Ваш e-mail', min_length=7)

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ('text',) 
        labels = {'text': "Введите комментарий"} 

class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog # используемая модель
        fields = ('title', 'description', 'content', 'image',) 
        labels = {'title': "Заголовок", 'description':"Краткое содержание", 'content':"Полное содержание", 'image':"Картинка"} 