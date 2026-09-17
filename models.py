from django.db import models
from django.contrib.auth.models import User


class PredictionRecord(models.Model):
    DISEASE_CHOICES = [
        ('TB',    'Tuberculosis'),
        ('SKIN',  'Skin Disease'),
        ('MAL',   'Malaria'),
        ('ASTH',  'Asthma'),
        ('CHKPX', 'Chickenpox'),
    ]
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    disease_type   = models.CharField(max_length=10, choices=DISEASE_CHOICES)
    input_data     = models.TextField()
    prediction     = models.CharField(max_length=100)
    confidence     = models.FloatField()
    uploaded_image = models.ImageField(
        upload_to='uploads/', null=True, blank=True)
    created_at     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} — {self.disease_type} — {self.prediction}"


class ContactMessage(models.Model):
    name       = models.CharField(max_length=100)
    email      = models.EmailField()
    subject    = models.CharField(max_length=200)
    message    = models.TextField()
    sent_at    = models.DateTimeField(auto_now_add=True)
    is_read    = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} — {self.subject}"