from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import NewletterUser
from .forms import SubscriberForm
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Helper Functions
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

@csrf_exempt
def newsletter(request):
    if request.method == 'POST':
        sub = NewletterUser(email=request.POST['email'], conf_num=random_digits())
        sub.save()
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=sub.email,
            subject='Newsletter Confirmation',
            html_content='Thank you for signing up for my email newsletter! \
                Please complete the process by \
                <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \
                confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                                                       sub.email,
                                                       sub.conf_num))
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return render(request, 'portifolio/index.html', {'email': sub.email, 'action': 'added', 'form': SubscriberForm()})
    else:
        return render(request, 'portifolio/index.html', {'form': SubscriberForm()})

def confirm(request):
    sub = NewletterUser.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'portifolio/index.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'portifolio/index.html', {'email': sub.email, 'action': 'denied'})

def delete(request):
    sub = NewletterUser.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        return render(request, 'portifolio/index.html', {'email': sub.email, 'action': 'unsubscribed'})
    else:
        return render(request, 'portifolio/index.html', {'email': sub.email, 'action': 'denied'})
