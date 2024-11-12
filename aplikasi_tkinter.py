import tkinter as tk  # Mengimpor modul tkinter dengan alias tk
from tkinter import messagebox  # Mengimpor messagebox untuk menampilkan dialog pesan

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi():
    try:
        # Memeriksa setiap input apakah berupa angka
        for entry in entries:
            if not entry.get().isdigit():  # Cek jika input bukan angka
                raise ValueError("Semua nilai mata pelajaran harus berupa angka.")  # Jika bukan angka, munculkan error

        # Jika semua input valid, tampilkan hasil prediksi
        hasil_label.config(text="Prodi: Teknologi Informasi")  # Mengubah teks label hasil
    except ValueError as e:
        # Menampilkan pesan error jika ada input yang tidak valid
        messagebox.showerror("Input Error", str(e))  # Menampilkan kotak dialog error dengan pesan

# Membuat window utama
root = tk.Tk()  # Membuat jendela utama aplikasi
root.title("Aplikasi Prediksi Prodi Pilihan")  # Menentukan judul jendela

# Label judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))  # Membuat label judul
judul_label.grid(row=0, column=0, columnspan=2, pady=10)  # Menempatkan label di baris 0, merentang 2 kolom

# Membuat label dan entry untuk 10 nilai mata pelajaran
entry_labels = []  # List untuk menyimpan label
entries = []  # List untuk menyimpan input nilai

for i in range(10):  # Loop untuk membuat 10 label dan input
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i + 1}:")  # Membuat label nilai mata pelajaran
    label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="e")  # Menempatkan label di kolom 0
    entry_labels.append(label)  # Menambahkan label ke list

    entry = tk.Entry(root)  # Membuat kotak input
    entry.grid(row=i + 1, column=1, padx=10, pady=5)  # Menempatkan input di kolom 1
    entries.append(entry)  # Menambahkan input ke list

# Tombol untuk menampilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)  # Membuat tombol dengan fungsi hasil_prediksi
prediksi_button.grid(row=11, column=0, columnspan=2, pady=10)  # Menempatkan tombol di baris 11, merentang 2 kolom

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14))  # Membuat label kosong untuk hasil
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)  # Menempatkan label di baris 12, merentang 2 kolom

# Menjalankan aplikasi
root.mainloop()  # Memulai event loop untuk menangani interaksi pengguna
