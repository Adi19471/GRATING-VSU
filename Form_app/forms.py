from django import forms

from Form_app.models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register

        fields = '__all__'
        widgets = {
            
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Name'}),
            'mobile_no':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your Phone Number'}),
            'age':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your age'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
            'adharDetailes':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your Adhar 12-digit Number'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your address'}),

        }
        



# 'readonly':'True'