from prettytable import PrettyTable

def tampilkan_menu():
    tabel = PrettyTable()
    tabel.field_names = ["Pilihan", " SELAMAT DATANG DI TOKO ALAT MUSIK"]

    tabel.add_row(["1", "Masuk sebagai User (Lihat Katalog) - Akses Terbatas"])
    tabel.add_row(["2", "Masuk sebagai Admin (Kelola Stok) - Akses Penuh"])
    tabel.add_row(["3", "Keluar"])

    
    return tabel
def menu_user():
 

    table = PrettyTable()
    table.field_names = ["Pilihan", "MENU USER (Pengguna)"]

    table.add_row(["1", "Tampilkan Stok"])
    table.add_row(["2", "Cari Item Berdasarkan Kategori"])
    table.add_row(["3", "Lihat Statistik Stok"])
    table.add_row(["4", "Kembali ke Menu Utama"])

    return table

def menu_admin():
    

    table = PrettyTable()
    table.field_names = ["Pilihan", "MENU ADMIN"]

    table.add_row(["1", "Tampilkan Stok"])
    table.add_row(["2", "Tambah Item Baru"])
    table.add_row(["3", "Ubah Stok Item"])
    table.add_row(["4", "Hapus Item"])
    table.add_row(["5", "Cari Item Berdasarkan Kategori"])
    table.add_row(["6", "Lihat Statistik Stok"])
    table.add_row(["7", "Kembali ke Menu Utama"])

    return table
def tampilkan_header(judul):
    """
    Prosedur dengan parameter untuk menampilkan header
    """
  
    atap = '_'*58
    spasi = f'||{' ' * 54}||'
    lantai = '||' + '_'*54 + '||'
    
    print(atap)
    print(f"||{judul:^{54}}||")
    print(spasi)


