ask = True
username = "romi"
while ask:
    temp=input('masukan username:')
    userinput = (temp)
    if userinput == username:
        ask=False
        print("selamat datang ",userinput)
    else:
        ask=True
        print("username salah")