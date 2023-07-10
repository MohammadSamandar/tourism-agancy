from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactUsModelForm
from .models import ContactUs, UserProfile
from django.views import View
from django.views.generic.edit import FormView, CreateView
from django.contrib import messages
from site_module.models import SiteSetting


# Create your views here.

class contact_us_view(CreateView):
    form_class = ContactUsModelForm
    template_name = 'contact_us/contact.html'
    success_url = '/contact-us/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'پیام با موفقیت ارسال شد')
        return super().form_valid(form)



