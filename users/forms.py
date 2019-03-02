from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField(required=True)
	middle_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	national_Id = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	mobile_number = forms.CharField(required=True)
	location = forms.CharField(required=True)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'middle_name',  'last_name', 'national_Id',  'email', 'mobile_number', 'location', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
	first_name = forms.CharField(required=True)
	middle_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	national_Id = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	mobile_number = forms.CharField(required=True)
	location = forms.CharField(required=True)



	class Meta:
		model = User
		fields = ['username', 'first_name', 'middle_name',  'last_name', 'national_Id',  'email', 'mobile_number', 'location']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']

	

