def bubble_sort(daftar_angka):
    n = len(daftar_angka)
    for i in range(n-1):
        for j in range(n-i-1):
            if daftar_angka[j] < daftar_angka[j+1]:
                daftar_angka[j], daftar_angka[j+1] = daftar_angka[j+1], daftar_angka[j]

# Daftar angka
daftar_angka = [42, 19, 33, 8, 55]

# Memanggil fungsi bubble sort
bubble_sort(daftar_angka)

# Menampilkan hasil pengurutan
print("Hasil pengurutan:", daftar_angka)