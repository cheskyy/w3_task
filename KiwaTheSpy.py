def geser_huruf(huruf, offset):  # fungsi untuk pesan
    """Geser huruf dengan offset tertentu."""  # Ini adalah dokumentasi fungsi yang menjelaskan bahwa fungsi ini mengganti huruf dengan offset tertentu.
    return chr((ord(huruf) - ord('A') + offset) % 26 + ord('A'))  # Menghitung huruf baru dengan menggeser huruf 'A' dan menambahkan offset, lalu mengubahnya kembali menjadi karakter.
def enkripsi_dekripsi_pesan(mode, pesan):  # Fungsi untuk enkripsi atau dekripsi pesan
    """Enkripsi atau dekripsi pesan berdasarkan mode."""  # Dokumen yang menjelaskan bahwa fungsi ini melakukan enkripsi atau dekripsi.
    hasil = []  # Membuat list kosong untuk menyimpan hasil.
    offset = 5 if mode == 0 else -5  # Menentukan offset, 5 untuk enkripsi (mode 0) dan -5 untuk dekripsi (mode 1).
    for karakter in pesan:  # Loop untuk setiap karakter dalam pesan.
        if karakter.isalpha():  # Memeriksa apakah karakter adalah huruf.
            huruf_baru = geser_huruf(karakter, offset)  # Menggeser huruf menggunakan fungsi geser_huruf.
            hasil.append(huruf_baru)  # Menambahkan huruf baru ke list hasil.
        else:
            hasil.append(karakter)  # Menambahkan karakter non-huruf tanpa perubahan ke list hasil.
    return ''.join(hasil)  # Menggabungkan semua karakter dalam list hasil menjadi string dan mengembalikannya.
    """Fungsi utama untuk menjalankan program."""  # Dokumen yang menjelaskan bahwa ini adalah fungsi utama.
T = int(input("Masukkan jumlah percobaan: "))  # Meminta pengguna memasukkan jumlah percobaan.
for _ in range(T):  # Loop sebanyak T kali.
    mode = int(input("Masukkan mode (0 untuk enkripsi, 1 untuk dekripsi): "))  # Meminta pengguna memilih mode (enkripsi atau dekripsi).
    pesan = input("Masukkan pesan: ").strip()  # Meminta pengguna memasukkan pesan dan menghapus spasi di awal/akhir.
    print(enkripsi_dekripsi_pesan(mode, pesan))  # Memanggil fungsi enkripsi_dekripsi_pesan dan mencetak hasilnya.
