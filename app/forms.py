from django import forms

class CalendarForm(forms.Form):
    title = forms.CharField(max_length=100, label='タイトル')