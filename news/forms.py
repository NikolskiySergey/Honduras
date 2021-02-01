from django import forms
from django.core.exceptions import ValidationError

class StartForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    hondurasian = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}),
                                    choices=(('native', 'Native'), ('neighbor', 'Neighbor'), ('gringo', 'Gringo'),))
    like_country_No_doubt = forms.NullBooleanField()
    love_Fun = forms.NullBooleanField()

