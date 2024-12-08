from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee, SalaryNotification
from twilio.rest import Client

# Twilio Configuration
TWILIO_SID = 'AC84d9e231685647be25d48d53579fe338'
TWILIO_AUTH_TOKEN = '371b1332cb2639ea9e7bcd7452a04a73'
TWILIO_PHONE = '+14782454757'

def send_sms_notification(employee):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(
            to=employee.phone_number,
            from_=TWILIO_PHONE,
            body=f"Hi {employee.name}, your salary of PHP {employee.salary} has been credited to your account."
        )
        return "Sent" if message.sid else "Failed"
    except Exception as e:
        # Log the error for debugging
        print(f"Error sending SMS to {employee.phone_number}: {e}")
        return "Failed"


def dashboard(request):
    employees = Employee.objects.all()
    notifications = SalaryNotification.objects.all()
    return render(request, "employees/dashboard.html", {"employees": employees, "notifications": notifications})

def send_bulk_notifications(request):
    employees = Employee.objects.all()
    for employee in employees:
        status = send_sms_notification(employee)
        SalaryNotification.objects.create(employee=employee, status=status)
    return JsonResponse({"status": "Notifications sent successfully"})