from django.urls import path
from . import views

urlpatterns = [
    path('', views.PresentationListView.as_view(), name='index'),
]