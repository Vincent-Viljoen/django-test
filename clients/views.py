from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# from .forms import ClientsForm
# from .views import Clients

def home_screen_view(request):
    print(request.headers)
    return render(request, "clients/home.html", {})

# def clients(request):

#     if request.method == 'POST':
#         form = ClientsForm(request.POST)
#         if form.is_valid():
#             # Save the form data to the database
#             client = Clients(firstname=form.cleaned_data['firstname'],
#                               email=form.cleaned_data['email'],
#                               message=form.cleaned_data['message'],
#                               med_aid=form.cleaned_data['med_aid'],
#                               med_aid_num=form.cleaned_data['med_aid_num'])

#             client.save()
#             # Redirect to a success page
#             return render(request, 'contact_success.html')
#     else:
#         form = ClientsForm()


#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())

from .models import Contact
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request, 'clients/contact_success.html')

def fail(request):
    return render(request, 'clients/contact_fail.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact = Contact(name=form.cleaned_data['name'],
                              email=form.cleaned_data['email'],
                              message=form.cleaned_data['message'])
            contact.save()
            # Redirect to a success page
            return redirect('success')
        else:
            return redirect('fail')
    else:
        form = ContactForm()
    return render(request, 'clients/contact.html', {'form': form})