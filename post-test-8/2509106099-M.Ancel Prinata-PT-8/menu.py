from prettytable import PrettyTable

def tampilkan_menu():
    """Menu utama untuk memilih role"""
    table = PrettyTable()
    table.field_names = ["Pilihan", "Role"]
    table.add_row(["1", "User"])
    table.add_row(["2", "Admin"])
    table.add_row(["3", "Keluar"])
    table.title = "SELAMAT DATANG DI TOKO ALAT MUSIK"
    return table

def menu_user():
    """Menu untuk user"""
    table = PrettyTable()
    table.field_names = ["Pilihan", "Menu"]
    table.add_row(["1", "Lihat Stok"])
    table.add_row(["2", "Cari Berdasarkan Kategori"])
    table.add_row(["3", "Statistik Stok"])
    table.add_row(["4", "Kembali ke Menu Utama"])
    table.title = "MENU USER"
    return table

def menu_admin():
    """Menu untuk admin"""
    table = PrettyTable()
    table.field_names = ["Pilihan", "Menu"]
    table.add_row(["1", "Lihat Stok"])
    table.add_row(["2", "Tambah Item"])
    table.add_row(["3", "Update Stok"])
    table.add_row(["4", "Hapus Item"])
    table.add_row(["5", "Cari Berdasarkan Kategori"])
    table.add_row(["6", "Statistik Stok"])
    table.add_row(["7", "Kembali ke Menu Utama"])
    table.title = "MENU ADMIN"
    return table

def tampilkan_header(judul):
    """Menampilkan header dengan PrettyTable"""
    table = PrettyTable()
    table.field_names = [judul]
    table.align = "l"
    print(table)