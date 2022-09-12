from django import forms
from accounts.models import Rate

class rateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['assignmentsRating', 'attendanceRating', 'clarityRating','timingRating']