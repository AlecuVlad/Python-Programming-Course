from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.

# CreateView -> adaugare date in DB
# UpdateView -> modificare date in formular
# DeleteView -> stergere date din DB
# IndexView -> informare cu privire la formular
# ListView -> informatii de tip lista din DB
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView

from app1.models import Location


class CreateLocationView(LoginRequiredMixin, CreateView):
    model = Location
    # fields = '__all__'
    fields = ['city', 'country']
    template_name = 'app1/location_form.html'

    def get_success_url(self):
        return reverse('app1:listare')


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Location
    # fields = '__all__'
    fields = ['city', 'country']
    template_name = 'app1/location_form.html'

    def get_success_url(self):
        return reverse('app1:listare')


class ListLocationView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'app1/location_index.html'
