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
    defaults["lab_name"] = "lab_name"
    defaults["h01"] = "h01"
    defaults["h02"] = "h02"
    defaults["h03"] = "h03"
    defaults["h04"] = "h04"
    defaults["h05"] = "h05"
    defaults["h06"] = "h06"
    defaults["h07"] = "h07"
    defaults["h08"] = "h08"
    defaults["h09"] = "h09"
    defaults["c01"] = "c01"
    defaults["c02"] = "c02"
    defaults["p01"] = "p01"
    defaults["p02"] = "p02"
    defaults["p03"] = "p03"
    defaults["p04"] = "p04"
    defaults["p05"] = "p05"
    defaults["p06"] = "p06"
    defaults["mbs01"] = "mbs01"
    defaults["mbs02"] = "mbs02"
    defaults["mbs03"] = "mbs03"
    defaults["ge01"] = "ge01"
    defaults["lks01"] = "lks01"
    defaults["lks02"] = "lks02"
    defaults["lks03"] = "lks03"
    defaults["lks04"] = "lks04"
    defaults["lks05"] = "lks05"
    defaults["lks06"] = "lks06"
    defaults["lks07"] = "lks07"
    defaults["gm01"] = "gm01"
    defaults["gm02"] = "gm02"
    defaults["gm03"] = "gm03"
    defaults["lm01"] = "lm01"
    defaults["lm02"] = "lm02"
    defaults["lm03"] = "lm03"
    defaults["lm04"] = "lm04"
    defaults["lpg01"] = "lpg01"
    defaults["lpg02"] = "lpg02"
    defaults["lpg03"] = "lpg03"
    defaults["lpg04"] = "lpg04"
    defaults["lpg05"] = "lpg05"
    defaults["lpg06"] = "lpg06"
    defaults["lpg06"] = "lpg06"
    defaults["lpg07"] = "lpg07"
    defaults["lpg08"] = "lpg08"
    defaults["hv01"] = "hv01"
    defaults["hv02"] = "hv02"
    defaults["hv03"] = "hv03"
    defaults["i01"] = "i01"
    defaults["i02"] = "i02"
    defaults["i03"] = "i03"
    defaults["m01"] = "m01"
    defaults["m02"] = "m02"
    defaults["m03"] = "m03"
    defaults["M04"] = "M04"
    defaults["m05"] = "m05"
    defaults["m06"] = "m06"
    defaults["m07"] = "m07"
    defaults["m08"] = "m08"
    defaults["g01"] = "g01"
    defaults["other"] = "other"
    defaults["diagnosis"] = "diagnosis"
    defaults["h01_alergy"] = "h01_alergy"
    defaults["h02_alergy"] = "h02_alergy"
    defaults["h03_alergy"] = "h03_alergy"
    defaults["h04_alergy"] = "h04_alergy"
    defaults["h06_alergy"] = "h06_alergy"
    defaults["h07_alergy"] = "h07_alergy"
    defaults["h08_alergy"] = "h08_alergy"
    defaults["c01_iron_studies"] = "c01_iron_studies"
    defaults["c01_cardiac_markers"] = "c01_cardiac_markers"
    defaults["c02_cardiac_markers"] = "c02_cardiac_markers"
    defaults["c02_cardiac_markers_1"] = "c02_cardiac_markers_1"
    defaults["lks01_antenatal_screen"] = "lks01_antenatal_screen"
    defaults["lks02_antenatal_screen"] = "lks02_antenatal_screen"
    defaults["lks04_antenatal_screen"] = "lks04_antenatal_screen"
    defaults["lks05_antenatal_screen"] = "lks05_antenatal_screen"
    defaults["lks06_antenatal_screen"] = "lks06_antenatal_screen"
    defaults["lks07_antenatal_screen"] = "lks07_antenatal_screen"
    defaults["gm01_antenatal_screen"] = "gm01_antenatal_screen"
    defaults["fsh_menopausal_screen"] = "fsh_menopausal_screen"
    defaults["oestradiol_menopausal_screen"] = "oestradiol_menopausal_screen"
    defaults["albumin_menopausal_screen"] = "albumin_menopausal_screen"
    defaults["hv02_menopausal_screen"] = "hv02_menopausal_screen"
    defaults["hv03_menopausal_screen"] = "hv03_menopausal_screen"
    defaults["ast_menopausal_screen"] = "ast_menopausal_screen"
    defaults["i01_menopausal_screen"] = "i01_menopausal_screen"
    defaults["i02_menopausal_screen"] = "i02_menopausal_screen"
    defaults["i03_menopausal_screen"] = "i03_menopausal_screen"
    defaults.update(**kwargs)
    return models.objects.create(**defaults)


