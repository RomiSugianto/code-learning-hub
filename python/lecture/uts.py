dictionary = {
    'Nama'  : 'Budi santoso',
    'Kelas' : '12.4A',
    'NO HP' : '081298889299'
}

for key,val in dictionary.items():
    print(key, ":", val)
print('\n')

absen = int(input('Masukan Nilai Absen  :'))
tugas = int(input('Masukan Nilai Tugas  :'))
uts = int(input('Masukan Nilai UTS    :'))
uas = int(input('Masukan Nilai UAS    :'))

nilai = (absen*10/100)+(tugas*20/100)+(uts*30/100)+(uas*40/100)

print('\n')
print('Nilai Akhir Anda Adalah : ', nilai)
