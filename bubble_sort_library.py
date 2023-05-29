def bubble_sort(books):
    n = len(books)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if int(books[j][2]) > int(books[j + 1][2]):
                books[j], books[j + 1] = books[j + 1], books[j]

#Daftar Buku (Judul,Penulis,Jumlah Halaman)
books = [
    ["Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "320"],
    ["To Kill a Mockingbird", "Harper Lee", "281"],
    ["The Great Gatsby", "F. Scott Fitzgerald", "180"],
    ["Pride and Prejudice", "Jane Austen", "432"],
    ["1984", "George Orwell", "328"]
]

#Memanggil fungsi bubble_sort untuk mengurutkan daftar buku
bubble_sort(books)

#Mencetak hasil pengurutan
print("Hasil pengurutan berdasarkan jumlah halaman secara ascending:")
for item in books:
    print(item)