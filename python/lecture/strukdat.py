#cara mendefinisikan list
sebuah_list=['ZorinOS',
            'Ubuntu',
            'FreeBSD',
            'NetBSD',
            'OpenBSD',
            'Backtrack',
            'Fedora',
            'Slackwere',]

#cara mendefinisikan tuple
sebuah_tuple=('0','1','2','3','4','5','6','7','8','9')

#cara mendefinisikan sebuah Dictionary
sebuah_dictionary={'Nama':'Wiro Sableng',
                   'Prodi':'Ilmu Komputer',
                   'Email':'wirosabkeng@localhost',
                   'website':'http://www.sipampanggarang.com'}

#cara update sebuah element
#sebuah_list[5]='Kali Linux'
#print(sebuah_list)
#print("\n")

#tuple tidak dapat melakukan sebuah operasi perubahan element

#print(sebuah_dictionary)
#sebuah_dictionary['email']='sableng@localhost.com'
#print(sebuah_dictionary)



#cara menambahkan baru
#list_baru= sebuah_list+['PC Linux','Blankon','OpenSUSE']
#print(list_baru)
#print("\n")


#tuple_baru = sebuah_tuple+(10,11,12)
#print(tuple_baru)
#print("\n")


#dictionary_baru = {'Telp':'081289836702',
#                    'Alamat':'Pasundan,Bandung',}
#sebuah_dictionary.update(dictionary_baru)
#print(sebuah_dictionary)
#print("\n\n")

#cara menghapus sebuah elemen
print(sebuah_list)
del sebuah_list[0]
print(sebuah_list)
print("\n")

#tuple tidak mendukung proses penghapusan elemen


print(sebuah_dictionary)
del sebuah_dictionary['website']
print("\n")

print(sebuah_dictionary)

#cara akses list
print(sebuah_list[2:7])

#cara akses tuple
print(sebuah_tuple[3:6])

#cara akses dictionary
print(sebuah_dictionary['Nama'])
print(sebuah_dictionary['Email'])
print("\n")

for sebuah in sebuah_list:
    print(sebuah,)
print("\n")


for sebuah in sebuah_tuple:
    print(sebuah,)
print("\n")

# for sebuah in sebuah_dictionary:
# print('sebuah',':',sebuah_dictionary[sebuah])