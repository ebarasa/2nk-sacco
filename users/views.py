from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your Account has been Created! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
	return render(request, 'users/profile.html')

def activities(request):
	return render(request, 'users/activities.html')

def details(request):
	return render(request, 'users/details.html')

def report(request):
	return render(request, 'users/report.html')
