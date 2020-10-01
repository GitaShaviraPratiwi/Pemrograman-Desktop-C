#Menentukan nilai min & max dari kumpulan data
n=int(input("Masukkan Banyaknya Data = "))
data=[]
for i in range(1,n+1):
    input_data=int(input("Masukkan data ke-%d = " %i))
    data.append(input_data)
    
def nilai_terbesar(data):
    n_max = 0
    for i in data:
        if i > n_max:
            n_max = i
    return n_max

def nilai_terkecil(data):
    ind=0
    n_min = data[ind+1]
    for j in data:
        if j < n_min:
            n_min = j
    return n_min

#main program
print()
print('Angka Terbesar dari data ',data,'yaitu = ',nilai_terbesar(data))
print('Angka Terkecil dari data ',data,'yaitu = ',nilai_terkecil(data))

