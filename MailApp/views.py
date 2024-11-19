from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail as django_send_mail

def send_mail(request):
    context = {}
    if request.method == 'POST':
        address = request.POST.get('address')
        body = request.POST.get('message')
        subject = request.POST.get('subject')
        recipient_list = [email.strip() for email in address.split(',') if email.strip()]
        if recipient_list:
            try:
                django_send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
                context = {
                    'result': 'Email sent successfully'
                }
            except Exception as e:
                context = {
                    'result': f'Error sending email: {e}'
                }
        else:
            context = {
                'result': 'All fields are required'
            }
    return render(request, 'index.html', context)
