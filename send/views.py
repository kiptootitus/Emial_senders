from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def index(request):
    send_mail('Hello Titus ', 
    ' Hello there this is Titus, testing django send mail project, if you get so thumbs up', 
    'kiptootitus75@gmail.com',
    ['s.sanbf@gmail.com', 'jeptoomercy2001@gmail.com', 'tituskiptoo65@gmail.com'],
    fail_silently=False)
    return render(request, 'index.html')
