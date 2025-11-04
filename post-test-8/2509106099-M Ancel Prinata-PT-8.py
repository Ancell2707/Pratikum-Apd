import os

from menu import tampilkan_menu,menu_user,menu_admin,tampilkan_header


kategori = {"Senar", "Tiup", "Perkusi", "Keyboard"}
stok = {
    1: {"nama": "Gitar", "harga": 1500000, "jumlah": 5, "kategori": "Senar"},
    2: {"nama": "Piano", "harga": 5000000, "jumlah": 2, "kategori": "Keyboard"},
    3: {"nama": "Drum", "harga": 3000000, "jumlah": 3, "kategori": "Perkusi"},
    4: {"nama": "Saxophone", "harga": 2500000, "jumlah": 1, "kategori": "Tiup"}
}
pesan_error = "Terjadi kesalahan! Silakan coba lagi."


def tampilkan_item_berdasarkan_kategori(kategori_cari):
    """
    Fungsi dengan parameter untuk menampilkan item berdasarkan kategori
    """
    try:
        hasil = []
        for key in stok:
            if stok[key]["kategori"] == kategori_cari:
                hasil.append(stok[key])
        return hasil
    except Exception as e:
        print(f"{pesan_error} Error: {e}")
        return []

def hitung_total_nilai_stok(include_out_of_stock=True):
    """
    Fungsi tanpa parameter untuk menghitung total nilai stok
    """
    try:
        total_nilai = 0
        jumlah_item = 0
        item_kosong = 0
        
        for key in stok:
            item = stok[key]
            nilai_item = item["harga"] * item["jumlah"]
            
            if item["jumlah"] > 0:
                total_nilai += nilai_item
                jumlah_item += 1
            else:
                item_kosong += 1
                if include_out_of_stock:
                    total_nilai += nilai_item
        
        rata_rata = total_nilai / max(len(stok), 1)
        
        return {
            "total_nilai": total_nilai,
            "jumlah_item": jumlah_item,
            "item_kosong": item_kosong,
            "rata_rata": rata_rata
        }
    except Exception as e:
        print(f"{pesan_error} Error: {e}")
        return {"total_nilai": 0, "jumlah_item": 0, "item_kosong": 0, "rata_rata": 0}


def tampilkan_statistik_stok():
    """
    Prosedur tanpa parameter untuk menampilkan statistik stok
    """
    try:
        statistik = hitung_total_nilai_stok()
        kategori_count = {}
        
        for key in stok:
            kat = stok[key]["kategori"]
            kategori_count[kat] = kategori_count.get(kat, 0) + 1
        
        print("\n=== STATISTIK STOK ===")
        print(f"Total nilai stok: Rp{statistik['total_nilai']:,.2f}")
        print(f"Jumlah item: {statistik['jumlah_item']}")
        print(f"Item habis: {statistik['item_kosong']}")
        print(f"Rata-rata nilai per item: Rp{statistik['rata_rata']:,.2f}")
        print("\nItem per kategori:")
        for kat, count in kategori_count.items():
            print(f"- {kat}: {count} item")
    except Exception as e:
        print(f"{pesan_error} Error: {e}")

kategori_list = list(kategori)

