"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from home.views import *
from vege.views import*
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',home,name="home"),
    path('receips/',receips,name='receips'),
    path('del_rec/<id>/',del_rec,name="del_rec"),
    path('update_rec/<id>/',update_rec,name='update_rec'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('login/',login_pg,name='login_pg'),
    path('register/',register_pg,name='register_pg'),
    path('logout/',logout_pg,name="logout_pg"),
    path('sucess/',sucess),
    path('student/',get_students ,name="get_students"),
    path('see_marks/<str:student_id>',see_marks,name="see_marks"),
    path('admin/', admin.site.urls),
    path('send_email/',send_email,name="send_email"),]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+=staticfiles_urlpatterns()