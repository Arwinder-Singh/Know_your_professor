from django import forms
from accounts.models import Rate

class rateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['getreadytodoworkRating', 'skipclassyouwillnotpassRating', 'clarityRating','timelyteacherRating','ControlfreakRating','ToughGraderRating','BewareofquestioningRating','LectureheavyRating','NotesprovidedRating','ExtraactivitiesRating']