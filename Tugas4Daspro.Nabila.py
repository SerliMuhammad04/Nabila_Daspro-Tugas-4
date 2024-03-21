# Meminta input dari pengguna 
nilai = int(input("Masukkan angka pilihan Anda: "))


convert = bin(nilai)[2:]
biner = convert.zfill(nilai)

oktal = oct(nilai)[2:]
desimal = (nilai)
heksadesimal = hex(nilai)[2:]

print("Bilangan Biner:", biner)
print("Bilangan Oktal:", oktal)
print("Bilangan Desimal:", desimal)
print("Bilangan Heksadesimal:", heksadesimal)
