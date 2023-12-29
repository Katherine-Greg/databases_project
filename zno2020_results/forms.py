from django import forms

from zno2020_results.models import Student, Institution, Location, StudentResults


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class ResultCreationForm(forms.ModelForm):
    class Meta:
        model = StudentResults
        fields = "__all__"


class LocationCreationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"


class InstitutionCreationForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = "__all__"
