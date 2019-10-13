from django import forms
from .choices import GENDER_CHOICES, MARITAL_STATUS_CHOCIES
from users.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Role, UserProfile

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        fields = ('email', 'password')



class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=30, required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=30, required=False, help_text='Optional.')
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    role = forms.ModelChoiceField(queryset=Role.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS_CHOCIES, widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    password1 = forms.CharField(label="Password", widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    password2 = forms.CharField(label="Confirm Password", widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2','gender', 'marital_status')



class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('gender', 'marital_status')