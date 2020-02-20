from NJnaiduapp.models import *

from django.forms import ModelForm

class ChairmanForm(ModelForm):
    class Meta:
        model = Chairman
        fields = '__all__'