from django.shortcuts import render, redirect, reverse
from django.db import connections, connection, models
from accounts.models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from accounts.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	return redirect ('../crm')

def register(request):
	if request.method=='POST':##POST to custom form not tested
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account') 
	else:
		form = RegistrationForm()
		args= {'form': form}
		return render(request, 'accounts/reg_form.html', args)




def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance = request.user)

		if form.is_valid():
			form.save()
			return redirect('/account/profile')
	else:
		form = EditProfileForm(instance=request.user)
		args= {'form':form}
		return render(request, 'accounts/edit_profile.html', args)



def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user = request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/account/profile')
		else:
			return redirect('account/change-password')
	else:
		form = PasswordChangeForm(user=request.user)
		args= {'form':form}
		return render(request, 'accounts/change_password.html', args)


##Make class based view to change where it redirects too.
