from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth import login, authenticate, logout  # add to imports
from django.contrib import messages  # library to display flash message into the website

from .models import Tracker, About, Portfolio, Contact, Category, PDF
from django.core.mail import EmailMessage, BadHeaderError
from .forms import PDFForm, ContactForm


# Create your views here.
# https://docs.djangoproject.com/en/4.0/ref/request-response/#django.http.HttpRequest.META

def CV_Web(request):

    latest_description = About.objects.latest('updated_on').description # get the latest value of About description
    portfolios = Portfolio.objects.all()
    categories = Category.objects.all()
    pdf_link = PDF.objects.latest('updated_on') # get latest pdf.file (link) updated in the database
    final_pdf_link = '/static/assets/{}'.format(pdf_link.file) # to generate automatically the latest link pdf upload

# ==============================================
#                   Track User Meta data : Ip , web service , web browser
    user_ip_address = request.META.get('REMOTE_ADDR')
    user_hostname = request.META.get('REMOTE_HOST')
    user_agent = request.META.get('HTTP_USER_AGENT')
    user_server = request.META.get('SERVER_NAME')
    user_port = request.META.get('SERVER_PORT')

    #host = request.get_host()

    Tracker.objects.create(
        user_ip_address=user_ip_address,
        user_hostname=user_hostname,
        user_agent=user_agent,
        user_server=user_server,
        user_port=user_port
    )
# =================================================
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save form data to Django models
            contact = Contact(name=form.cleaned_data['name'],
                              email=form.cleaned_data['email'],
                              phone=form.cleaned_data['phone'],
                              message=form.cleaned_data['message'])
            contact.save()
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'message': form.cleaned_data['message']
            }
            from_email = settings.EMAIL_HOST_USER
            to_admin_email = settings.ADMIN_EMAIL
            cc_admin_email = [to_admin_email]

            message = '''
            From:\n{}\n
            to:\n{}\n
            Message:\n{}\n
            Email:\n{}\n
            Phone:\n{}\n
            '''.format(form.cleaned_data['name'], to_admin_email, form.cleaned_data['message'], form.cleaned_data['email'], form.cleaned_data['phone'])

            try:
                # Send email to admin
                email = EmailMessage('Feedback', message, from_email, [form.cleaned_data['email']], cc=cc_admin_email)
                email.send()
            except ValueError:
                messages.error(request, 'Error sending your message')
                return redirect('CV')
            return redirect('success/')
        else:
            form = ContactForm()
    else:
        form = ContactForm()

    context = {'Abouts': latest_description, 'form': form, 'categories': categories, 'portfolios': portfolios, 'pdf': final_pdf_link}
    return render(request, 'cv_page.html', context)


def is_superuser(user):
    return user.is_superuser

def redirect_email(request):
    return render(request, 'Success_page.html')


@login_required
@user_passes_test(is_superuser)
def UploadFile(request):
    if request.method == 'POST':
        form = PDFForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = PDFForm()
        context = {
            'form': form,
        }
    return render(request, 'pdf_load.html', context)


