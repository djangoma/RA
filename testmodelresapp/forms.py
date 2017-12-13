from django import forms
from .models import JournalArticle, ConferenceArticle, Project
from django.forms import ModelForm

class JournalNewForm(forms.ModelForm):
    '''message = forms.CharField(widget=forms.Textarea(), max_length=100)'''

    class Meta:
        model = JournalArticle
        fields = '__all__'
	
class JournalUpdateForm(forms.ModelForm):
	class Meta:
		model = JournalArticle
		fields = '__all__'

class ConferenceNewForm(forms.ModelForm):
    '''message = forms.CharField(widget=forms.Textarea(), max_length=100)'''

    class Meta:
        model = ConferenceArticle
        fields = '__all__'
	
class ConferenceUpdateForm(forms.ModelForm):
	class Meta:
		model = ConferenceArticle
		fields = '__all__'
		
class ProjectNewForm(forms.ModelForm):
    '''message = forms.CharField(widget=forms.Textarea(), max_length=100)'''

    class Meta:
        model = Project
        fields = '__all__'
	
class ProjectUpdateForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = '__all__'