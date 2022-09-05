from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class userRegForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password_again = forms.CharField(label='Repeat Password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name', 'email')

    def cleaned_password_again(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_again']:
            raise forms.ValidationError('Password didn\'t match')

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')