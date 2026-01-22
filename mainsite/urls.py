
from django.urls import path
from mainsite import views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
]