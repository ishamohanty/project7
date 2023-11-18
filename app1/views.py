from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':50,'b':80,'c':100}
    return render(request,'conditions.html',d)
