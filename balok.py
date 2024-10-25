print('='*40)
print('rumus balok')
print('='*40)

p = float(input('masukkan panjang: '))
l = float(input('masukkan lebar: '))
t = float(input('masukkan tinggi: '))

lp = lambda p,l,t : 2 * (p * 1 * p * t * l * t)
v = lambda p,l,t : p * l * t
k = lambda p,l,t : 4 * (p + l + t)

print('luas permukaan: ',p,l,t)
print('volume : ',p,l,t)
print('keliling : ',p,l,t)