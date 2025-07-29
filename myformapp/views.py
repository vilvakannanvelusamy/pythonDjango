from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
import logging

def index(request):
    return HttpResponse("Index Page")

def contact(request):
    logger = logging.getLogger("testing")

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            logger.debug(f"Post data is {cleaned['name']}, {cleaned['email']}, {cleaned['message']}")
            success_message = 'Your Email has been sent!'
            return render(request, "contact.html", {
                'form': ContactForm(),  # Reset form after success
                'success_message': success_message
            })
        else:
            logger.debug("Form validation failed")
            return render(request, "contact.html", {'form': form})
    
    else:
        form = ContactForm()
        return render(request, "contact.html", {'form': form})
