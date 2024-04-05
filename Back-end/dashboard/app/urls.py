from django.urls import path
from . import views
urlpatterns = [
    path('showdata/',views.get_data)
]
