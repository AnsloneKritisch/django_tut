from django.contrib import admin
from django.urls import path
from app1 import views as ap1
from app2 import views as ap2
from app3 import views as ap3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj_app1/',ap1.django_app1),
    path('dj_app2/',ap2.django_app2),
    path('dj_app3/',ap3.django_app3),
]

