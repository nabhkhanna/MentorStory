from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class UpdateMentor(ModelForm):
    class Meta:
        model = Mentor
        fields = '__all__'
        exclude = ['user']


class UpdateMentee(ModelForm):
    class Meta:
        model = Mentee
        fields = '__all__'
        exclude = ['user']


class CreateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['mentee','taken','mentor']


