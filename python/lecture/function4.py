def cetak_perolehan_nilai( nama, twitter, *scores):
    print ("Nama : ", nama)
    print ("Twitter : ", twitter)
    print ("Score yang diperoleh : ")
    i = 1
    for score in scores:
        print ("nilai ke - %d : %d" % (i, score))
        i= i + 1

    return
# kalau parameter diisi semua
print ("Dengan adanya variable-length variabel sisa akan menjadi tuple : ")
cetak_perolehan_nilai("Silvy", "@sivlysiv", 90, 80, 70, 80, 90)