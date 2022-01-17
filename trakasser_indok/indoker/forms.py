from django import forms
from . import models
import re

class CreateIndoker(forms.ModelForm):
    class Meta:
        model = models.Indoker
        fields = ['fornavn', 'etternavn', 'profile_pic', 'facebooklink']

    def clean_facebooklink(self):
        facebooklink = self.cleaned_data.get("facebooklink")
        print(facebooklink)
        print("https" in facebooklink)
        if "https" in facebooklink:
            facebooklink = re.sub(r'^.*?f', 'f', facebooklink)
            return facebooklink
        else:
            return facebooklink