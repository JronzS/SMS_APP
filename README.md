💸 Salary Notification System

This is a Django-based Salary Notification System that sends salary notifications to employees via SMS using Twilio API. It also features a simple web-based dashboard to view employee details and trigger SMS notifications for all employees.
🚀 Features

    📲 Send Salary Notifications via SMS
    📋 View Employee Details (Name, Phone, Bank Account, Salary)
    📡 Twilio Integration for seamless SMS delivery
    📅 Track Notification Status (Sent, Failed) with timestamps
    📈 Bulk Notification Sending (Send to all employees at once)

  🛠️ Usage Instructions

    Add Employees
        Log in to the admin panel at http://127.0.0.1:8000/admin/
        Add employee details (Name, Phone, Bank Account, Salary) in the Employee model.

    Send SMS Notifications
        Visit the dashboard at http://127.0.0.1:8000/
        Click the Send SMS Notifications button to send bulk notifications to all employees.
        The system will update the status of each SMS (Sent, Failed) in the SalaryNotification model.

📚 Code Explanation
1️⃣ Models

    Employee: Contains employee details (name, phone, salary, etc.).
    SalaryNotification: Tracks the status of SMS notifications sent to employees.

2️⃣ Views

    dashboard(): Renders the employee dashboard where employee information is displayed.
    send_sms_notification(): Handles SMS sending logic using Twilio API.
    send_bulk_notifications(): Sends SMS notifications to all employees and logs the status.

3️⃣ Templates

    dashboard.html: Contains a form to trigger the "Send Notifications" action.
    It also displays a table of employees and their information.
