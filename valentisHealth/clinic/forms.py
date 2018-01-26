from django import forms
from .models import models


class modelsForm(forms.ModelForm):
    class Meta:
        model = models
        fields = ['lab_name', 'h01', 'h02', 'h03', 'h04', 'h05', 'h06', 'h07', 'h08', 'h09', 'c01', 'c02', 'p01', 'p02', 'p03', 'p04', 'p05', 'p06', 'mbs01', 'mbs02', 'mbs03', 'ge01', 'lks01', 'lks02', 'lks03', 'lks04', 'lks05', 'lks06', 'lks07', 'gm01', 'gm02', 'gm03', 'lm01', 'lm02', 'lm03', 'lm04', 'lpg01', 'lpg02', 'lpg03', 'lpg04', 'lpg05', 'lpg06', 'lpg06', 'lpg07', 'lpg08', 'hv01', 'hv02', 'hv03', 'i01', 'i02', 'i03', 'm01', 'm02', 'm03', 'M04', 'm05', 'm06', 'm07', 'm08', 'g01', 'other', 'diagnosis', 'h01_alergy', 'h02_alergy', 'h03_alergy', 'h04_alergy', 'h06_alergy', 'h07_alergy', 'h08_alergy', 'c01_iron_studies', 'c01_cardiac_markers', 'c02_cardiac_markers', 'c02_cardiac_markers_1', 'lks01_antenatal_screen', 'lks02_antenatal_screen', 'lks04_antenatal_screen', 'lks05_antenatal_screen', 'lks06_antenatal_screen', 'lks07_antenatal_screen', 'gm01_antenatal_screen', 'fsh_menopausal_screen', 'oestradiol_menopausal_screen', 'albumin_menopausal_screen', 'hv02_menopausal_screen', 'hv03_menopausal_screen', 'ast_menopausal_screen', 'i01_menopausal_screen', 'i02_menopausal_screen', 'i03_menopausal_screen']


