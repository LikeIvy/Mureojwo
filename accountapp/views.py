from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'accountapp/test.html')
