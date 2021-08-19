from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Resume Inquiry"
            body = {
            'name': form.cleaned_data['name'],
            'email' : form.cleaned_data['email'],
            'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'azeezsodiqkayode@gmail.com', ['azeezsodiqkayode@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    form = ContactForm()
    return render(request, 'home.html', {'form':form})



