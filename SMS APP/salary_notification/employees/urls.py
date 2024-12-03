from django.urls import path
from .views import send_test_sms
from .views import dashboard


urlpatterns = [
    # Other paths...
    path('send-test-sms/', send_test_sms, name='send_test_sms'),
     path('', dashboard, name='dashboard'),
]
