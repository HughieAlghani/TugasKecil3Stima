# FUNGSI / PROSEDUR
def euclidean (x1, y1, x2, y2) :
    return float(((((x1-x2)**2) + ((y1-y2)**2))**0.5)*111)

# MAIN PROGRAM

# Menerima banyak simpul
f = open("C:/Users/Hughie/Documents/Kuliah/Jurusan/Semester 4/Strategi Algoritma/Tugas Kecil/Tugas Kecil 3/TugasKecil3Stima/test/BuahBatu.txt", "r") 
read = f.readline()
N = int(read)

# Menyediakan matriks nama dan lokasi
# Format : <Nama simpul>, <posisi x>, <posisi y>
Simpul = [['a', 0, 0] for i in range (N)]


# Menerima nama-nama simpul dan lokasinya
for i in range (N) :
    read = f.readline()
    Lokasi = read.split(" ")
    Simpul[i][0] = str(Lokasi[0])
    Simpul[i][1] = float(Lokasi[1])
    Simpul[i][2] = float(Lokasi[2])

# Menerima matriks adjacency (boolean)
# Menentukan apakah tiap simpul terhubung
Adjacency = [[-1 for j in range (N)] for i in range (N)]

for i in range (N) :
    read = f.readline()
    adj = read.split(" ")
    for j in range (N) :
        Adjacency[i][j] = int(adj[j])

# Menyediakan matriks jarak antar simpul
Direction = [[float(-1) for j in range (N)] for i in range (N)]

for i in range (N) :
    for j in range (N) :
        if (Adjacency[i][j] == 1) :
            Direction[i][j] = float(euclidean(Simpul[i][1], Simpul[i][2], Simpul[j][1], Simpul[j][2]))

print("Lokasi yang tersedia: ")
for i in range(N) :
    print("- " + Simpul[i][0])
# Menerima simpul asal dan simpul tujuan
valid = False
while (not valid) :
    Asal_str = str(input("Lokasi Anda sekarang: "))
    for i in range (N) :
        if (Asal_str == Simpul[i][0]) :
            valid = True
valid = False
while (not valid) :
    Tujuan_str = str(input("Lokasi tujuan Anda: "))
    for i in range (N) :
        if (Tujuan_str == Simpul[i][0]) :
            valid = True

for i in range (N) :
    if (Simpul[i][0] == Asal_str) :
        Asal_idx = i
    if (Simpul[i][0] == Tujuan_str) :
        Tujuan_idx = i

# List pengecekan
Cek = []

# Mencari jalur
found = False
Cek.append(Asal_str)

acuan = Asal_idx
jalur = Simpul[Asal_idx][0]
jarak = float(euclidean(Simpul[Asal_idx][1], Simpul[Asal_idx][2], Simpul[Tujuan_idx][1], Simpul[Tujuan_idx][2]))
temp = [['a', 0] for i in range (N)]
Hasil = [jalur, jarak]

while (not found) :
    count = 0
    for i in range (N) :
        if (Adjacency[acuan][i] == 1) :
            sudah = False
            for j in range (len(Cek)) :
                if (Simpul[i][0] == Cek[j]) :
                    sudah = True
            if (not sudah) :
                Cek.append(Simpul[i][0])
                jalurNew = jalur + " → " + Simpul[i][0]
                jarak = Direction[acuan][i] + euclidean(Simpul[i][1], Simpul[i][2], Simpul[Tujuan_idx][1], Simpul[Tujuan_idx][2])
                temp[count][0] = jalurNew
                temp[count][1] = jarak
                count += 1
                if (i == Tujuan_idx) :
                    found = True
                    Hasil[0] = jalurNew
    if (not found) :
        min = temp[0][1]
        for i in range (count) :
            if (temp[i][1] <= min) :
                min = temp[i][1]
                jalur = temp[i][0]
        Hasil[0] = jalur
        Hasil[1] = min
        curr = jalur.split(" → ")
        for i in range (N) :
            if (Simpul[i][0] == curr[-1]) :
                acuan = i
        for i in range (N) :
            for j in range (2) :
                temp[i][0] = 'a'
                temp[i][1] = 0
        

jalurAkhir = (Hasil[0]).split(" → ")
jarakAkhir = 0
for i in range (len(jalurAkhir)-1) :
    for j in range (N) :
        if (Simpul[j][0] == jalurAkhir[i]) :
            a = j
        if (Simpul[j][0] == jalurAkhir[i+1]) :
            b = j
    jarakAkhir += Direction[a][b]
print("Jalur yang didapatkan: " + Hasil[0])
if (jarakAkhir >= 1) :
    print("Jarak tempuh: %.2f Km" % jarakAkhir)
else :
    jarakAkhir *= 1000
    print("Jarak tempuh: %.2f m" % jarakAkhir)