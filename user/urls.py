from django.urls import path
from . import views

urlpatterns = [
    path('user_agent/', views.index, name="index"),
    path('user_agent/info/', views.info, name="info"),
    path('user_agent/sobreMi/', views.sobreMi, name="sobreMi")
]