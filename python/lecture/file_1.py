try:
    sebuah_file = open("absen.txt", 'w')
    print ("nama file yang tadi dibuat : ", sebuah_file.name)
    print ("mode pembacaan file : ", sebuah_file.mode)
    print ("apakah filenya udah ditutup ? : ", sebuah_file.closed)    
    sebuah_file.close()
    print ("apakah filenya udah ditutup ? : ", sebuah_file.closed)
except (IOError, OSError)as e:
    print ("proses gagal karena : ", e)