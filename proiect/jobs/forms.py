from django import forms

from jobs.models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['name', 'url', 'description', 'customer']

    def __init__(self, pk, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        cleaned_data = self.cleaned_data
        name_value = cleaned_data.get('name')
        customer_value = cleaned_data.get('customer')
        if self.pk:
            if Job.objects.filter(name=name_value, customer=customer_value, active=1).exclude(id=self.pk).exists():
                self._errors['name'] = self.error_class(["Jobul exista deja la aceasta companie!"])
        else:
            if Job.objects.filter(name=name_value, customer=customer_value, active=1).exists():
                self._errors['name'] = self.error_class(["Jobul exista deja la aceasta companie!"])
        return cleaned_data


