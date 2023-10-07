""" Imports from django and contact form. """
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ContactForm
from .models import TeamMember


def ContactMessage(request):
    """
    View to display contact us form.

    If the form is valid, save, display a
    success message and return the contact us form.
    If invalid, display error message.
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thank you for your enquiry,\
                we will get back to soon!')

            return redirect('contact')
        else:
            messages.error(request,
                           'Something went wrong, please check the form')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def team_member_list(request):
    team_members = TeamMember.objects.all()
    return render(request, 'team/member_list.html', {'team_members': team_members})


def team_member_detail(request, pk):
    team_member = get_object_or_404(TeamMember, pk=pk)
    return render(request, 'team/member_detail.html', {'team_member': team_member})
