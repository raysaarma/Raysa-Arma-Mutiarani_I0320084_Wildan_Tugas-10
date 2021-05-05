print('SILAHKAN MASUKKAN BIODATA DIRI ANDA')
print('-----------------------------------')

nama = input('Nama : ')
TTL = input('TTL : ')
alamat = input('Alamat : ')
nim = input('NIM : ')
prodi = input('Prgram studi : ')


teks = 'Nama : {}\nTTL : {}\nAlamat : {}\nNIM : {}\nProgram studi : {}'.format(nama, TTL, alamat, nim, prodi)

file_bio= open('biodata.txt', 'a')
file_bio.write(teks)
file_bio.close()