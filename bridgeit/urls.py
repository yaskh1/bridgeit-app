from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.utils.safestring import mark_safe

# Custom BridgeIT Logo Header HTML
logo_html = mark_safe("""
    <div style="text-align: center; margin-bottom: 15px;">
        <div style="font-size: 28px; font-weight: 800; font-style: italic; color: #1A4D54; display: inline-block;">
            Bridge<span style="color: #28A7A0; font-style: normal;">IT</span>
        </div>
        <div style="font-size: 11px; color: #666; font-weight: 600; margin-top: 2px;">
            Pass it over. Safely.
        </div>
    </div>
""")

admin.site.site_header = logo_html
admin.site.site_title = "BridgeIT"
admin.site.index_title = "Shift Handover Management Portal"

def redirect_to_login(request):
    return redirect('/admin/login/')

urlpatterns = [
    path('', redirect_to_login),
    path('admin/', admin.site.urls),
]
