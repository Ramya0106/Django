from django.db import models
# from django.forms import ModelForm

# Create your models here.
from django.utils import timezone

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    #rollno = models.

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)