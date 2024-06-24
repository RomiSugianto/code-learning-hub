import os
try:
    os.remove('daftar-hadir.txt')
    print ("File sudah dihapus..")
except (IOError, OSError) as e:
    print ("proses error karena : ", e)