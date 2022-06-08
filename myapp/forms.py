from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import *




class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',error_messages={'username':{'required':'username required'}})
    password = forms.CharField(label='Password',error_messages={'password':{'required':'password required'}})

class SignUp(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','gender','mobile','location']
        Widget={
            'username': forms.TextInput(attrs={'class':'form-control','label':'Username'}),
            'first_name': forms.TextInput(attrs={'class':'form-control','label':'Name'}),
            'gender': forms.Select(attrs={'class':'form-control','label':'Gender'}),
            'mobile': forms.TextInput(attrs={'class':'form-control','label':'Mobile No'}),
            'location': forms.TextInput(attrs={'class':'form-control','label':'Address'}),
        }

class AddPostForm(forms.ModelForm):
    class Meta:
        model=AddPost
        fields=['post','description']

class EditForm(UserChangeForm):
    class Meta:
        model=User
        fields=['first_name','mobile','gender','location','profile']

        Widget={
           'first_name': forms.TextInput(attrs={'class':'form-control','label':'Name'}),
            'mobile': forms.TextInput(attrs={'class':'form-control','label':'Mobile No'}),
            'gender': forms.Select(attrs={'class':'form-control','label':'Gender'}),
            'location': forms.TextInput(attrs={'class':'form-control','label':'Address'}),
            'profile': forms.TextInput(attrs={'class':'form-control','label':'Profile'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment']
        Widget={
           'comment': forms.Textarea(attrs={'class':'form-control','label':'Comment'}),
        }
        