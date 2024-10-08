"""
URL configuration for OrganProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from OrganApp.views import index,signup,loginview
from OrganApp import admin_urls,user_urls,bank_urls
from OrganApp import views

urlpatterns = [
    # path('admin/', admin.site.urls),/
    path('',index.as_view(),name='index'),
    path('login/',loginview.as_view(),name='login'),
    path('admin/',admin_urls.urls()),
    path('signup',signup.as_view(),name='signup'),
    path('user/',user_urls.urls()),
    path('bloodbank/',bank_urls.urls()),
    path('activate/<str:uidb64>/<str:token>/',views.activate_account, name='activate'),
    path('update-password', views.update_password_view, name='update_password')


]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)