from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexml(request):
    return render(request, 'indexml.html')