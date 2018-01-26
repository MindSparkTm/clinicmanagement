import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import pre_auth
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


def create_pre_auth(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["reference_no"] = "reference_no"
    defaults["authority_type"] = "authority_type"
    defaults["provider"] = "provider"
    defaults["ward"] = "ward"
    defaults["date_admitted"] = "date_admitted"
    defaults["date_provided"] = "date_provided"
    defaults["notes"] = "notes"
    defaults["claim"] = "claim"
    defaults["limit"] = "limit"
    defaults["batch_no"] = "batch_no"
    defaults["date_reported"] = "date_reported"
    defaults["admit_days"] = "admit_days"
    defaults["anniv"] = "anniv"
    defaults["daily_bed_limit"] = "daily_bed_limit"
    defaults["type"] = "type"
    defaults["authorised_by"] = "authorised_by"
    defaults.update(**kwargs)
    return pre_auth.objects.create(**defaults)


class pre_authViewTest(unittest.TestCase):
    '''
    Tests for pre_auth
    '''
    def setUp(self):
        self.client = Client()

    def test_list_pre_auth(self):
        url = reverse('pre_auth_pre_auth_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pre_auth(self):
        url = reverse('pre_auth_pre_auth_create')
        data = {
            "name": "name",
            "reference_no": "reference_no",
            "authority_type": "authority_type",
            "provider": "provider",
            "ward": "ward",
            "date_admitted": "date_admitted",
            "date_provided": "date_provided",
            "notes": "notes",
            "claim": "claim",
            "limit": "limit",
            "batch_no": "batch_no",
            "date_reported": "date_reported",
            "admit_days": "admit_days",
            "anniv": "anniv",
            "daily_bed_limit": "daily_bed_limit",
            "type": "type",
            "authorised_by": "authorised_by",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pre_auth(self):
        pre_auth = create_pre_auth()
        url = reverse('pre_auth_pre_auth_detail', args=[pre_auth.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pre_auth(self):
        pre_auth = create_pre_auth()
        data = {
            "name": "name",
            "reference_no": "reference_no",
            "authority_type": "authority_type",
            "provider": "provider",
            "ward": "ward",
            "date_admitted": "date_admitted",
            "date_provided": "date_provided",
            "notes": "notes",
            "claim": "claim",
            "limit": "limit",
            "batch_no": "batch_no",
            "date_reported": "date_reported",
            "admit_days": "admit_days",
            "anniv": "anniv",
            "daily_bed_limit": "daily_bed_limit",
            "type": "type",
            "authorised_by": "authorised_by",
        }
        url = reverse('pre_auth_pre_auth_update', args=[pre_auth.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


