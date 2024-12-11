print('='*25)
print('PROGRAM KONVERSI KELVIN')
print('='*25)

k = float(input('Masukkan Suhu Kelvin: '))
c = k - 273.15
f = 9/5 * (k-273.15) + 32
r = 4/5 * (k-273.15)

print('Hasil Konversi:')
print(c, 'Celsius')
print(f, 'Fahrenheit')
print(r, 'Reamur')