from django.urls import path
from .views import courses_authorize_view

urlpatterns = [
    path('courses-authorize/', courses_authorize_view, name='authorize'),
]
