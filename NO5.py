#validasi username dan password

username_code = 'gita shavira'
password_code = '12345'
kesempatan = 3
while kesempatan>0:
    user=input('Masukkan Username : ').lower()
    passw=input('Masukkan Password : ')
    if user==username_code and passw==password_code:
        print('Anda Berhasil Masuk')
        break
    else:
        kesempatan=kesempatan-1
else:
    print('Maaf Username dan Password anda salah')
