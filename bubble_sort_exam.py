def bubble_sort(nilai_siswa):
    n = len(nilai_siswa)
    for i in range(n-1):
        for j in range(n-i-1):
            if nilai_siswa[j] > nilai_siswa[j+1]:
                nilai_siswa[j], nilai_siswa[j+1] = nilai_siswa[j+1], nilai_siswa[j]

# Daftar nilai siswa
nilai_siswa = [78, 65, 90, 82,]

# Memanggil fungsi bubble sort
bubble_sort(nilai_siswa)

# Menampilkan hasil pengurutan
print("Hasil pengurutan:", nilai_siswa)