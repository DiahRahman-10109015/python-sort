# python-sort
Pada praktikum kali ini membahas mengenai materi Bubble Sort dan Selection Sort 
**PERCOBAAN PRAKTIKUM**
**BUBBLE SORT**
=> Saya mempelajari bahwa Bubble Sort menggunakan metode pengurutan data dengan cara membandingkan data dan menukar elemen-elemen adjacent secara berulang-ulang sampai seluruh elemen terurut.
=> Kelebihan dari metode ini yaitu implementasinya yang sederhana dan mudah dipahami.
=> Pada percobaan praktikum 1-7 menggunakan Bubble Sort, ada dua pengurutan yang dapat di jalankan yaitu mengurutkan secara ascending dan descending 
   - ascending yaitu mengurutkan dari nilai terkecil ke terbesar (a-z) (1-9)
   - descending yaitu mengurutkan dari nilai terbesar ke terkecil (z-a) (9-1)
=> Pada percobaan praktikum Bubble Sort menggunakan perulangan for untuk membandingkan antara nilai yang terkecil dan terbesar sehingga diurutkan dengan fungsi tertentu.
   - fungsi yang menggunakan operasi **if arr[j] > arr[j+1]:** untuk membandingkan nilai terkecil untuk mengurutkan secara ascending pembeda disini yaitu operasi (>), maka        nilai akan diurutkan dari yang terkecil
   - fungsi yang menggunakan operasi **if arr[j] < arr[j+1]:** untuk membandingkan nilai terbesar untuk mengurutkan secara descending pembeda disini yaitu operasi (<), maka      nilai akan diurutkan dari nilai yang terbesar

**SELECTION SORT**
=> Saya mempelajari bahwa Selection Sort menggunakan metode pengurutan data dengan cara mencari elemen terkecil dari sisa array yang belum diurutkan dan menukarnya dengan elemen pertama.
=> Kelebihan dari metode ini yaitu jumlah perbandingan yang tetap, yaitu sebanyak (n-1) perbandingan, di mana n adalah jumlah elemen yang diurutkan.
=> Pada percobaan praktikum 8-14 menggunakan Selection Sort, ada dua pengurutan yang dapat di jalankan yaitu mengurutkan secara ascending dan descending 
   - ascending yaitu mengurutkan dari nilai terkecil ke terbesar (a-z) (1-9)
   - descending yaitu mengurutkan dari nilai terbesar ke terkecil (z-a) (9-1)
=> Pada percobaan praktikum Selection Sort menggunakan perulangan for untuk menukar nilai terkecil dengan nilai yang ada pada posisi terkini.
   - fungsi yang menggunakan operasi **if arr[j] < arr[min_index]:** merupakan untuk mengurutkan secara ascending pembeda disini yaitu operasi (> arr[min_index]), maka nilai      akan diurutkan dari yang terkecil
   - fungsi yang menggunakan operasi **if arr[j] > arr[min_index]::** merupakan untuk mengurutkan secara descending pembeda disini yaitu operasi (< arr[min_index]), maka          nilai akan diurutkan dari yang terbesar
   -
**LATIHAN PRAKTIKUM**
Pada latihan praktikum 1
=> Menggunakan perulangan for dengan fungsi **if arr[j] > arr[j+1]:** untuk melakukan perbandingan untuk mengurutkan nilai siswa secara ascending dengan Bubble Sort

Pada latihan praktikum 2
=> Menggunakan perulangan for dengan fungsi **if arr[j] < arr[j+1]:** untuk melakukan perbandingan untuk mengurutkan nilai siswa secara descending dengan Selection Sort

Pada latihan praktikum 3
=> Menggunakan perulangan for dengan fungsi **if int(books[j][2]) > int(books[j + 1][2]):** dengan perbandingan untuk mengurutkan nama buku secara ascending dengan Bubble Sort

Pada latihan praktikum 4
=> Menggunakan perulangan for dengan fungsi **if daftar_angka[j] < daftar_angka[j+1]:** dengan menukar elemen terkecil dengan posisi terkini kemudian pindah ke posisi terkini untuk mengurutkan angka secara ascending dengan Selection Sort

Pada latihan praktikum 5
=> Menggunakan perulangan for dengan fungsi **if pemain[j][2] > pemain[min_index][2]:** dengan menukar elemen terkecil dengan posisi terkini kemudian pindah ke posisi terkini untuk mengurutkan angka secara descending dengan Selection Sort
