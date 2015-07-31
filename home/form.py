from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(widget=forms.TextInput(attrs={'id':'subject', 'class':'form-control', 'name':'subject', 'placeholder':'Subject'}))
	sender = forms.EmailField(widget=forms.TextInput(attrs={'id':'email', 'name':'email', 'placeholder':'Email Address', 'class':'form-control'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'id':'message', 'name':'message', 'placeholder':'Enter your message for use here. I will get back to you as soon as possible', 'rows':'7'}))

# first_name = forms.CharField(max_length=100, 
# 		widget=forms.TextInput(attrs={'placeholder':'First name', 'id':'fname', 'class':'form-control', 'name':'name'}))

# 	last_name = forms.CharField(max_length=100,
# 		widget=forms.TextInput(attrs={'placeholder':'Last name', 'id':'lname', 'class':'form-control', 'name':'name'}))