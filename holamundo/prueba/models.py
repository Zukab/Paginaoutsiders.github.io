from django.db import models
from django.utils.translation import ungettext_lazy

class Contact(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)
    email = models.EmailField(blank=False,null=False)
    phone = models.CharField( max_length=225, null=False, blank=False)
    message = models.CharField(max_length=225, null=False, blank=False)
    def __str__(self) -> str:
        return self.name+" "+self.email