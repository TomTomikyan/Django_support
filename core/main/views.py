from django.shortcuts import render,redirect
from .models import support

# Create your views here.

def Home(request):
    return render(request,'home.html',context={

    })
def Support(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_text = request.POST.get('text')
        support.objects.create(email=user_email,text=user_text)
        return redirect('support')
    return render(request,'support.html',context={
        
    })