print('='*30)
print('PROGRAM KONVERSI FAHRENHEIT')
print('='*30)

f = float(input('Masukkan Suhu Fahrenheit: '))
c = 5/9 * (f-32)
k = 5/9 * (f-32) + 273.15
r = 4/9 * (f-32)

print('Hasil Konversi:')
print(c, 'Celsius')
print(k, 'Kelvin')
print(r, 'Reamur')