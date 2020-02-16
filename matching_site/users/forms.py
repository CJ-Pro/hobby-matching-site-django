from django import forms
from django.contrib.auth.models import User
from match.models import Hobby,Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=(('Male', 'Male'), ('Female', 'Female')))
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1940, 2001)))
    hobbies = forms.ModelMultipleChoiceField(queryset=Hobby.objects.all(),widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'gender', 'date_of_birth', 'hobbies']


class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
