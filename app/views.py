from django.shortcuts import render
from RPi import GPIO as GPIO
from django.http import JsonResponse

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT)
# Create your views here.

def ledpost(request):
    if request.POST["state"] == "on":
        GPIO.output(17,GPIO.HIGH)
    elif request.POST["state"] == "off":
        GPIO.output(17,GPIO.LOW)
    print(request.POST["state"])
    return JsonResponse({'üres':'a pride ot be kell tiltani'})

def led0(request):
    return render(request,"led.html",{})