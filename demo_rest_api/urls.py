from django.urls import path
from .views import DemoRestApi
from . import views

urlpatterns = [

    path('', DemoRestApi.as_view()),
]