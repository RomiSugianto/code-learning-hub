ask = True
while ask:
    temp=input('masukan angka kurang dari 10 !!!:')
    angka = int(temp)
    if angka<10:
        ask=False
        print("anda menginput nila",angka)
    else:
        ask=True