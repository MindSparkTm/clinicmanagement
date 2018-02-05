import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import patientVisit
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_patientvisit(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["patient_no"] = "patient_no"
    defaults["visit_id"] = "visit_id"
    defaults["radiology_no"] = "radiology_no"
    defaults["notes"] = "notes"
    defaults["diagnosis"] = "diagnosis"
    defaults["prescription_id"] = "prescription_id"
    defaults["status"] = "status"
    defaults.update(**kwargs)
    return patientVisit.objects.create(**defaults)


class patientVisitViewTest(unittest.TestCase):
    '''
    Tests for patientVisit
    '''
    def setUp(self):
        self.client = Client()

    def test_list_patientvisit(self):
        url = reverse('clinic_patientvisit_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_patientvisit(self):
        url = reverse('clinic_patientvisit_create')
        data = {
            "name": "name",
            "patient_no": "patient_no",
            "visit_id": "visit_id",
            "radiology_no": "radiology_no",
            "notes": "notes",
            "diagnosis": "diagnosis",
            "prescription_id": "prescription_id",
            "status": "status",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_patientvisit(self):
        patientvisit = create_patientvisit()
        url = reverse('clinic_patientvisit_detail', args=[patientvisit.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_patientvisit(self):
        patientvisit = create_patientvisit()
        data = {
            "name": "name",
            "patient_no": "patient_no",
            "visit_id": "visit_id",
            "radiology_no": "radiology_no",
            "notes": "notes",
            "diagnosis": "diagnosis",
            "prescription_id": "prescription_id",
            "status": "status",
        }
        url = reverse('clinic_patientvisit_update', args=[patientvisit.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


