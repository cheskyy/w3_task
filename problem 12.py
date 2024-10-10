def pecahkan_pesan(string, n, angka):
  """
  Fungsi untuk memecahkan pesan berdasarkan indeks yang diberikan.
  Args:
    string: String utama yang berisi pesan terenkripsi.
    n: Jumlah angka indeks.
    angka: List berisi angka-angka indeks.
  Returns:
    String: Pesan yang sudah dipecahkan.
  """
  pesan_asli = ""
  for i in angka:
    # Karena indeks dimulai dari 0, kita kurangkan 1 dari angka
    pesan_asli += string[i-1]
  return pesan_asli
# Input
string_utama = input("Masukkan string utama: ")
jumlah_angka = int(input("Masukkan jumlah angka: "))
angka_indeks = list(map(int, input("Masukkan angka-angka (pisahkan dengan spasi): ").split()))
# Panggil fungsi dan cetak hasil
hasil = pecahkan_pesan(string_utama, jumlah_angka, angka_indeks)
print("Pesan asli:", hasil)