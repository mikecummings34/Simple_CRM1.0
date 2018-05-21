from django.shortcuts import render, redirect
from django.db import connections, connection, models
from accounts.models import *
from crm_app.models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from crm_app.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from django.http import HttpResponse, JsonResponse
from django.db.models import F



# Create your views here.
def view_profile(request):
	if request.method == 'POST':
		if 'recent_tickets' in request.POST and request.POST['recent_tickets']:
			techname = request.POST['recent_tickets']
			tickets = Servicetickets.objects.filter(technician=techname).order_by('-ticketstartdate')
			lib={'user':request.user,'tickets':tickets}
			return render (request, 'crm_temps/view-profile.html', lib)
	else:		
		args = {'user': request.user}
		return render(request, 'crm_temps/view-profile.html', args)

def ticket_detail(request):
	if request.method == "GET":
		if 'ticket' in request.GET and request.GET['ticket']:
			q= request.GET['ticket']
			qset = Servicetickets.objects.get(oid=q)
			tset = Timeentries.objects.filter(ticketid = q)
			lib = {'tickets':qset, 'entries':tset}
			return render(request, 'crm_temps/ticket-details.html', lib)

def new_entry(request):
	if request.method == "GET":
		if 'editticket' in request.GET and request.GET['editticket']:
			req = request.GET['editticket']
			entry = NewTicketTimeEntries(request.GET)
			initialvalue = NewTicketTimeEntries(initial = {'ticketid':req})
			ticketreq = Servicetickets.objects.get(oid = req)
			timeentries = Timeentries.objects.filter(ticketid = req)
			lib = {'entries':entry, "tid":initialvalue, "ticket":ticketreq, "timeentries":timeentries}
			return render(request, 'crm_temps/forms/new-entry.html', lib)
	if request.method == "POST":
		entry = NewTicketTimeEntries(request.POST)
		if entry.is_valid():
			s = entry.save()
			return HttpResponse('saved')
