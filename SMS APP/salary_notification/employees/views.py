from django.shortcuts import render
from .models import Employee
from django.http import JsonResponse
from twilio.rest import Client


def dashboard(request):
    employees = Employee.objects.all()
    return render(request, "employees/dashboard.html", {"employees": employees})


# Twilio Configuration
TWILIO_SID = "ACaf90cef83cb654308749fec374c96e03"  
TWILIO_AUTH_TOKEN = "13097dde094440db8db39167b799adef"  
TWILIO_PHONE = "+1 775 368 2614"  

def send_test_sms(request):
    test_phone_number = "+639153875230"  
    message_body = "Hi, this is Boss I message your account send already send money."

    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            to=test_phone_number,
            from_=TWILIO_PHONE,
            body=message_body
        )
        return JsonResponse({"status": "Success", "sid": message.sid})
    except Exception as e:
        return JsonResponse({"status": "Failed", "error": str(e)})
    
    
