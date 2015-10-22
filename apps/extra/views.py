from django.conf import settings
from django.shortcuts import render_to_response
from django.contrib import messages
from django.template import RequestContext
from forms import ContactForm


def contact_us(request):
    """
    """
    context = {'form': ContactForm()}

    if request.POST:
        form = ContactForm(request.POST)
        context.update({'form': form})
        if form.is_valid():
            form.send_mail()
            messages.info(request, 'Your email was sent successfully, thanks for contacting us.')

    return render_to_response('contact.html', context, RequestContext(request))