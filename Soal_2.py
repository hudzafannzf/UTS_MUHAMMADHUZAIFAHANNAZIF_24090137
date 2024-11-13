while True: 
    input_tahun = str(input("Masukan Tahun: "))

if input_tahun: 
    input_tahun / 400 
    print(f'Tahun {input_tahun} merupakan Tahun KABISAT')

    if input_tahun:
        input_tahun / 4
        print(f'Tahun {input_tahun} termasuk tahun kabisat')

else:
    print(f'Tahun {input_tahun} Bukan termasuk tahun kabisat')