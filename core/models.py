import uuid
from django.db import models
from django.contrib.auth.models import User

class Handover(models.Model):
    RISK_CHOICES = [
        ('LOW', 'Low Risk'),
        ('MODERATE', 'Moderate Risk'),
        ('HIGH', 'High Risk'),
        ('UNSTABLE', 'Unstable / Critical'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.CharField(max_length=50, verbose_name="Patient ID")
    patient_name = models.CharField(max_length=150, verbose_name="Patient Name")
    patient_age = models.PositiveIntegerField(verbose_name="Age")
    patient_gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    bed_number = models.CharField(max_length=20, verbose_name="Bed Number")

    # ISBAR Fields
    situation = models.TextField(blank=True, null=True, help_text="S - Situation")
    background = models.TextField(blank=True, null=True, help_text="B - Background")
    assessment = models.TextField(blank=True, null=True, help_text="A - Assessment")
    recommendation = models.TextField(blank=True, null=True, help_text="R - Recommendation")

    risk_stratification = models.CharField(max_length=20, choices=RISK_CHOICES, default='LOW')
    is_override = models.BooleanField(default=False, verbose_name="Emergency Override Triggered")
    override_reason = models.TextField(blank=True, null=True, help_text="Mandatory if Emergency Override is active")

    outgoing_physician = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='outgoing_handovers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} ({self.patient_id}) - Bed {self.bed_number}"

class Task(models.Model):
    PRIORITY_CHOICES = [('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')]
    
    handover = models.ForeignKey(Handover, on_delete=models.CASCADE, related_related_name='tasks', related_name='tasks')
    description = models.CharField(max_length=255)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MEDIUM')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Assigned Physician")
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.description} ({self.priority})"
