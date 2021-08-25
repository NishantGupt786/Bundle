from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexwb(request):
    return render(request, 'indexwb.html')
