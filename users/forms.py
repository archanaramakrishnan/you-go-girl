from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birthdate = forms.DateField(help_text='Required. Format: MM/DD/YYYY')
    location = forms.CharField(max_length=30)
    spoken_language = forms.CharField(max_length=50)
    preferred_programming_language = forms.CharField(max_length=50)
    bio = forms.CharField(max_length=500, help_text='<500 characters')
    sign_up_as_mentor = forms.BooleanField(help_text='Yes')
    hrs_per_week_available = forms.IntegerField()
    university = forms.CharField(max_length=100)
    company = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'email', 
            'birthdate', 
            'location',
            'spoken_language',
            'preferred_programming_language',
            'bio',
            'sign_up_as_mentor',
            'hrs_per_week_available',
            'university',
            'company',
            'username',  
            'password1', 
            'password2',
            ]