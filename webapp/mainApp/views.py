from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', 
    {'values':['If you have question, call mee','(003) 594 - 32 - 25']})

