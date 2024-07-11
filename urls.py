from django.urls import path
from . import views
# Create your views here.


urlpatterns = [
    path('', views.ContactUsView.as_view(), name='contact_us_page'),
]
