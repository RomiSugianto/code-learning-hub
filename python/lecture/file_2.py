try:
    sebuah_file = open("absen.txt", 'w')
    print ("nama file yang tadi dibuat : ", sebuah_file.name)
    print ("mode pembacaan file : ", sebuah_file.mode)
    print ("apakah filenya udah ditutup ? : ", sebuah_file.closed)
    sebuah_file.write('1. Jajang Surahman, Teknik Informatika, ITENAS\n')
    sebuah_file.write('2. Angel Corine, Manajemen Informatika, UNIKOM\n')
    sebuah_file.write('3. Samsul Basri, Ilmu Komputer, UPI\n')
    sebuah_file.close()
    print ("apakah filenya udah ditutup ? : ", sebuah_file.closed)
except IOError as e:
    print ("proses gagal karena : ", e)