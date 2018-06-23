"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from projectcrm import views
from . import views
from django.urls import reverse
##import views from accounts
from accounts import views as accountview

urlpatterns = [
	url(r'^$', views.view_profile.as_view(), name = 'view_profile'),
	url(r'^tickets/details/$', views.ticket_detail.as_view(), name='ticket_detail'),
	url(r'^tickets/new-entry/$', views.new_entry, name='new_entry'),
    url(r'^new-ticket/$', views.create_ticket.as_view(), name='create_ticket'),
    url(r'^tickets/$', views.tickets, name='tickets'),
    url(r'ajax_req/$', views.ajax_req, name='ajax_req'),
    url(r'^ajax/$', views.TicketFilter, name='ticket-filter'),
    url(r'^ticketform/$', views.ajax_form, name='ajax-form'),



    url(r'^client/$', views.ClientGet.as_view(), name='client'),
    url(r'^clientq/$', views.ClientPostQ.as_view(), name = 'client_detail'),
    url(r'^client_tech/$', views.ClientGetTech.as_view(), name = 'client_tech'),
    url(r'^client_tickets/$', views.ClientPostTickets.as_view(), name = 'client_tickets'),

    #url(r'^clienttest/$',  views.clienttest.as_view(), name = "clienttest"),	
    #url(r'^clientposttest/$',  views.clientposttest.as_view(), name = "clientposttest"),
    



]