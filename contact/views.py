from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # Saves to DB immediately because it's a ModelForm
            messages.success(request, f"Thank you! Your message has been sent.")
            # Redirect to home page at the contact anchor
            return redirect('/#contact')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
