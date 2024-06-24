import os
try:
    os.rename('absen.txt', 'daftar-hadir.txt')
    print ("Nama file sudah diubah..")
except (IOError, OSError) as e:
    print ("proses error karena : ", e)