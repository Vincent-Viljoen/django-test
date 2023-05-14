from django import forms

# class ClientsForm(forms.Form):
#   firstname = forms.CharField(max_length=255)
#   email = forms.EmailField(max_length=254)
#   message = forms.TextField()
#   med_aid = forms.CharField(max_length=255)
#   med_aid_num = forms.IntegerField()

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)