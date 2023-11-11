from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Contact
from .contact_form import ContactForm

#listing of all contacts
class ContactListView(ListView):
    model = Contact

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm

    #returns to homepage when contact is created successfully
    success_url = reverse_lazy('contact_list')
