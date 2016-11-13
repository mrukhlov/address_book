from django import forms
from django.contrib.auth import authenticate
from django.forms import ModelForm
from models import bookEntryModel

class LoginForm(forms.Form):
	username = forms.CharField(label=u'Username', max_length=1000, required=True)
	password = forms.CharField(label=u'Password', max_length=1000, required=True, widget=forms.PasswordInput())

	def clean(self):
		cleaned_data = super(LoginForm, self).clean()
		if not self.errors:
			user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
			self.user = user
		return cleaned_data

	def get_user(self):
		return self.user or None

class bookEntryForm(ModelForm):
	class Meta:
		model = bookEntryModel
		fields = ('name', 'phone', 'address', 'birth_date', 'email')