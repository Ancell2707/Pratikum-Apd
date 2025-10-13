
kategori = ("Senar", "Tiup", "Perkusi", "Keyboard")

stok = [
    ["Gitar", 1500000, 5, 0],  # 0 = Senar
    ["Piano", 5000000, 2, 3],  # 3 = Keyboard
    ["Drum", 3000000, 3, 2],   # 2 = Perkusi
    ["Saxophone", 2500000, 1, 1]  # 1 = Tiup
]


while True:
    print("\n=== SELAMAT DATANG DI TOKO ALAT MUSIK ===")
    print("1. Masuk sebagai User (Lihat Katalog) - Akses Terbatas")
    print("2. Masuk sebagai Admin (Kelola Stok) - Akses Penuh")
    print("3. Keluar")
    
    role_pilihan = input("Pilih role (1-3): ")
    
    if role_pilihan == "1":
        while True:
            print("\n--- MENU USER (Pengguna) ---")
            print("1. Tampilkan Stok")
            print("2. Cari Item Berdasarkan Kategori")
            print("3. Kembali ke Menu Utama")
            
            user_pilihan = input("Pilih menu (1-3): ")
            
            if user_pilihan == "1":
                print("\n--- Daftar Stok (Hanya Lihat) ---")
                for i in range(len(stok)):
                    item = stok[i]
                    nama = item[0]
                    harga = item[1]
                    jumlah = item[2]
                    kat_idx = item[3]
                    kat_nama = kategori[kat_idx]
                    print(f"Nama: {nama}, Harga: Rp{harga}, Stok: {jumlah}, Kategori: {kat_nama}")
            
            elif user_pilihan == "2":
                print("\nContoh: Kategori Senar dan Tiup (indeks 0:2)")
                # Buat list baru dengan slicing kondisi (potong berdasarkan kat_idx 0 sampai <2)
                hasil = []
                for i in range(len(stok)):
                    if 0 <= stok[i][3] < 2:  # Logika slicing: start=0, stop=2, step=1 implisit
                        hasil.append(stok[i])
                # Tampilkan hasil dengan perulangan for
                if len(hasil) > 0:
                    for item in hasil:
                        nama = item[0]
                        kat_idx = item[3]
                        kat_nama = kategori[kat_idx]
                        print(f"Nama: {nama}, Kategori: {kat_idx} ({kat_nama})")
                else:
                    print("Tidak ada item di kategori tersebut.")
            
            elif user_pilihan == "3":
                print("Kembali ke menu utama (bisa switch ke Admin).")
                break
            
            else:
                print("Pilihan tidak valid! Coba lagi.")
    
    elif role_pilihan == "2":
        
        while True:
            print("\n--- MENU ADMIN ---")
            print("1. Tampilkan Stok")
            print("2. Tambah Item Baru")
            print("3. Ubah Stok Item")
            print("4. Hapus Item")
            print("5. Cari Item Berdasarkan Kategori")
            print("6. Kembali ke Menu Utama (Switch Role)")
            
            admin_pilihan = input("Pilih menu (1-6): ")
            
            if admin_pilihan == "1":
                print("\n--- Daftar Stok ---")
                for i in range(len(stok)):
                    item = stok[i]
                    nama = item[0]
                    harga = item[1]
                    jumlah = item[2]
                    kat_idx = item[3]
                    kat_nama = kategori[kat_idx]
                    print(f"Nama: {nama}, Harga: Rp{harga}, Stok: {jumlah}, Kategori: {kat_nama}")
            
            elif admin_pilihan == "2":
                nama_baru = input("Nama alat musik: ")
                harga_baru = int(input("Harga: "))
                jumlah_baru = int(input("Jumlah stok: "))
                print("\n--- Kategori (0-3) ---")
                
                for i in range(len(kategori)):
                    print(f"{i}: {kategori[i]}")
                kat_idx = int(input("Indeks kategori: "))
                
                if 0 <= kat_idx < len(kategori):
                    stok.append([nama_baru, harga_baru, jumlah_baru, kat_idx])
                    print("Item ditambahkan!")
                else:
                    print("Indeks kategori tidak valid!")
            
            elif admin_pilihan == "3":
                # Ubah item (update list dengan indeks) - Hanya Admin
                if len(stok) > 0:
                    print("\n--- Daftar Stok Saat Ini (Indeks) ---")
                    for i in range(len(stok)):
                        print(f"{i}: {stok[i][0]}")
                    idx = int(input("Indeks item yang diubah: "))
                    if 0 <= idx < len(stok):
                        nama_lama = stok[idx][0]
                        stok_baru = int(input(f"Stok baru untuk {nama_lama}: "))
                        stok[idx][2] = stok_baru
                        print("Stok diubah!")
                    else:
                        print("Indeks tidak valid!")
                else:
                    print("Stok kosong!")
            
            elif admin_pilihan == "4":
                # Hapus item (delete list dengan del) - Hanya Admin
                nama_hapus = input("Nama item yang dihapus: ")
                ditemukan = False
                for i in range(len(stok)):
                    if stok[i][0].lower() == nama_hapus.lower():
                        del stok[i]
                        print("Item dihapus!")
                        ditemukan = True
                        break
                if not ditemukan:
                    print("Item tidak ditemukan!")
            
            elif admin_pilihan == "5":
                # Cari (sama seperti user) - Admin juga bisa
                print("\nContoh: Kategori Senar dan Tiup (indeks 0:2)")
                hasil = []
                for i in range(len(stok)):
                    if 0 <= stok[i][3] < 2:
                        hasil.append(stok[i])
                if len(hasil) > 0:
                    for item in hasil:
                        nama = item[0]
                        kat_idx = item[3]
                        kat_nama = kategori[kat_idx]
                        print(f"Nama: {nama}, Kategori: {kat_idx} ({kat_nama})")
                else:
                    print("Tidak ada item di kategori tersebut.")
            
            elif admin_pilihan == "6":
                print("Kembali ke menu utama (bisa switch ke User).")
                break
            
            else:
                print("Pilihan tidak valid! Coba lagi.")
    
    elif role_pilihan == "3":
        print("Terima kasih telah mengunjungi Toko Alat Musik!")
        break
    
    else:
        print("Pilihan role tidak valid! Coba lagi.")