class modelsViewTest(unittest.TestCase):
    '''
    Tests for models
    '''
    def setUp(self):
        self.client = Client()

    def test_list_models(self):
        url = reverse('clinic_models_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_models(self):
        url = reverse('clinic_models_create')
        data = {
            "lab_name": "lab_name",
            "h01": "h01",
            "h02": "h02",
            "h03": "h03",
            "h04": "h04",
            "h05": "h05",
            "h06": "h06",
            "h07": "h07",
            "h08": "h08",
            "h09": "h09",
            "c01": "c01",
            "c02": "c02",
            "p01": "p01",
            "p02": "p02",
            "p03": "p03",
            "p04": "p04",
            "p05": "p05",
            "p06": "p06",
            "mbs01": "mbs01",
            "mbs02": "mbs02",
            "mbs03": "mbs03",
            "ge01": "ge01",
            "lks01": "lks01",
            "lks02": "lks02",
            "lks03": "lks03",
            "lks04": "lks04",
            "lks05": "lks05",
            "lks06": "lks06",
            "lks07": "lks07",
            "gm01": "gm01",
            "gm02": "gm02",
            "gm03": "gm03",
            "lm01": "lm01",
            "lm02": "lm02",
            "lm03": "lm03",
            "lm04": "lm04",
            "lpg01": "lpg01",
            "lpg02": "lpg02",
            "lpg03": "lpg03",
            "lpg04": "lpg04",
            "lpg05": "lpg05",
            "lpg06": "lpg06",
            "lpg06": "lpg06",
            "lpg07": "lpg07",
            "lpg08": "lpg08",
            "hv01": "hv01",
            "hv02": "hv02",
            "hv03": "hv03",
            "i01": "i01",
            "i02": "i02",
            "i03": "i03",
            "m01": "m01",
            "m02": "m02",
            "m03": "m03",
            "M04": "M04",
            "m05": "m05",
            "m06": "m06",
            "m07": "m07",
            "m08": "m08",
            "g01": "g01",
            "other": "other",
            "diagnosis": "diagnosis",
            "h01_alergy": "h01_alergy",
            "h02_alergy": "h02_alergy",
            "h03_alergy": "h03_alergy",
            "h04_alergy": "h04_alergy",
            "h06_alergy": "h06_alergy",
            "h07_alergy": "h07_alergy",
            "h08_alergy": "h08_alergy",
            "c01_iron_studies": "c01_iron_studies",
            "c01_cardiac_markers": "c01_cardiac_markers",
            "c02_cardiac_markers": "c02_cardiac_markers",
            "c02_cardiac_markers_1": "c02_cardiac_markers_1",
            "lks01_antenatal_screen": "lks01_antenatal_screen",
            "lks02_antenatal_screen": "lks02_antenatal_screen",
            "lks04_antenatal_screen": "lks04_antenatal_screen",
            "lks05_antenatal_screen": "lks05_antenatal_screen",
            "lks06_antenatal_screen": "lks06_antenatal_screen",
            "lks07_antenatal_screen": "lks07_antenatal_screen",
            "gm01_antenatal_screen": "gm01_antenatal_screen",
            "fsh_menopausal_screen": "fsh_menopausal_screen",
            "oestradiol_menopausal_screen": "oestradiol_menopausal_screen",
            "albumin_menopausal_screen": "albumin_menopausal_screen",
            "hv02_menopausal_screen": "hv02_menopausal_screen",
            "hv03_menopausal_screen": "hv03_menopausal_screen",
            "ast_menopausal_screen": "ast_menopausal_screen",
            "i01_menopausal_screen": "i01_menopausal_screen",
            "i02_menopausal_screen": "i02_menopausal_screen",
            "i03_menopausal_screen": "i03_menopausal_screen",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_models(self):
        models = create_models()
        url = reverse('clinic_models_detail', args=[models.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_models(self):
        models = create_models()
        data = {
            "lab_name": "lab_name",
            "h01": "h01",
            "h02": "h02",
            "h03": "h03",
            "h04": "h04",
            "h05": "h05",
            "h06": "h06",
            "h07": "h07",
            "h08": "h08",
            "h09": "h09",
            "c01": "c01",
            "c02": "c02",
            "p01": "p01",
            "p02": "p02",
            "p03": "p03",
            "p04": "p04",
            "p05": "p05",
            "p06": "p06",
            "mbs01": "mbs01",
            "mbs02": "mbs02",
            "mbs03": "mbs03",
            "ge01": "ge01",
            "lks01": "lks01",
            "lks02": "lks02",
            "lks03": "lks03",
            "lks04": "lks04",
            "lks05": "lks05",
            "lks06": "lks06",
            "lks07": "lks07",
            "gm01": "gm01",
            "gm02": "gm02",
            "gm03": "gm03",
            "lm01": "lm01",
            "lm02": "lm02",
            "lm03": "lm03",
            "lm04": "lm04",
            "lpg01": "lpg01",
            "lpg02": "lpg02",
            "lpg03": "lpg03",
            "lpg04": "lpg04",
            "lpg05": "lpg05",
            "lpg06": "lpg06",
            "lpg06": "lpg06",
            "lpg07": "lpg07",
            "lpg08": "lpg08",
            "hv01": "hv01",
            "hv02": "hv02",
            "hv03": "hv03",
            "i01": "i01",
            "i02": "i02",
            "i03": "i03",
            "m01": "m01",
            "m02": "m02",
            "m03": "m03",
            "M04": "M04",
            "m05": "m05",
            "m06": "m06",
            "m07": "m07",
            "m08": "m08",
            "g01": "g01",
            "other": "other",
            "diagnosis": "diagnosis",
            "h01_alergy": "h01_alergy",
            "h02_alergy": "h02_alergy",
            "h03_alergy": "h03_alergy",
            "h04_alergy": "h04_alergy",
            "h06_alergy": "h06_alergy",
            "h07_alergy": "h07_alergy",
            "h08_alergy": "h08_alergy",
            "c01_iron_studies": "c01_iron_studies",
            "c01_cardiac_markers": "c01_cardiac_markers",
            "c02_cardiac_markers": "c02_cardiac_markers",
            "c02_cardiac_markers_1": "c02_cardiac_markers_1",
            "lks01_antenatal_screen": "lks01_antenatal_screen",
            "lks02_antenatal_screen": "lks02_antenatal_screen",
            "lks04_antenatal_screen": "lks04_antenatal_screen",
            "lks05_antenatal_screen": "lks05_antenatal_screen",
            "lks06_antenatal_screen": "lks06_antenatal_screen",
            "lks07_antenatal_screen": "lks07_antenatal_screen",
            "gm01_antenatal_screen": "gm01_antenatal_screen",
            "fsh_menopausal_screen": "fsh_menopausal_screen",
            "oestradiol_menopausal_screen": "oestradiol_menopausal_screen",
            "albumin_menopausal_screen": "albumin_menopausal_screen",
            "hv02_menopausal_screen": "hv02_menopausal_screen",
            "hv03_menopausal_screen": "hv03_menopausal_screen",
            "ast_menopausal_screen": "ast_menopausal_screen",
            "i01_menopausal_screen": "i01_menopausal_screen",
            "i02_menopausal_screen": "i02_menopausal_screen",
            "i03_menopausal_screen": "i03_menopausal_screen",
        }
        url = reverse('clinic_models_update', args=[models.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


