try:
    sebuah_file = open("absen.txt", 'rb')
    print ("nama file yang tadi dibuat : ", sebuah_file.name)
    print ("mode pembacaan file : ", sebuah_file.mode)
    print ("apakah filenya udah ditutup ? : ", sebuah_file.closed)
    print ("isi file : \n")
    for line in sebuah_file:
        print (line)
    print ("posisi pointer pada file : ", sebuah_file.tell())
    print ("kembali lagi ke awal : ", sebuah_file.seek(0, 0))
    print ("isi file : \n")
    for line in sebuah_file:
        print (line)
    print ("posisi pointer pada file : ", sebuah_file.tell())
    sebuah_file.close()
    print ("apakah filenya udah ditutup ? : ", sebuah_file.closed)
except IOError as e:
    print ("proses gagal karena : ", e)