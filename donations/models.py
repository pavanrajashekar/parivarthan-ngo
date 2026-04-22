from django.db import models
from django.utils import timezone

class Donation(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Success', 'Success'),
        ('Failed', 'Failed'),
    )

    donor_name = models.CharField(max_length=100)
    donor_email = models.EmailField()
    amount = models.PositiveIntegerField(help_text="Amount in INR")
    
    # Razorpay Specifics
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    date_donated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.donor_name} - ₹{self.amount} ({self.status})"
