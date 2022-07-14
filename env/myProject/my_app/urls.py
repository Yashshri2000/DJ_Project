from django.urls import path
from .views import *

urlpatterns = [
    path('',home1, name='home'),
    path('edit_profile/<int:id>',update_profile, name='edit_profile'),
]