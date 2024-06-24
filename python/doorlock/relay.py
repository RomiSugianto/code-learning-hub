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