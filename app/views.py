from django.shortcuts import render
from RPi import GPIO as GPIO

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT)
# Create your views here.

def led1(request):
    if request.POST["state"] == "on":
        GPIO.output(17,GPIO.HIGH)
    elif request.POST["state"] == "off":
        GPIO.output(17,GPIO.LOW)
    print(request.POST["state"])

def led0(request):
    return render(request,"led.html",{})