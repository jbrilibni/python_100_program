print('='*40)
print('MENENTUKAN ZAT')
print('='*40)

inputan_suhu = int(input('masukkan suhu = '))
if inputan_suhu <= 0:
    print('ini adalah zat padat')
elif 0 <= inputan_suhu < 100:
    print('ini adalah zat cair')
elif inputan_suhu > 100:
    print('ini adalah zat uap')