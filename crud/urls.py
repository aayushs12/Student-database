"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.conf.urls.static import static
from django.conf.urls import handler404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.stdisplay,name="stdisplay"),
    path('Create/',views.stinsert,name="stinsert"),
    path('Edit/<int:stid>',views.stedit,name="stedit"),
    path('Update/<int:stid>',views.stupdate,name="stupdate"),
    path('Delete/<int:stid>',views.stdel,name="stdel"),
    path('data/', views.stsearch,name="stsearch"),
    path('data/<int:stid>',views.stDetailView),
    path('data/<int:stid>/',views.stDetailView),
    path('wrong/',views.sdisplay),
    path('courses/',views.cdisplay,name="cdisplay"),
    path('cdetail/<str:cid>',views.coursedisplay,name="cdisplay")
]
handler500="crud.views.handleit"
