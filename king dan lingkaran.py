print("masukkan bilangan dengan spasi :")
x1, y1 = map(int, input() .split( )) #membaca input dari pengguna, memisahkan bilangan yang dimasukkan berdasarkan spasi, dan mengonversinya menjadi tipe int. Nilai pertama disimpan di variabel x1 dan nilai kedua di y1.
xs, ys = map(int, input() .split( )) #baris ini membaca input kedua dari pengguna dan menyimpannya dalam variabel xs dan ys.
xf, yf = map(int, input() .split( )) #input ketiga. Nilai disimpan dalam variabel xf dan yf.
j_sf = ((xf - xs)**2 + (yf - ys)**2) #menghitung jarak kuadrat antara titik (xs, ys) dan (xf, yf) menggunakan rumus jarak Euclidean. Hasilnya disimpan dalam variabel j_sf.
j_If = ((xf - x1)**2 + (yf - y1)**2) #menghitung jarak kuadrat antara titik (x1, y1) dan (xf, yf), lalu menyimpannya dalam variabel j_If.
if j_If > j_sf: #memeriksa apakah jarak kuadrat dari titik (x1, y1) ke (xf, yf) lebih besar daripada jarak kuadrat dari (xs, ys) ke (xf, yf).
    print("Yes")
else: #bagian dari struktur kontrol yang menyatakan bahwa jika kondisi sebelumnya tidak terpenuhi, maka program akan menjalankan perintah
    print("No") #kondisi di atas salah (jarak j_If tidak lebih besar), maka program mencetak "No".
