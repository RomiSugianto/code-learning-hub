jurusan = str(input("pilih jurusan : "))
jam = str(input("pilih jam :"))

if jurusan == "ti":
    njurusan = "teknik informatika"
    if jam == "pg":
        njam = "07.00-16.00"
        biaya = "Rp 1.000.000"
    else:
        njam = "16.00-21.00"
        biaya = "Rp 1.500.000"
else:
    njurusan = "sistem informasi"
    if jam == "pg":
        njam = "07.00-16.00"
        biaya = "Rp 2.000.000"
    else:
        njam = "16.00-21.00"
        biaya = "Rp 2.500.000"

print("anda memilih jurusan : ",njurusan)
print("dengan pilihan jam : ",njam)
print("dengan harga : ",biaya)