import os
from menu import tampilkan_menu, menu_user, menu_admin, tampilkan_header
from Stok_Manager import (
    tampilkan_semua_stok, tampilkan_item_berdasarkan_kategori, 
    tambah_item, update_stok, hapus_item, get_kategori_list, 
    get_stok, item_exists
)
from Statistik import tampilkan_statistik_stok

pesan_error = "Terjadi kesalahan! Silakan coba lagi."

def clear_screen():
    """Membersihkan layar"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        try:
            clear_screen()
            print(tampilkan_menu())
            
            role_pilihan = input("\nPilih role (1-3): ")
            
            if role_pilihan == "1":
                menu_user_handler()
            elif role_pilihan == "2":
                menu_admin_handler()
            elif role_pilihan == "3":
                print("Terima kasih telah mengunjungi Toko Alat Musik!")
                break
            else:
                print("Pilihan role tidak valid! Coba lagi.")
                input("\nEnter untuk melanjutkan...")
        
        except Exception as e:
            print(f"{pesan_error} Error: {e}")
            input("\nEnter untuk melanjutkan...")

def menu_user_handler():
    """Handler untuk menu user"""
    while True:
        try:
            clear_screen()
            print(menu_user())
            user_pilihan = input("Pilih menu (1-4): ")
            
            if user_pilihan == "1":
                clear_screen()
                print(tampilkan_semua_stok())
                input("\nEnter untuk kembali...")
            
            elif user_pilihan == "2":
                try:
                    clear_screen()
                    kategori_list = get_kategori_list()
                    print("Kategori tersedia:", kategori_list)
                    cari_kat = input("Masukkan nama kategori yang ingin dicari: ").capitalize()
                    
                    hasil = tampilkan_item_berdasarkan_kategori(cari_kat)
                    if hasil:
                        print(hasil)
                    else:
                        print("Tidak ada item di kategori tersebut.")
                    input("\nEnter untuk kembali...")
                except Exception as e:
                    print(f"{pesan_error} Error: {e}")
                    input("\nEnter untuk kembali...")
            
            elif user_pilihan == "3":
                clear_screen()
                table_main, table_kategori = tampilkan_statistik_stok()
                print(table_main)
                if table_kategori:
                    print("\n" + str(table_kategori))
                input("\nEnter untuk kembali...")
            
            elif user_pilihan == "4":
                print("Kembali ke menu utama...")
                break
            
            else:
                print("Pilihan tidak valid! Coba lagi.")
                input("\nEnter untuk kembali...")
        
        except Exception as e:
            print(f"{pesan_error} Error: {e}")
            input("\nEnter untuk kembali...")

def menu_admin_handler():
    """Handler untuk menu admin"""
    while True:
        try:
            clear_screen()
            print(menu_admin())
            admin_pilihan = input("Pilih menu (1-7): ")
            
            if admin_pilihan == "1":
                clear_screen()
                print(tampilkan_semua_stok())
                input("\nEnter untuk kembali...")
            
            elif admin_pilihan == "2":
                try:
                    clear_screen()
                    tampilkan_header("TAMBAH ITEM BARU")
                    
                    nama_baru = input("Nama alat musik: ")
                    if not nama_baru:
                        raise ValueError("Nama tidak boleh kosong!")
                    
                    harga_baru = int(input("Harga: "))
                    if harga_baru <= 0:
                        raise ValueError("Harga harus lebih dari 0!")
                    
                    jumlah_baru = int(input("Jumlah stok: "))
                    if jumlah_baru < 0:
                        raise ValueError("Jumlah stok tidak boleh negatif!")
                    
                    print("\nKategori Tersedia:")
                    for kat in get_kategori_list():
                        print("-", kat)
                    print()
                    
                    kat_baru = input("Masukkan kategori: ").capitalize()
                    
                    if kat_baru in get_kategori_list():
                        success, message = tambah_item(nama_baru, harga_baru, jumlah_baru, kat_baru)
                        print(f"\n{message}")
                    else:
                        print("Kategori tidak valid!")
                    input("\nEnter untuk kembali...")
                
                except ValueError as ve:
                    print(f"Input tidak valid: {ve}")
                    input("\nEnter untuk kembali...")
                except Exception as e:
                    print(f"{pesan_error} Error: {e}")
                    input("\nEnter untuk kembali...")
            
            elif admin_pilihan == "3":
                try:
                    clear_screen()
                    if get_stok():
                        print(tampilkan_semua_stok())
                        
                        idx = int(input("\nID item yang akan diubah stok: "))
                        if item_exists(idx):
                            stok_baru = int(input(f"Stok baru: "))
                            if stok_baru < 0:
                                raise ValueError("Stok tidak boleh negatif!")
                            
                            success, message = update_stok(idx, stok_baru)
                            print(f"\n{message}")
                        else:
                            print("ID item tidak valid!")
                    else:
                        print("Stok kosong!")
                    input("\nEnter untuk kembali...")
                
                except ValueError as ve:
                    print(f"Input tidak valid: {ve}")
                    input("\nEnter untuk kembali...")
                except Exception as e:
                    print(f"{pesan_error} Error: {e}")
                    input("\nEnter untuk kembali...")
            
            elif admin_pilihan == "4":
                try:
                    clear_screen()
                    if get_stok():
                        print(tampilkan_semua_stok())
                        
                        nama_hapus = input("\nNama item yang akan dihapus: ")
                        
                        success, message = hapus_item(nama_hapus)
                        print(f"\n{message}")
                    else:
                        print("Stok kosong!")
                    input("\nEnter untuk kembali...")
                
                except Exception as e:
                    print(f"{pesan_error} Error: {e}")
                    input("\nEnter untuk kembali...")
            
            elif admin_pilihan == "5":
                try:
                    clear_screen()
                    kategori_list = get_kategori_list()
                    print("Kategori tersedia:", kategori_list)
                    cari_kat = input("Masukkan nama kategori: ").capitalize()
                    
                    hasil = tampilkan_item_berdasarkan_kategori(cari_kat)
                    if hasil:
                        print(hasil)
                    else:
                        print("Tidak ada item di kategori tersebut.")
                    input("\nEnter untuk kembali...")
                except Exception as e:
                    print(f"{pesan_error} Error: {e}")
                    input("\nEnter untuk kembali...")
            
            elif admin_pilihan == "6":
                clear_screen()
                table_main, table_kategori = tampilkan_statistik_stok()
                print(table_main)
                if table_kategori:
                    print("\n" + str(table_kategori))
                input("\nEnter untuk kembali...")
            
            elif admin_pilihan == "7":
                print("Kembali ke menu utama...")
                break
            
            else:
                print("Pilihan tidak valid! Coba lagi.")
                input("\nEnter untuk kembali...")
        
        except Exception as e:
            print(f"{pesan_error} Error: {e}")
            input("\nEnter untuk kembali...")

if __name__ == "__main__":
    main()