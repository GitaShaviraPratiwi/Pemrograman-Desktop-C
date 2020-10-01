jumlah_data = int(input("Masukkan jumlah data = "))
data_nilai = []
for i in range(1,jumlah_data+1):
    n=int(input("Masukkan data ke-%d = " %i))
    data_nilai.append(n)
ratarata=0
for j in range(len(data_nilai)):
    ratarata+=data_nilai[j]
hasil=ratarata/jumlah_data
print('Nilai rata-rata dari data',data_nilai,"adalah = ",hasil)
