from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from jobs.forms import JobForm
from jobs.models import Job


class CreateJobView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_form.html'

    def get_form_kwargs(self):
        data = super(CreateJobView, self).get_form_kwargs()
        data.update({'pk': None})
        return data

    def get_success_url(self):
        return reverse('jobs:list')


class ListJobView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'jobs/job_index.html'

    def get_queryset(self):
        return Job.objects.filter(active=1)


class UpdateJobView(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_form.html'

    def get_form_kwargs(self):
        data = super(UpdateJobView, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})
        return data

    def get_success_url(self):
        return reverse('jobs:list')


@login_required
def delete_job(request, pk):
    if request.user.is_authenticated:
        Job.objects.filter(id=pk).update(active=0)
    return redirect('jobs:list')
