# Django Mail App

This is a simple Django app that allows sending emails through a web interface. It provides functionality to input recipient email addresses, subject, and message content. After submission, it attempts to send an email to the specified recipients using the configured SMTP settings in Django's `settings.py` file.

## Features
- Users can input multiple email addresses separated by commas.
- Users can specify the subject and message body.
- Emails are sent using the SMTP configuration provided in the Django project settings.
- Error handling for invalid or missing fields.
- Success or failure messages are displayed on the webpage after attempting to send the email.

## Prerequisites

Before using this app, ensure that you have the following:

1. **Python 3.x** installed on your machine.
2. **Django** installed in your environment.
   - To install Django, use the following command:
     ```bash
     pip install django
     ```
3. An SMTP email configuration to send emails. You need to set up the email host and email credentials in the `settings.py` file.

## Installation

1. Clone the repository or copy the app into your Django project.

2. Ensure your Django settings include proper email configuration. For example:

```python
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # or any other email service provider
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'  # Your email
EMAIL_HOST_PASSWORD = 'your-email-password'  # Your email password or app-specific password
