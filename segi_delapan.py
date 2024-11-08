def segi_lima():
    print('='*40)
    print('KELILING SEGI DELAPAN')
    print('='*40)

    s = int(input('masukkan panjang sisinya: '))
    l = lambda s : 8 * s

    print(f'keliling : {l(s)}')

segi_lima()