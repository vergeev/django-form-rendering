from django.urls import path

from contacts.views import Home

urlpatterns = [
    path('', Home.as_view()),
]
