print("=====================aplikasi sederhana dengan python====================")
absen = int(input("masukan nilai absen: "))
tugas = int(input("masukan nilai tugas: "))
uts = int(input("masukan nilai uts: "))
uas = int(input("masukan nilai uas: "))

nabsen=absen*10/100
ntugas=tugas*20/100
nuts=uts*30/100
nuas=uas*40/100
nakhir=nabsen+ntugas+nuts+nuas
print("=========================hasil nilai akhir=======================")
print("nilai absen anda adalah",nabsen)
print("nilai absen anda adalah",ntugas)
print("nilai absen anda adalah",nuts)
print("nilai absen anda adalah",nuas)
print("hasil nilai akhir anda adalah",nakhir)


if nakhir >=90 and nakhir <=100:
    grade="A"
    status="lulus"
elif nakhir>=75 and nakhir <=89:
    grade="B"
    status="lulus"
elif nakhir>=55 and nakhir <=74:
    grade="C"
    status="lulus"
elif nakhir>=40 and nakhir <=54:
    grade="D"
    status="tidak lulus"
else:
    grade="E"
    status="tidak lulus"

print("=========================grade=======================")
print("anda mendapatkan grade : ",grade)
print("anda dinyatakan : ",status)