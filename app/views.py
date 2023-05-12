from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from gallery.models import category, snippet
from .models import feedback, Contact
from .forms import feedbackForm, ContactForm

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def payment(request):
    return render(request, 'payment.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Feedback Submitted Successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

@login_required
def feedback(request):
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Feedback Submitted Successfully!')
            return redirect('feedback')
    else:
        form = feedbackForm()
    return render(request, 'feedback.html', {'form': form})