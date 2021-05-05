#membaca file per baris
file_puisi = open("puisi.txt", "r")

print(file_puisi.readlines())

file_puisi.close()

#membaca semua teks dalam file
file_puisi = open("puisi.txt", "r")
puisi = file_puisi.read()

print(puisi)

file_puisi.close()

