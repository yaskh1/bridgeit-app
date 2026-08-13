from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect

# Customize Admin Header & Title to BridgeIT
admin.site.site_header = "BridgeIT Admin Portal"
admin.site.site_title = "BridgeIT"
admin.site.index_title = "Pass it over. Safely."

# Redirect homepage directly to the Login Screen
def redirect_to_login(request):
    return redirect('/admin/login/')

urlpatterns = [
    path('', redirect_to_login),
    path('admin/', admin.site.urls),
]
