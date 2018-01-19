from django import forms

class ControlsForm(forms.Form):
    vacation_mode = forms.ChoiceField(("On", "Off"))