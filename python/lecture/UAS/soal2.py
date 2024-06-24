import salary

name=input('masukan nama:')
print('1.Direktur 2.Komisaris 3.Staff administrasi 4.Programmer')
division=input('pilih no jabatan:')

calc=salary.Salary(division)
print(name, calc.cekSalary())