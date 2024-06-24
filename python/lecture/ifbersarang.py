gaji = int(input("masukan gaji: "))
berkeluarga = True
punya_rumah = True

if gaji > 3000000:
    print ("GAJI SUDAH DIATAS UMR")
    if berkeluarga:
        print("WAJIB IKUTAN ASURANSI DAN MENABUNG UNTUK PENSIUN")
    else:
        print("TIDAK PERLU IKUT ASURANSI")

    if punya_rumah:
        print("WAJIB BAYAR PAJAK RUMAH")
    else:
        print("TIDAK WAJIB BAYAR PAJAK RUMAH")
else:
    print("GAJI BELUM UMR")
