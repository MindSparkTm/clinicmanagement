import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import models
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


def create_models(**kwargs):
    defaults = {}
    defaults["patient_id"] = "patient_id"
    defaults["first_name"] = "first_name"
    defaults["middle_name"] = "middle_name"
    defaults["last_name"] = "last_name"
    defaults["Gender"] = "Gender"
    defaults["street_name"] = "street_name"
    defaults["apartment_name"] = "apartment_name"
    defaults["postal_code"] = "postal_code"
    defaults["postal_address"] = "postal_address"
    defaults["city"] = "city"
    defaults["country"] = "country"
    defaults["age"] = "age"
    defaults["next_of_kin"] = "next_of_kin"
    defaults["n_of_kin_rel"] = "n_of_kin_rel"
    defaults["email"] = "email"
    defaults["phone"] = "phone"
    defaults["primary_insurance"] = "primary_insurance"
    defaults["secondary_insurance"] = "secondary_insurance"
    defaults["pri_ins_sub"] = "pri_ins_sub"
    defaults["sec_ins_sub"] = "sec_ins_sub"
    defaults["other_ins_subscriber"] = "other_ins_subscriber"
    defaults["subscriber_relationship"] = "subscriber_relationship"
    defaults["sub_address"] = "sub_address"
    defaults["ss_number"] = "ss_number"
    defaults["sub_ss_number"] = "sub_ss_number"
    defaults["alt_phone"] = "alt_phone"
    defaults["sub_work_phone"] = "sub_work_phone"
    defaults["dob"] = "dob"
    defaults["sub_dob"] = "sub_dob"
    defaults["sub_employer"] = "sub_employer"
    defaults.update(**kwargs)
    return models.objects.create(**defaults)


class modelsViewTest(unittest.TestCase):
    '''
    Tests for models
    '''
    def setUp(self):
        self.client = Client()

    def test_list_models(self):
        url = reverse('registration_models_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_models(self):
        url = reverse('registration_models_create')
        data = {
            "patient_id": "patient_id",
            "first_name": "first_name",
            "middle_name": "middle_name",
            "last_name": "last_name",
            "Gender": "Gender",
            "street_name": "street_name",
            "apartment_name": "apartment_name",
            "postal_code": "postal_code",
            "postal_address": "postal_address",
            "city": "city",
            "country": "country",
            "age": "age",
            "next_of_kin": "next_of_kin",
            "n_of_kin_rel": "n_of_kin_rel",
            "email": "email",
            "phone": "phone",
            "primary_insurance": "primary_insurance",
            "secondary_insurance": "secondary_insurance",
            "pri_ins_sub": "pri_ins_sub",
            "sec_ins_sub": "sec_ins_sub",
            "other_ins_subscriber": "other_ins_subscriber",
            "subscriber_relationship": "subscriber_relationship",
            "sub_address": "sub_address",
            "ss_number": "ss_number",
            "sub_ss_number": "sub_ss_number",
            "alt_phone": "alt_phone",
            "sub_work_phone": "sub_work_phone",
            "dob": "dob",
            "sub_dob": "sub_dob",
            "sub_employer": "sub_employer",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_models(self):
        models = create_models()
        url = reverse('registration_models_detail', args=[models.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_models(self):
        models = create_models()
        data = {
            "patient_id": "patient_id",
            "first_name": "first_name",
            "middle_name": "middle_name",
            "last_name": "last_name",
            "Gender": "Gender",
            "street_name": "street_name",
            "apartment_name": "apartment_name",
            "postal_code": "postal_code",
            "postal_address": "postal_address",
            "city": "city",
            "country": "country",
            "age": "age",
            "next_of_kin": "next_of_kin",
            "n_of_kin_rel": "n_of_kin_rel",
            "email": "email",
            "phone": "phone",
            "primary_insurance": "primary_insurance",
            "secondary_insurance": "secondary_insurance",
            "pri_ins_sub": "pri_ins_sub",
            "sec_ins_sub": "sec_ins_sub",
            "other_ins_subscriber": "other_ins_subscriber",
            "subscriber_relationship": "subscriber_relationship",
            "sub_address": "sub_address",
            "ss_number": "ss_number",
            "sub_ss_number": "sub_ss_number",
            "alt_phone": "alt_phone",
            "sub_work_phone": "sub_work_phone",
            "dob": "dob",
            "sub_dob": "sub_dob",
            "sub_employer": "sub_employer",
        }
        url = reverse('registration_models_update', args=[models.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


