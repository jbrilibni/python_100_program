print('='*25)
print('PROGRAM KONVERSI CELSIUS')
print('='*25)

c = float(input('Masukkan Suhu Celsius: '))
f = 9/5 * c + 32
k = c + 273.15
r = 4/5 * c

print('Hasil Konversi:')
print(f, 'Fahrenheit')
print(k, 'Kelvin')
print(r, 'Reamur')