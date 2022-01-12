from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("안녕!! Django")

def greet(request):
    return render(request, 'basic1/greet.html')

def fruit_from(request):
    return render(request, 'basic1/fruit_from.html')

def fruit(request):
    input = request.POST.get("favorite")
    print("input = ", input)
    return HttpResponse("좋아하는 과일: " + input + "^3^ 완전 먹고싶다! 히히")