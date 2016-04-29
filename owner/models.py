from __future__ import unicode_literals

from django.db import models
from accounts.models import User as CustomUser
import uuid

class Institution(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True)
    address = models.CharField(max_length=255, default=None, blank=True, null=True)
    country = models.CharField(max_length=255, default=None, blank=True, null=True)
    department = models.CharField(max_length=255, default=None, blank=True, null=True)

    def __unicode__(self):
        return str(self.name)

    def as_json(self):
        return {
            "uuid": self.id,
            "name": self.name,
            "address": self.address,
            "country": self.country,
            "department": self.department
        }

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = None
        if not self.address:
            self.address = None
        if not self.country:
            self.country = None
        if not self.department:
            self.department = None
        super(Institution, self).save(*args, **kwargs)

class ServiceOwner(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, default=None, blank=True)
    last_name = models.CharField(max_length=255, default=None, blank=True)
    email = models.EmailField(default=None, blank=True)
    phone = models.CharField(max_length=255, default=None, blank=True, null=True)
    id_service_owner = models.ForeignKey(Institution)

    id_account = models.ForeignKey(CustomUser, null=True, blank=True, default = None)

    def __unicode__(self):
        return str(self.first_name) + " " + str(self.last_name)

    def get_institution(self):
        return Institution.objects.get(id=self.id_service_owner.pk).as_json()


    def save(self, *args, **kwargs):
        if not self.phone:
            self.phone = None
        if not self.first_name:
            self.first_name = None
        if not self.last_name:
            self.last_name = None
        if not self.email:
            self.email = None
        super(ServiceOwner, self).save(*args, **kwargs)

    def as_json(self):
        return {
            "uuid": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "institution": self.id_service_owner.as_json(),
            "account_id": self.id_account_id
        }

class ContactInformation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, default=None, blank=True)
    last_name = models.CharField(max_length=255, default=None, blank=True)
    email = models.EmailField(default=None, blank=True)
    phone = models.CharField(max_length=255, default=None, blank=True, null=True)
    url = models.CharField(max_length=255, default=None, blank=True, null=True)

    def __unicode__(self):
        return str(self.first_name) + " " + str(self.last_name)


    def save(self, *args, **kwargs):
        if not self.phone:
            self.phone = None
        if not self.first_name:
            self.first_name = None
        if not self.last_name:
            self.last_name = None
        if not self.email:
            self.email = None
        if not self.url:
            self.url = None
        super(ContactInformation, self).save(*args, **kwargs)

    def as_json(self):
        return {
            "uuid": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone
        }

class Internal(models.Model):

    id_contact_info = models.ForeignKey(ContactInformation)

    def __unicode__(self):
        cont_info = ContactInformation.objects.get(pk=self.id_contact_info.pk)
        return str(cont_info)

class External(models.Model):

    id_contact_info = models.ForeignKey(ContactInformation)

    def __unicode__(self):
        cont_info = ContactInformation.objects.get(pk=self.id_contact_info.pk)
        return str(cont_info)