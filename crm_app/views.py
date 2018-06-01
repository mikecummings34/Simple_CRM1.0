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
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.views.generic import ListView, FormView, View, DetailView
from django.shortcuts import get_object_or_404



# Create your views here.
"""
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
"""




##class based view of view profile

'''
def ticket_detail(request):
	if request.method == "GET":
		if 'ticket' in request.GET and request.GET['ticket']:
			q= request.GET['ticket']
			qset = Servicetickets.objects.get(oid=q)
			tset = Timeentries.objects.filter(ticketid = q)
			lib = {'tickets':qset, 'entries':tset}
			return render(request, 'crm_temps/ticket-details.html', lib)
'''




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
			return render(request, 'crm_temps/tickets.html', lib)
		elif 'tech' in request.GET and request.GET['tech']:
			q=request.GET['tech']
			tickets = Servicetickets.objects.filter(technician=q)
			lib = {'tickets':tickets}
			return render(request, 'crm_temps/tickets.html', lib)
		elif 'filter' in request.GET and request.GET['filter']:
			q = request.GET['filter']
			tickets = Servicetickets.objects.filter(ticket_status=1)
			lib={'tickets':tickets}
			return render(request, 'crm_temps/tickets.html')

		else:	
			tickets = Servicetickets.objects.all().order_by('-ticketstartdate')[:30]
			lib = {'tickets': tickets}
			return render(request, 'crm_temps/tickets.html', lib)

'''
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
'''

###this could work, but need to render different templates for each request type.
'''
class client(ListView):
	#model = Clientlist
	#query_set = Clientlist.objects.all()
	#template_name = []
	#context_object_name = 'client'

	def get_context_data(self, **kwargs):
		context = super(client, self).get_context_data(**kwargs)
		if self.request.method == 'GET':
			if self.request.GET == 'tech':
				context['tickets'] = Servicetickets.objects.filter(technician = self.request.GET['tech'])
				return context
			else:
				context['client'] = Clientlist.objects.all().values()
				return context
		if self.request.method == "POST":
			if self.request.POST == 'q':
				context['clientinfo'] = Clientlist.objects.get(oid = self.request.POST['q'])
				context['contact'] = Contacts.objects.filter(clientid = self.request.POST['q'])
				return context
			if self.request.POST == 'tickets':
				context['tickets'] = Servicetickets.objects.filter(clientid = self.request.POST['tickets'])
				context['name'] = Clientlist.objects.get(oid = self.request.POST['tickets'])
				return context 

	def get_queryset(self):
		if self.queryset is None:
			if self.request.method == "GET":
				self.queryset = Clientlist.objects.all()
				return self.queryset
			if self.request.method == "POST":
				if 'q' in self.request.POST and self.request.POST['q']:
					self.queryset


	def post(self, request, *args, **kwargs):
		if self.request.method == "POST":
			self.object_list = self.get_queryset()
			allow_empty = self.get_allow_empty()
			context = self.get_context_data()
			return self.render_to_response(context)

	def get_template_names(self):
		self.template_name ='crm_temps/client.html'
		#template_name = super(client, self).get_template_names()
		req = self.request
		if req.method == "GET":
			template_name = 'crm_temps/client.html'
			return self.template_name
		if self.request.method == "POST":
			if 'q' in self.request.POST and self.request.POST['q']:
				self.template_name = 'crm_temps/client_profile.html'
				return super(client, self).get_template_names()


'''




'''
class client_detail(ListView):
	#query_set = Clientlist.objects.all()
	template_name = 'crm_temps/client_profile.html'
	context_object_name = "clientinfo"
	#extra_context = {'contact':Contacts.objects.all()}
	#query_set = Clientlist.objects.all()
	#model = Clientlist

	def get_context_data(self, **kwargs):
		context = super(clientposttest, self).get_context_data(**kwargs)
		context['contact'] =  Contacts.objects.filter(clientid = self.request.GET['q'])
		context['clientinfo'] = Clientlist.objects.get(oid = self.request.GET['q'])
		return context

	def get_queryset(self):
		if self.queryset is None:
			return self.queryset
'''





## Client Functions in CBV START HERE##
######################################
#####################################
####################################
class ClientMixin(object):
	"""Main mixin for client based functions. Change this before live. failed on get is an option so resubmitting
	a posted page will redirect to post it again"""
	failed_on_get = False
	def get_queryset(self, **kwargs):
		if self.queryset is None:
			return self.queryset

	def post(self, *args, **kwargs):
		if self.request.method == "POST" or self.failed_on_get == 'True':
			self.object_list = self.get_queryset()
			allow_empty = self.get_allow_empty()
			context = self.get_context_data()
			return self.render_to_response(context)

##vvvvvCBVs that Inherit from Client Mixin vvvvvvv###
class view_profile(ClientMixin, ListView):

	template_name = 'crm_temps/view-profile.html'
	context_object_name = 'placeholder'
	http_method_names = ['get','post']
	
	def get_context_data(self, **kwargs):
		context = super(view_profile, self).get_context_data(**kwargs)
		if self.request.method == "POST":
			context['user'] =  self.request.user
			context['tickets'] = Servicetickets.objects.filter(technician = self.request.POST['recent_tickets']).order_by('-ticketstartdate')
			return context
		else:
			context['user'] = self.request.user
			return context

	def get_queryset(self):
		if self.queryset is None:
			return self.queryset

	def post(self, request, *args, **kwargs):
		if self.request.method == "POST":
			self.object_list = self.get_queryset()
			allow_empty = self.get_allow_empty()
			context = self.get_context_data()
			return self.render_to_response(context)
		else:
			HttpResponse("fuck you")

class ticket_detail(ClientMixin, ListView):
	template_name = 'crm_temps/ticket-details.html'
	context_object_name = 'placeholder'

	def get_context_data(self, **kwargs):
		context = super(ticket_detail, self).get_context_data(**kwargs)
		context['tickets'] =  Servicetickets.objects.get(oid = self.request.GET['ticket'])
		context['entries'] = Timeentries.objects.filter(ticketid = self.request.GET['ticket'])
		return context

class ClientPostQ(ClientMixin, ListView):
	template_name = "crm_temps/client_profile.html"

	def get_context_data(self, **kwargs):
		context = super(ClientPostQ, self).get_context_data(**kwargs)
		context['clientinfo'] = Clientlist.objects.get(oid = self.request.POST['q'])
		context['contact'] = Contacts.objects.filter(clientid = self.request.POST['q'])
		return context
	def get(self, request, *args, **kwargs):
		return HttpResponseRedirect(reverse('crm:client'))

class ClientPostTickets(ClientMixin, ListView):
	template_name = "crm_temps/tickets.html"

	def get_context_data(self, **kwargs):
		context['tickets'] = Servicetickets.objects.filter(clientid=self.request.POST['tickets']).order_by("-timestamp")
		context['name'] = Clientlist.objects.get(oid = self.request.POST['tickets'])
		return context

class ClientGetTech(ClientMixin, ListView):
	template_name = "crm_temps/ticket-detail.html"

	def get_context_data(self, **kwargs):
		context['tech'] = Servicetickets.objects.filter(technician=self.request.POST['tech'])
		return context


class ClientGet(ListView):
	template_name = "crm_temps/client.html"
	model = 'Clientlist'
	queryset = Clientlist.objects.all()
	context_object_name = 'client'

####^^^^^^^End of ClientMixin CBVs^^^^^^^^^^########
##################################################
#####################################################

	





