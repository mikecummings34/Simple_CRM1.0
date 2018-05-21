from django import forms
from django.forms import ModelForm, modelform_factory, ModelChoiceField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import *
from crm_app.models import *
from datetime import *
import time
from bootstrap3_datetime.widgets import DateTimePicker
from django_unixdatetimefield import UnixDateTimeField
from django.utils.dateformat import format



class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email', 
			'password1',
			'password2',
		)

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user 




class EditProfileForm(UserChangeForm):

	class Meta:
		model = User
		fields = (
			'email',
			'first_name',
			'last_name',
			'password'
		)

##Do I need this?
class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj 
##working function
## ticks = serviceticket.timestamp
## datetime(1,1,1) + timedelta(microseconds = ticks/10)
## output should be datetime.datetime(year, month, day, hour, minute, second ...etc)
#def testtime(*args, **kwargs):
#	dotnet = datetime(1,1,1)
#	times = datetime.now()
#	unix = times - dotnet
#	dotnettimestamp = (((unix.days*60*60*24 + unix.seconds)*1000 + unix.microseconds)*100)*100
#	return dotnettimestamp
from netunix import views
def movie():
	t = views.dotnet_unix().now()
	i = views.dotnet_unix().from_dotnet(t)
	m = datetime.fromtimestampe(str(i))
	return m

class NewTicketForm(forms.ModelForm):
	class Meta:
		model = Servicetickets
		fields = ("__all__")
		widgets = {
			#'ticketstartdate':DateTimePicker(options={"format": "YYYY/MM/DD HH:mm:ss"}, attrs={'onchange':'this.form.submit()'}),
			'technician': forms.Select(choices=Technicians.objects.values_list('nickname','nickname')),
			'ticket_title':forms.TextInput(attrs={'placeholder':'title', 'style':'font-size:48px;'}),
			'contact_name':forms.Select(attrs={'placeholder':'contact'}),

			
		}
	
	clientid = forms.IntegerField(widget=forms.Select(choices=Clientlist.objects.values_list('oid','clientname')
		))
	
	#technician = forms.CharField(widget=forms.Select(choices=Technicians.objects.values_list('nickname','nickname')))
	worktype = forms.CharField(widget=forms.Select(choices=Worktypes.objects.values_list('worktype', 'worktype')))
	ticketstartdate = forms.DateTimeField(widget=forms.HiddenInput())
	timestamp = forms.CharField(widget=forms.DateInput(attrs={
		"placeholder":'timestamp', "value":movie}))
	ticket_status = forms.CharField(widget=forms.Select(choices=Ticketstatuses.objects.values_list('oid','status')))


class NewTicketTimeEntries(forms.ModelForm):
	class Meta:
		model = Timeentries
		fields = ("__all__")
		widgets = {

			'notes':forms.TextInput(attrs={'placeholder':'Entry Notes'}),
			'technician': forms.Select(choices=Technicians.objects.values_list('nickname','nickname')),

		}

	timestamp = forms.CharField(widget=forms.DateInput(attrs={
		"placeholder":"timestamp", "value":movie})) 
	worktype = forms.CharField(widget=forms.Select(choices=Worktypes.objects.values_list('worktype', 'worktype'))) 
	startdate = forms.DateTimeField(widget=forms.HiddenInput())
	enddate = forms.DateTimeField(widget=forms.HiddenInput())
	
		
		

###works when testtime funtion in here and timestamp value is set to time. Need to figure out how to get time to update when a new instance is called and not
###when code is saved and server restarted. 
class testticket(forms.ModelForm):

	class Meta:
		model = Servicetickets
		fields = ("__all__")
		widgets = {
			#'ticketstartdate':DateTimePicker(options={"format": "YYYY/MM/DD HH:mm:ss"}, attrs={'onchange':'this.form.submit()'}),
			'technician': forms.Select(choices=Technicians.objects.values_list('nickname','nickname')),
			'ticket_title':forms.TextInput(attrs={'placeholder':'title'}),
			'contact_name':forms.TextInput(attrs={'placeholder':'contact'}),
			
		}
	
	clientid = forms.IntegerField(widget=forms.Select(choices=Clientlist.objects.values_list('oid','clientname')
		))
	#technician = forms.CharField(widget=forms.Select(choices=Technicians.objects.values_list('nickname','nickname')))
	worktype = forms.CharField(widget=forms.Select(choices=Worktypes.objects.values_list('worktype', 'worktype')))
	ticketstartdate = forms.DateTimeField(widget=forms.HiddenInput())
	timestamp = forms.CharField(widget=forms.DateInput(attrs={
		"placeholder":'timestamp', "value":movie}))
	ticket_status = forms.CharField(widget=forms.Select(choices=Ticketstatuses.objects.values_list('oid','status')))


class emailTest(forms.Form):
		subject = forms.CharField(required = True)	
		from_email = forms.EmailField(required=True)		
		message = forms.CharField()
		



	



		
		 
    
		

