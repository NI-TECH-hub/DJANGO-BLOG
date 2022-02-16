



# from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _
from .models import Post

# from miniblog.blog.models import Post
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='password(Again)', widget= forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email','username':'userID'}
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs=
            {'class':'form-control'}),
        }

class LogInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description']
        labels = {'title':'Title','description':'desc'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
        'desc':forms.Textarea(attrs={'class':'form-control'}),
        }