# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django_unixdatetimefield import UnixDateTimeField

# Create your models here.
class Clientlist(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    techsupportplan = models.CharField(db_column='TechSupportPlan', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extension = models.CharField(db_column='Extension', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fax_number = models.CharField(db_column='Fax Number', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    primarycontact = models.CharField(db_column='PrimaryContact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    donotassist = models.NullBooleanField(db_column='DoNotAssist')  # Field name made lowercase.
    clienttype = models.IntegerField(db_column='ClientType', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientList'


class Clientnotes(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    category = models.IntegerField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    new_ticket_popup = models.CharField(db_column='New Ticket Popup', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'ClientNotes'


class Clienttypes(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createtickets = models.NullBooleanField(db_column='CreateTickets')  # Field name made lowercase.
    defaultchecked = models.NullBooleanField(db_column='DefaultChecked')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientTypes'


class Companyinventory(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemID')  # Field name made lowercase.
    typeid = models.IntegerField(db_column='TypeID', blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    datereceived = models.DateTimeField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
    dateinstalled = models.DateTimeField(db_column='DateInstalled', blank=True, null=True)  # Field name made lowercase.
    itemnotes = models.TextField(db_column='ItemNotes', blank=True, null=True)  # Field name made lowercase.
    currentclient = models.IntegerField(db_column='CurrentClient', blank=True, null=True)  # Field name made lowercase.
    billed = models.DateTimeField(db_column='Billed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CompanyInventory'
        unique_together = (('oid', 'itemid'),)


class Companyinventorydetail(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyinventoryid = models.IntegerField(db_column='CompanyInventoryID', blank=True, null=True)  # Field name made lowercase.
    serviceticket = models.IntegerField(db_column='ServiceTicket', blank=True, null=True)  # Field name made lowercase.
    client = models.IntegerField(db_column='Client', blank=True, null=True)  # Field name made lowercase.
    workstart = models.DateTimeField(db_column='WorkStart', blank=True, null=True)  # Field name made lowercase.
    workstop = models.DateTimeField(db_column='WorkStop', blank=True, null=True)  # Field name made lowercase.
    detailnotes = models.TextField(db_column='DetailNotes', blank=True, null=True)  # Field name made lowercase.
    billable = models.NullBooleanField(db_column='Billable')  # Field name made lowercase.
    billed = models.NullBooleanField(db_column='Billed')  # Field name made lowercase.
    billableamount = models.DecimalField(db_column='BillableAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CompanyInventoryDetail'


class Contacts(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone Number', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    extension = models.CharField(db_column='Extension', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cell_phone = models.CharField(db_column='Cell Phone', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primary = models.NullBooleanField(db_column='Primary')  # Field name made lowercase.
    sendticketassignemail = models.NullBooleanField(db_column='SendTicketAssignEmail')  # Field name made lowercase.
    sendticketcompleteemail = models.NullBooleanField(db_column='SendTicketCompleteEmail')  # Field name made lowercase. 

    class Meta:
        managed = False
        db_table = 'Contacts'


class Internalemailaddresses(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    smtphost = models.CharField(db_column='SmtpHost', max_length=255, blank=True, null=True)  # Field name made lowercase.
    smtpport = models.IntegerField(db_column='SmtpPort', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InternalEmailAddresses'


class Inventoryitems(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    model_number = models.CharField(db_column='Model Number', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    upc = models.CharField(db_column='UPC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    currentinventoryitem = models.NullBooleanField(db_column='CurrentInventoryItem')  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    client_price = models.DecimalField(db_column='Client Price', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reorderthreshold = models.IntegerField(db_column='ReorderThreshold', blank=True, null=True)  # Field name made lowercase.
    parcount = models.IntegerField(db_column='ParCount', blank=True, null=True)  # Field name made lowercase.
    vendorid = models.IntegerField(db_column='VendorID', blank=True, null=True)  # Field name made lowercase.
    manufacturerid = models.IntegerField(db_column='ManufacturerID', blank=True, null=True)  # Field name made lowercase.
    itemnotes = models.TextField(db_column='ItemNotes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryItems'


class Inventorystatuses(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    inventorystatus = models.CharField(db_column='InventoryStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    defaultchecked = models.NullBooleanField(db_column='DefaultChecked')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryStatuses'


class Options(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientassignemailsubject = models.CharField(db_column='ClientAssignEmailSubject', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clientassignemailbody = models.TextField(db_column='ClientAssignEmailBody', blank=True, null=True)  # Field name made lowercase.
    clientcompleteemailsubject = models.CharField(db_column='ClientCompleteEmailSubject', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clientcompleteemailbody = models.TextField(db_column='ClientCompleteEmailBody', blank=True, null=True)  # Field name made lowercase.
    internalassignemailsubject = models.CharField(db_column='InternalAssignEmailSubject', max_length=255, blank=True, null=True)  # Field name made lowercase.
    internalassignemailbody = models.TextField(db_column='InternalAssignEmailBody', blank=True, null=True)  # Field name made lowercase.
    internalcompleteemailsubject = models.CharField(db_column='InternalCompleteEmailSubject', max_length=255, blank=True, null=True)  # Field name made lowercase.
    internalcompleteemailbody = models.TextField(db_column='InternalCompleteEmailBody', blank=True, null=True)  # Field name made lowercase.
    rootfolder = models.CharField(db_column='RootFolder', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ticketnumber = models.IntegerField(db_column='TicketNumber', blank=True, null=True)  # Field name made lowercase.
    default_technician = models.IntegerField(db_column='Default Technician', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    refreshinterval = models.IntegerField(db_column='RefreshInterval', blank=True, null=True)  # Field name made lowercase.
    inventoryordersubject = models.CharField(db_column='InventoryOrderSubject', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inventoryorderbody = models.TextField(db_column='InventoryOrderBody', blank=True, null=True)  # Field name made lowercase.
    inventoryordertoemail = models.CharField(db_column='InventoryOrderToEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Options'


class PasteErrors(models.Model):
    oid = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    ticketid = models.IntegerField(db_column='TicketID', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.CharField(db_column='TimeStamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    technician = models.CharField(db_column='Technician', max_length=255, blank=True, null=True)  # Field name made lowercase.
    worktype = models.CharField(db_column='WorkType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Paste Errors'


class Reservedwords(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    word = models.CharField(db_column='Word', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReservedWords'


class SavedContacts(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID', blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber1 = models.CharField(db_column='PhoneNumber1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber2 = models.CharField(db_column='PhoneNumber2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primary = models.NullBooleanField(db_column='Primary')  # Field name made lowercase.
    sendticketassignemail = models.NullBooleanField(db_column='SendTicketAssignEmail')  # Field name made lowercase.
    sendticketcompleteemail = models.NullBooleanField(db_column='SendTicketCompleteEmail')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Saved Contacts'


class Servicetickets(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    timestamp = models.CharField(db_column='TimeStamp', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientID')  # Field name made lowercase.
    ticket_title = models.CharField(db_column='Ticket Title', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    technician = models.CharField(db_column='Technician', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contact_name = models.CharField(db_column='Contact Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ticketstartdate = models.DateTimeField(db_column='TicketStartDate', blank=True, null=True)  # Field name made lowercase.
    time_spent_minutes_field = models.IntegerField(db_column='Time Spent (Minutes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ticket_status = models.IntegerField(db_column='Ticket Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    worktype = models.CharField(db_column='WorkType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    internal_notes = models.TextField(db_column='Internal Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    client_notes = models.TextField(db_column='Client Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    complete = models.NullBooleanField(db_column='Complete')  # Field name made lowercase.
    ticketcategory1 = models.IntegerField(db_column='TicketCategory1', blank=True, null=True)  # Field name made lowercase.
    ticketcategory2 = models.IntegerField(db_column='TicketCategory2', blank=True, null=True)  # Field name made lowercase.
    ticketcategory3 = models.IntegerField(db_column='TicketCategory3', blank=True, null=True)  # Field name made lowercase.
    billable = models.IntegerField(db_column='Billable', blank=True, null=True)  # Field name made lowercase.
    billed = models.NullBooleanField(db_column='Billed')  # Field name made lowercase.
    ticketnumber = models.IntegerField(db_column='TicketNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServiceTickets'
        unique_together = (('oid', 'clientid'),)


class Techsupportplans(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    planname = models.CharField(db_column='PlanName', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TechSupportPlans'


class Technicians(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='Nickname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fromemailaddress = models.IntegerField(db_column='FromEmailAddress', blank=True, null=True)  # Field name made lowercase.
    toemailaddress = models.IntegerField(db_column='ToEmailAddress', blank=True, null=True)  # Field name made lowercase.
    editclosedtickets = models.NullBooleanField(db_column='EditClosedTickets')  # Field name made lowercase.
    editclients = models.NullBooleanField(db_column='EditClients')  # Field name made lowercase.
    editsettings = models.NullBooleanField(db_column='EditSettings')  # Field name made lowercase.
    billing = models.NullBooleanField(db_column='Billing')  # Field name made lowercase.
    viewotherstickets = models.NullBooleanField(db_column='ViewOthersTickets')  # Field name made lowercase.
    assignticketstoothers = models.NullBooleanField(db_column='AssignTicketsToOthers')  # Field name made lowercase.
    alloweditsendemail = models.NullBooleanField(db_column='AllowEditSendEmail')  # Field name made lowercase.
    sendemaildefailt = models.NullBooleanField(db_column='SendEmailDefailt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Technicians'


class Ticketcategory1(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TicketCategory1'


class Ticketcategory2(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    category1id = models.IntegerField(db_column='Category1ID')  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TicketCategory2'
        unique_together = (('oid', 'category1id'),)


class Ticketcategory3(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    category1id = models.IntegerField(db_column='Category1ID')  # Field name made lowercase.
    category2id = models.IntegerField(db_column='Category2ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TicketCategory3'
        unique_together = (('oid', 'category1id', 'category2id'),)


class Ticketstatuses(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    defaultforticketview = models.NullBooleanField(db_column='DefaultForTicketView')  # Field name made lowercase.
    defaultforbillingview = models.NullBooleanField(db_column='DefaultForBillingView')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TicketStatuses'


class Timeentries(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ticketid = models.IntegerField(db_column='TicketID')  # Field name made lowercase.
    timestamp = models.CharField(db_column='TimeStamp', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    technician = models.CharField(db_column='Technician', max_length=255, blank=True, null=True)  # Field name made lowercase.
    worktype = models.CharField(db_column='WorkType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimeEntries'
        unique_together = (('oid', 'ticketid'),)


class Worktypes(models.Model):
    oid = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    worktype = models.CharField(db_column='WorkType', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkTypes'

