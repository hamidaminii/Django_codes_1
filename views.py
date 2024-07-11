from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, FormView

from.forms import ContactUsForm,ContactUsModelForm
from .models import ContactUs


class ContactUsView(FormView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


