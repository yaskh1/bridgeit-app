from django.contrib import admin
from .models import Handover, Task

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

@admin.register(Handover)
class HandoverAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'patient_id', 'bed_number', 'risk_stratification', 'is_override', 'created_at')
    list_filter = ('risk_stratification', 'is_override', 'created_at')
    search_fields = ('patient_name', 'patient_id', 'bed_number')
    inlines = [TaskInline]

    fieldsets = (
        ('Patient Identification', {
            'fields': ('patient_id', 'patient_name', 'patient_age', 'patient_gender', 'bed_number', 'risk_stratification')
        }),
        ('Emergency Override Option', {
            'fields': ('is_override', 'override_reason'),
            'description': 'Check box below if active resuscitation or emergency prevents full ISBAR completion.'
        }),
        ('ISBAR Structured Clinical Information', {
            'fields': ('situation', 'background', 'assessment', 'recommendation')
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.outgoing_physician:
            obj.outgoing_physician = request.user
        super().save_model(request, obj, form, change)
