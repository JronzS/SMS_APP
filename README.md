Employee Salary Notification System 📲

This is a simple Django-based web application for managing employee salary notifications. The system allows you to send salary notifications via SMS directly to employees' mobile phones using the Vonage SMS API, which is compatible with Philippine numbers.
📋 Features

    View employee details (name, phone number, bank account, salary) on a dashboard.
    Send individual or bulk SMS notifications to employees.
    Log each notification's status (Sent, Failed) for tracking purposes.

🛠️ Tech Stack

    Backend: Django (Python)
    Frontend: HTML, CSS (via Bootstrap 5)
    SMS API: Vonage (formerly Nexmo) for global SMS support


📦 Project Structure

project-folder/
├── employees/
│   ├── migrations/
│   ├── templates/
│   │    └── employees/
│   │         └── dashboard.html
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── manage.py
├── requirements.txt
└── README.md

