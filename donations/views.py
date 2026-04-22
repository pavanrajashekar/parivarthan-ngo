from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Donation
from .forms import DonationForm
import uuid

def initiate_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.status = 'Pending'
            # In a real Razorpay flow, we'd ping the Razorpay API here to get an Order ID
            donation.payment_id = str(uuid.uuid4())[:8] # Fake ID
            donation.save()
            return redirect('mock-gateway', donation_id=donation.id)
    else:
        form = DonationForm()
    
    return render(request, 'donations/donate.html', {'form': form})

def mock_gateway(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id)
    
    if request.method == 'POST':
        # Simulate successful payment
        donation.status = 'Success'
        donation.save()
        messages.success(request, f"Thank you {donation.donor_name}! Your donation of ₹{donation.amount} was successful.")
        return redirect('initiate-donation')
        
    return render(request, 'donations/mock_gateway.html', {'donation': donation})
