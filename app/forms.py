from django import forms

class CalendarForm(forms.Form):
    title = forms.CharField(max_length=100, label='タイトル')

class ChoiceForm(forms.Form):
    check = forms.BooleanField(label='チェックボックス', required=False)

"""
#ここから選択肢　https://arakan-pgm-ai.hatenablog.com/entry/2019/02/18/090000

class CheckboxForm(forms.Form):
    CHOICE = [
        ('1','選択肢＜１＞'),
        ('2','選択肢＜２＞'),
        ('3','選択肢＜３＞'),
        ]
     
    two = forms.MultipleChoiceField(
        label=labels[1],
        required=False,
        disabled=False,
        initial=[],
        choices=CHOICE,
        widget=forms.CheckboxSelectMultiple(attrs={
            'id': 'two','class': 'form-check-input'})) 

"""
