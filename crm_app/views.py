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


def create_ticket(request):
	if request.method == "GET":
		ticket = NewTicketForm(request.GET)
		entries = NewTicketTimeEntries(request.GET)
		lib = {'ticket':ticket, 'entries':entries}
		return render(request, 'crm_temps/forms/new-ticket.html', lib)
		
	if request.method == "POST":
		ticket = NewTicketForm(request.POST)
		entries = NewTicketTimeEntries(request.POST)
		subject = request.POST.get("ticket_title","")
		message = request.POST.get("notes","")
		from_email = request.POST.get("emailcomplete","")
		if ticket.is_valid() and entries.is_valid():
			m = ticket.save()
			entryintance = entries.instance
			k = m.timestamp
			ticket.save()
			v = Servicetickets.objects.get(timestamp = k)
			f = v.oid
			p = entryintance.ticketid
			entryintance.ticketid = f
			entries.save()
			
			send_mail(subject, message, from_email, ['admin@example.com'])

			return HttpResponse(entryintance.ticketid)

def tickets(request):
	if request.method == "GET":

		if 'cid' in request.GET and request.GET['cid']:
			q = request.GET['cid']
			tickets = Servicetickets.objects.filter(clientid=q)
			lib = {'tickets':tickets}
			return render(request, 'crm/tickets.html', lib)
		elif 'tech' in request.GET and request.GET['tech']:
			q=request.GET['tech']
			tickets = Servicetickets.objects.filter(technician=q)
			lib = {'tickets':tickets}
			return render(request, 'crm/tickets.html', lib)
		elif 'filter' in request.GET and request.GET['filter']:
			q = request.GET['filter']
			tickets = Servicetickets.objects.filter(ticket_status=1)
			lib={'tickets':tickets}
			return render(request, 'crm/tickets.html')

		else:	
			tickets = Servicetickets.objects.all().order_by('-ticketstartdate')[:30]
			lib = {'tickets': tickets}
			return render(request, 'crm/tickets.html', lib)

def client(request):
	if request.method == "POST":
		if 'q' in request.POST and request.POST['q']: 
			q = request.POST['q']
			profile = Clientlist.objects.get(oid=q)
			contact = Contacts.objects.filter(clientid = q)
			 
			 
			lib= {'clientinfo':profile, 'contact':contact}
			return render(request, 'crm_temps/client_profile.html',lib)
		else:
			q = request.POST['tickets']
			tickets = Servicetickets.objects.filter(clientid=q).order_by("-timestamp")
			test = Clientlist.objects.get(oid=q)
			lib= {'tickets':tickets,
				  'name':test,
				  }

			return render(request, 'crm_temps/tickets.html',lib)
	elif request.method == "GET":
			if 'tech' in request.GET and request.GET['tech']:
				q = request.GET['tech']
				qset = Servicetickets.objects.filter(technician=q)
				lib = {'tickets': qset}
				return render(request, 'crm_temps/ticket-details.html', lib)
			else:
				query = Clientlist.objects.all().values()
				prnt = print(request)
				value = {'client': query}
				return render(request, 'crm_temps/client.html', value)

from django.views.generic import ListView

class clienttest(ListView): ##pass kwargs
	model = Clientlist
	queryset = Clientlist.objects.all()
	template_name = 'crm_temps/client.html'
	context_object_name = 'client'
