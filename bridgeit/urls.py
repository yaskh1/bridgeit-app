from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
from django.conf import settings

# Custom BridgeIT Logo & Branding Header
logo_html = mark_safe(getattr(settings, 'ADMIN_STYLES', '') + """
    <div style="text-align: center; margin-bottom: 20px;">
        <!-- BridgeIT Brand Logo Icon -->
        <div style="margin-bottom: 8px;">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="display: inline-block;">
                <path d="M4 12H20M4 12L9 7M4 12L9 17" stroke="#1A4D54" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M20 12L15 7M20 12L15 17" stroke="#28A7A0" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        </div>
        <!-- Dual-Teal Styled Title -->
        <div style="font-size: 32px; font-weight: 900; font-style: italic; color: #1A4D54; letter-spacing: -0.5px;">
            Bridge<span style="color: #28A7A0; font-style: normal;">IT</span>
        </div>
        <!-- Slogan -->
        <div style="font-size: 12px; color: #555555; font-weight: 700; margin-top: 4px; letter-spacing: 0.5px; text-transform: uppercase;">
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
