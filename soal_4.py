input_bb = 0
input_tb = 0

for i in range():
    input_bb = int(input('Masukan Berat Badan (kg): '))
    input_tb = int(input('Masukan Tinggi Badan(M):  '))

    hasil_timbang = input_bb // input_tb

    if hasil_timbang < 18.5:
        tipe = print( 'Berat Badan Kurang')

    elif 18.5 <= hasil_timbang < 24.9 :
        tipe = print('Berat Badan Normal')

    elif 25 <= hasil_timbang < 29.9 :
        tipe = print('Berat Badan Kelebihan')

    elif hasil_timbang >= 30:
        tipe = print('Anda Obesitas')

    print(f'Beerat Badan:{input_bb} ')
    print(f'Tinggi Badan:{input_tb}')
    print(f'Kategori BMI : {tipe}')