def segi_sembilan():
    print('='*40)
    print('KELILING SEGI SEMBILAN')
    print('='*40)

    s = int(input('masukkan sisinya: '))
    l = lambda s : 9 * s

    print(f'keliling : {l(s)}')

segi_sembilan()