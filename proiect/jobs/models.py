from django.db import models

# Create your models here.


class Job(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    description = models.TextField()
    customer = models.ForeignKey('app2.Companies', on_delete=models.CASCADE)
    active = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} {self.description}"


# sa se realizeze Create, Read, Update, Delete (CRUD) pentru modulul de jobs.
# trebuie sa avem o validare in care sa nu existe job cu nume si customer identic
