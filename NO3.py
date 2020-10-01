#program ini untuk menghitung index massa tubuh
print('Kalkulator BMI (Body Mass Index)')

BB = float(input('Berat Badan anda (kg) = '))
TB = int(input('Tinggi Badan anda (cm) = '))

cTB = TB/100
BMI = BB/(cTB*cTB)

print('BMI anda yaitu = ',BMI)
if BMI < 18.5:
    print('Anda Termasuk Kelompok Berat Badan Kurang')
elif BMI <= 22.9:
    print('Anda Termasuk Kelompok Berat Badan Normal')
elif BMI <= 29.9:
    print('Anda Termasuk Kelompok Berat Badan Berlebihan (Kecenderungan Obesitas)')
else:
    print('Anda Termasuk Kelompok Obesitas')
