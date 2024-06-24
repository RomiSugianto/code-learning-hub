from django.http import HttpResponse
from django.shortcuts import render
import RPi.GPIO as GPIO


# Konfigurasi pin GPIO yang terhubung dengan relay switch
relay_pin = 23

# Konfigurasi mode GPIO sebagai output
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)


# Fungsi untuk mengaktifkan relay switch
def activate_relay():
  GPIO.output(relay_pin, GPIO.HIGH)


# Fungsi untuk menonaktifkan relay switch
def deactivate_relay():
  GPIO.output(relay_pin, GPIO.LOW)


# View untuk mengaktifkan relay switch
def activate_relay_view(request):
  activate_relay()
  return HttpResponse('Relay diaktifkan')


# View untuk menonaktifkan relay switch
def deactivate_relay_view(request):
  deactivate_relay()
  return HttpResponse('Relay dinonaktifkan')


def index(request):
    context = {
        "status": "",
    }
    action = request.POST.get('action')
    if request.method == 'POST':
        # proses update lock disini
        if action == "lock":
            activate_relay()
            context['status'] = "lock"
        if action == "unlock":
            deactivate_relay()
            context['status'] = "unlock"
        return render(request, "index.html", context)
    return render(request, "index.html", context)
