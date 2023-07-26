from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm


def contact_view(request):
    """
    A function to render contact page,
    provide contact form
    """
    if request.user.is_authenticated:
        email = request.user.email
        contact_form = ContactForm(initial={'email': email})
        if request.method == 'POST':
            contact_form = ContactForm(data=request.POST)

            if contact_form.is_valid():
                contact = contact_form.save(commit=False)
                contact.save()

                return render(request, 'contact/thank_you.html')
    else:
        contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form
    }
    return render(request, template, context)