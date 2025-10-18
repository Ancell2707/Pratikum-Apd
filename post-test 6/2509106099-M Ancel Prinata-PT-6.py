import os

kategori = {"Senar", "Tiup", "Perkusi", "Keyboard"}

kategori_list = list(kategori)

spasi = f'||{' ' * 54}||'
atap = '_'*58
lantai = '||' + '_'*54 + '||'

stok = {
    1: {"nama": "Gitar", "harga": 1500000, "jumlah": 5, "kategori": "Senar"},
    2: {"nama": "Piano", "harga": 5000000, "jumlah": 2, "kategori": "Keyboard"},
    3: {"nama": "Drum", "harga": 3000000, "jumlah": 3, "kategori": "Perkusi"},
    4: {"nama": "Saxophone", "harga": 2500000, "jumlah": 1, "kategori": "Tiup"}
}



while True:
    os.system('cls || clear')
    print(atap)
    print("||          SELAMAT DATANG DI TOKO ALAT MUSIK           ||")
    print(spasi)
    print("||1. Masuk sebagai User (Lihat Katalog) - Akses Terbatas||")
    print("||2. Masuk sebagai Admin (Kelola Stok) - Akses Penuh    ||")
    print("||3. Keluar                                             ||")
    print(lantai)
    
    role_pilihan = input("\nPilih role (1-3): ")
    
    if role_pilihan == "1":
        while True:
            os.system('cls || clear')
            print(atap)
            print(f"||{'MENU USER (Pengguna)':^{54}}||")
            print(spasi)
            print(f"||{'1.Tampilkan Stock':<{54}}||")
            print(f"||{'2. Cari Item Berdasarkan Kategori':<{54}}||")
            print(f"||{'3. Kembali ke Menu Utama':<{54}}||")
            print(lantai)
            print()
            
            
            user_pilihan = input("Pilih menu (1-3): ")
            
            if user_pilihan == "1":
                os.system('cls || clear')
                print(atap)
                print(f"||{'Daftar Stok (Hanya Lihat)':^{54}}||")
                print(lantai)
                for key in stok:
                    item = stok[key]
                    print(f"Nama: {item['nama']}, Harga: Rp{item['harga']}, Stok: {item['jumlah']}, Kategori: {item['kategori']}")
                input("Enter untuk ulang...")
            
            elif user_pilihan == "2":
                print("\nKategori tersedia:", kategori_list)
                cari_kat = input("Masukkan nama kategori yang ingin dicari: ").capitalize()
                hasil = []
                for key in stok:
                    if stok[key]["kategori"] == cari_kat:
                        hasil.append(stok[key])
                if len(hasil) > 0:
                    for item in hasil:
                        print(f"Nama: {item['nama']}, Kategori: {item['kategori']}")
                    input("Enter untuk ulang...")
                else:
                    print("Tidak ada item di kategori tersebut.")
                    input("Enter untuk ulang...")
            
            elif user_pilihan == "3":
                print("Kembali ke menu utama (bisa switch ke Admin).")
                break
            
            else:
                print("Pilihan tidak valid! Coba lagi.")
                input("Enter untuk ulang...")
    
    elif role_pilihan == "2":
        while True:
            os.system('cls || clear')
            print(atap)
            print(f"||{'MENU ADMIN ':^{54}}||")
            print(spasi)
            print(f"||{'1. Tampilkan Stok':<{54}}||")
            print(f"||{'2. Tambah Item Baru':<{54}}||")
            print(f"||{'3. Ubah Stok Item':<{54}}||")
            print(f"||{'4. Hapus Item':<{54}}||")
            print(f"||{'5. Cari Item Berdasarkan Kategori':<{54}}||")
            print(f"||{'6. Kmebali Kemenu Utama (Swite Role)':<{54}}||")
            print(lantai)
            print()
            
            admin_pilihan = input("Pilih menu (1-6): ")
            
            if admin_pilihan == "1":
                os.system('cls || clear')
                print(atap)
                print(f"||{'Daftar Stok ':^{54}}||")
                print(lantai)
                for key in stok:
                    item = stok[key]
                    print(f"{key}. Nama: {item['nama']}, Harga: Rp{item['harga']}, Stok: {item['jumlah']}, Kategori: {item['kategori']}")
                input("Enter untuk ulang...")
            
            elif admin_pilihan == "2":
                os.system('cls || clear')
                nama_baru = input("Nama alat musik: ")
                harga_baru = int(input("Harga: "))
                jumlah_baru = int(input("Jumlah stok: "))
                
                print()
                print(atap)
                print(f"||{'Kategori ':^{54}}||")
                print(lantai)
                for kat in kategori_list:
                    print("-", kat)
                print()
                kat_baru = input("Masukkan kategori: ").capitalize()
                
                if kat_baru in kategori:
                    next_id = max(stok.keys()) + 1 if stok else 1
                    stok[next_id] = {
                        "nama": nama_baru,
                        "harga": harga_baru,
                        "jumlah": jumlah_baru,
                        "kategori": kat_baru
                    }
                    print()
                    print("Item ditambahkan!")
                    input("Enter untuk ulang...")
                else:
                    print("Kategori tidak valid!")
                    input("Enter untuk ulang...")
            
            elif admin_pilihan == "3":
                if len(stok) > 0:
                    os.system('cls || clear')
                    print(atap)
                    print(f"||{'Print Stok Saat Ini ':^{54}}||")
                    print(lantai)
                    for key in stok:
                        print(f"{key}: {stok[key]['nama']}")
                    idx = int(input("Indeks item yang diubah: "))
                    if idx in stok:
                        nama_lama = stok[idx]["nama"]
                        stok_baru = int(input(f"Stok baru untuk {nama_lama}: "))
                        stok[idx]["jumlah"] = stok_baru
                        print("Stok diubah!")
                        input("Enter untuk ulang...")
                    else:
                        print("Indeks tidak valid!")
                        input("Enter untuk ulang...")
                else:
                    print("Stok kosong!")
                    input("Enter untuk ulang...")
            
            elif admin_pilihan == "4":
                nama_hapus = input("Nama item yang dihapus: ")
                ditemukan = False
                for key in list(stok.keys()):
                    if stok[key]["nama"].lower() == nama_hapus.lower():
                        del stok[key]
                        print("Item dihapus!")
                        ditemukan = True
                        input("Enter untuk ulang...")
                        break
                if not ditemukan:
                   
                    print(atap)
                    print(f"||{'Item Tidak Di Temukan ':^{54}}||")
                    print(lantai)
                    input("Enter untuk ulang...")
            
            elif admin_pilihan == "5":
                print("\nKategori tersedia:", kategori_list)
                cari_kat = input("Masukkan nama kategori: ").capitalize()
                print()
                hasil = []
                for key in stok:
                    if stok[key]["kategori"] == cari_kat:
                        hasil.append(stok[key])
                if len(hasil) > 0:
                    for item in hasil:
                        print(f"Nama: {item['nama']}, Kategori: {item['kategori']}")
                    input("Enter untuk ulang...")
                else:
                    print("Tidak ada item di kategori tersebut.")
                    input("Enter untuk ulang...")
            
            elif admin_pilihan == "6":
                print("Kembali ke menu utama (bisa switch ke User).")
                break
            
            else:
                print("Pilihan tidak valid! Coba lagi.")
                input("Enter untuk ulang...")
    
    elif role_pilihan == "3":
        print("Terima kasih telah mengunjungi Toko Alat Musik!")
        break
    
    else:
        print("Pilihan role tidak valid! Coba lagi.")
        input("Enter untuk ulang...")