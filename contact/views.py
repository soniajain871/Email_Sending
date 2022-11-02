from contextlib import redirect_stderr
from django.shortcuts import render 
from django.core.mail import send_mail
from .forms import contactForm
# Create your views here.
def index(request):
    print("contact form")
    #if request.method
    form =contactForm()  
      
   # if form.is_valid():
         
    send_mail("The contact from mail","this is message",
    "noreply@codewithstein.com",['soniajain@gmail.com'],fail_silently=False,)
    print ('email done')
    return render(request, 'contact/index.html')
   # else:
    #      form =contactForm()

    #return render(request, 'contact/index.html', {'form': form})