while True:
    try:
        os.system('cls || clear')
        print(tampilkan_menu())
        
        role_pilihan = input("\nPilih role (1-3): ")
        
        if role_pilihan == "1":
            while True:
                try:
                    os.system('cls || clear')
                    print(menu_user())
                    user_pilihan = input("Pilih menu (1-4): ")
                    
                    if user_pilihan == "1":
                        os.system('cls || clear')
                        tampilkan_header("Daftar Stok (Hanya Lihat)")
                        for key in stok:
                            item = stok[key]
                            print(f"Nama: {item['nama']}, Harga: Rp{item['harga']}, Stok: {item['jumlah']}, Kategori: {item['kategori']}")
                        input("\nEnter untuk ulang...")
                    
                    elif user_pilihan == "2":
                        try:
                            print("\nKategori tersedia:", kategori_list)
                            cari_kat = input("Masukkan nama kategori yang ingin dicari: ").capitalize()
                            hasil = tampilkan_item_berdasarkan_kategori(cari_kat)
                            if len(hasil) > 0:
                                for item in hasil:
                                    print(f"Nama: {item['nama']}, Harga: Rp{item['harga']}, Stok: {item['jumlah']}, Kategori: {item['kategori']}")
                            else:
                                print("Tidak ada item di kategori tersebut.")
                            input("\nEnter untuk ulang...")
                        except Exception as e:
                            print(f"{pesan_error} Error: {e}")
                            input("\nEnter untuk ulang...")
                    
                    elif user_pilihan == "3":
                        tampilkan_statistik_stok()
                        input("\nEnter untuk ulang...")
                    
                    elif user_pilihan == "4":
                        print("Kembali ke menu utama (bisa switch ke Admin).")
                        break
                    
                    else:
                        print("Pilihan tidak valid! Coba lagi.")
                        input("\nEnter untuk ulang...")
                
                except Exception as e:
                    print(f"{pesan_error} Error: {e}")
                    input("\nEnter untuk ulang...")
        
        elif role_pilihan == "2":
            while True:
                try:
                    os.system('cls || clear')
                    print(menu_admin())
                    admin_pilihan = input("Pilih menu (1-7): ")
                    
                    if admin_pilihan == "1":
                        os.system('cls || clear')
                        tampilkan_header("Daftar Stok")
                        for key in stok:
                            item = stok[key]
                            print(f"{key}. Nama: {item['nama']}, Harga: Rp{item['harga']}, Stok: {item['jumlah']}, Kategori: {item['kategori']}")
                        input("\nEnter untuk ulang...")
                    
                    elif admin_pilihan == "2":
                        try:
                            os.system('cls || clear')
                            nama_baru = input("Nama alat musik: ")
                            if not nama_baru:
                                raise ValueError("Nama tidak boleh kosong!")
                            
                            harga_baru = int(input("Harga: "))
                            if harga_baru <= 0:
                                raise ValueError("Harga harus lebih dari 0!")
                            
                            jumlah_baru = int(input("Jumlah stok: "))
                            if jumlah_baru < 0:
                                raise ValueError("Jumlah stok tidak boleh negatif!")
                            
                            print()
                            tampilkan_header("Kategori Tersedia")
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
                                print("\nItem berhasil ditambahkan!")
                                input("Enter untuk ulang...")
                            else:
                                print("Kategori tidak valid!")
                                input("Enter untuk ulang...")
                        
                        except ValueError as ve:
                            print(f"Input tidak valid: {ve}")
                            input("Enter untuk ulang...")
                        except Exception as e:
                            print(f"{pesan_error} Error: {e}")
                            input("Enter untuk ulang...")
                    
                    elif admin_pilihan == "3":
                        try:
                            if len(stok) > 0:
                                os.system('cls || clear')
                                tampilkan_header("Stok Saat Ini")
                                for key in stok:
                                    print(f"{key}: {stok[key]['nama']} (Stok: {stok[key]['jumlah']})")
                                
                                idx = int(input("\nIndeks item yang diubah: "))
                                if idx in stok:
                                    nama_lama = stok[idx]["nama"]
                                    stok_baru = int(input(f"Stok baru untuk {nama_lama}: "))
                                    if stok_baru < 0:
                                        raise ValueError("Stok tidak boleh negatif!")
                                    
                                    stok[idx]["jumlah"] = stok_baru
                                    print("Stok berhasil diubah!")
                                else:
                                    print("Indeks tidak valid!")
                                input("\nEnter untuk ulang...")
                            else:
                                print("Stok kosong!")
                                input("\nEnter untuk ulang...")
                        
                        except ValueError as ve:
                            print(f"Input tidak valid: {ve}")
                            input("\nEnter untuk ulang...")
                        except Exception as e:
                            print(f"{pesan_error} Error: {e}")
                            input("\nEnter untuk ulang...")
                    
                    elif admin_pilihan == "4":
                        try:
                            if len(stok) > 0:
                                os.system('cls || clear')
                                tampilkan_header("Daftar Item")
                                for key in stok:
                                    print(f"{key}: {stok[key]['nama']}")
                                
                                nama_hapus = input("\nNama item yang dihapus: ")
                                ditemukan = False
                                
                                for key in list(stok.keys()):
                                    if stok[key]["nama"].lower() == nama_hapus.lower():
                                        konfirmasi = input(f"Yakin hapus {stok[key]['nama']}? (y/n): ").lower()
                                        if konfirmasi == 'y':
                                            del stok[key]
                                            print("Item berhasil dihapus!")
                                        else:
                                            print("Penghapusan dibatalkan.")
                                        ditemukan = True
                                        break
                                
                                if not ditemukan:
                                    tampilkan_header("Item Tidak Ditemukan")
                                input("\nEnter untuk ulang...")
                            else:
                                print("Stok kosong!")
                                input("\nEnter untuk ulang...")
                        
                        except Exception as e:
                            print(f"{pesan_error} Error: {e}")
                            input("\nEnter untuk ulang...")
                    
                    elif admin_pilihan == "5":
                        try:
                            print("\nKategori tersedia:", kategori_list)
                            cari_kat = input("Masukkan nama kategori: ").capitalize()
                            print()
                            hasil = tampilkan_item_berdasarkan_kategori(cari_kat)
                            if len(hasil) > 0:
                                for item in hasil:
                                    print(f"Nama: {item['nama']}, Harga: Rp{item['harga']}, Stok: {item['jumlah']}, Kategori: {item['kategori']}")
                            else:
                                print("Tidak ada item di kategori tersebut.")
                            input("\nEnter untuk ulang...")
                        except Exception as e:
                            print(f"{pesan_error} Error: {e}")
                            input("\nEnter untuk ulang...")
                    
                    elif admin_pilihan == "6":
                        tampilkan_statistik_stok()
                        input("\nEnter untuk ulang...")
                    
                    elif admin_pilihan == "7":
                        print("Kembali ke menu utama (bisa switch ke User).")
                        break
                    
                    else:
                        print("Pilihan tidak valid! Coba lagi.")
                        input("\nEnter untuk ulang...")
                
                except Exception as e:
                    print(f"{pesan_error} Error: {e}")
                    input("\nEnter untuk ulang...")
        
        elif role_pilihan == "3":
            print("Terima kasih telah mengunjungi Toko Alat Musik!")
            break
        
        else:
            print("Pilihan role tidak valid! Coba lagi.")
            input("\nEnter untuk ulang...")
    
    except Exception as e:
        print(f"{pesan_error} Error: {e}")
        input("\nEnter untuk ulang...")