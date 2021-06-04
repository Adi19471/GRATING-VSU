from django import forms

# from .models import User

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class UserReg(UserCreationForm):
    # password1:forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # password2:forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-Enter Your Passwowd'}))

   
    class Meta:
      
        model = User
        fields = ['username','email']

        
        widgets={
        'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Id'}),
        'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email iD example@gmail.com'}),

       
        }