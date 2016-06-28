from django import forms
from .models import Estimate

class RequestForm(forms.ModelForm):

    class Meta:
        model = Estimate
        fields = ('salary', 'age', 'summ', 'time', 'experience', 'history', 'current', 'outstanding',)
		
		
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
	
