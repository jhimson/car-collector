from django.forms import ModelForm
from .models import Racing


class RacingForm(ModelForm):
    class Meta:
        model = Racing
        fields = ['date', 'location']
