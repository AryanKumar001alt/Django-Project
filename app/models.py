from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
)

class ExamForm(models.Model):
    # ✅ FIXED (no migration error)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    full_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=15)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    # ✅ FIXED (no migration error)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.full_name