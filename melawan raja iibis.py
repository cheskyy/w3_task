def ucup_menang(U, K, M): #Mendefinisikan fungsi ucup_menang yang menerima tiga parameter: U (HP Ucup), K (jumlah ksatria), dan M (jumlah minion).
    ap_ucup = 100 #mendefinisikn ap_ucup, yaitu attack power (daya serang) Ucup, yang bernilai 100.
    M_beku = M // 2 #Menghitung jumlah minion yang "beku" (setengah dari jumlah minion yang diberikan) dengan membagi M dengan 2.
    hp_minion = 100 #Mendefinisikan hp_minion, yaitu HP setiap minion, yang bernilai 100.
    damage_minion = M_beku * 2 * ( hp_minion / ap_ucup)
    #Menghitung total damage yang diberikan oleh minion dengan rumus:
    #Damage total = jumlah minion beku × 2 × (HP minion / attack power Ucup).
    K_beku = K // 2 #Menghitung jumlah ksatria yang "beku" (setengah dari jumlah ksatria yang diberikan) dengan membagi K dengan 2.
    hp_knight = 500 #mendefinisikan hp_knight, yaitu HP setiap ksatria, yang bernilai 500.
    damage_knight = K_beku * 5 * (hp_knight / ap_ucup) 
    #Menghitung total damage yang diberikan oleh ksatria dengan rumus:
    #Damage total = jumlah ksatria beku × 5 × (HP ksatria / attack power Ucup).
    hp_raja = 1000 #Mendefinisikan hp_raja, yaitu HP raja, yang bernilai 1000.
    damage_raja = 100 * ( hp_raja / ap_ucup) 
    #Menghitung damage yang diberikan oleh raja dengan rumus:
    #Damage = 100 × (HP raja / attack power Ucup).
    total_damage = damage_minion + damage_knight + damage_raja #Menghitung total damage yang diterima Ucup dengan menjumlahkan damage dari minion, ksatria, dan raja.
    U_tersisa = U - total_damage #Menghitung sisa HP Ucup setelah menerima total damage.
    if U_tersisa > 0: #Memeriksa apakah sisa HP Ucup masih positif.
        return f"Yey! Ucup Menang! HP tersisa: {int(U_tersisa)}" #jika sisa HP positif, mengembalikan pesan bahwa Ucup menang dan menunjukkan HP tersisa.
    else:
        return "Yah! Ucup Meninggoy." #jika sisa HP tidak positif, mengembalikan pesan bahwa Ucup kalah.

U = int(input())
K = int(input())
M = int(input())
print(ucup_menang(U, K, M))