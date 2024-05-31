from django.shortcuts import render
from RPi import GPIO as GPIO
from django.http import JsonResponse

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT)
setup()
# Create your views here.

def ledset(request,state):
    if state:
        GPIO.output(17,GPIO.HIGH)
    else:
        GPIO.output(17,GPIO.LOW)
    return JsonResponse({'üres':'a pride ot be kell tiltani'})

def led0(request):
    return render(request,"led.html",{})