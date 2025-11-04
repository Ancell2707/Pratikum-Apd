from prettytable import PrettyTable

kategori = {"Senar", "Tiup", "Perkusi", "Keyboard"}
stok = {
    1: {"nama": "Gitar", "harga": 1500000, "jumlah": 5, "kategori": "Senar"},
    2: {"nama": "Piano", "harga": 5000000, "jumlah": 2, "kategori": "Keyboard"},
    3: {"nama": "Drum", "harga": 3000000, "jumlah": 3, "kategori": "Perkusi"},
    4: {"nama": "Saxophone", "harga": 2500000, "jumlah": 1, "kategori": "Tiup"}
}
pesan_error = "Terjadi kesalahan! Silakan coba lagi."

def tampilkan_semua_stok():
    """Menampilkan semua stok dalam bentuk tabel"""
    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Harga", "Stok", "Kategori"]
    
    for key, item in stok.items():
        table.add_row([key, item["nama"], f"Rp{item['harga']:,}", item["jumlah"], item["kategori"]])
    
    table.title = "DAFTAR STOK ALAT MUSIK"
    return table

def tampilkan_item_berdasarkan_kategori(kategori_cari):
    """
    Fungsi dengan parameter untuk menampilkan item berdasarkan kategori
    Mengembalikan tabel PrettyTable
    """
    try:
        table = PrettyTable()
        table.field_names = ["Nama", "Harga", "Stok", "Kategori"]
        table.title = f"ITEM KATEGORI {kategori_cari.upper()}"
        
        hasil_ditemukan = False
        for key in stok:
            if stok[key]["kategori"].lower() == kategori_cari.lower():
                item = stok[key]
                table.add_row([item["nama"], f"Rp{item['harga']:,}", item["jumlah"], item["kategori"]])
                hasil_ditemukan = True
        
        return table if hasil_ditemukan else None
        
    except Exception as e:
        print(f"{pesan_error} Error: {e}")
        return None

def tambah_item(nama, harga, jumlah, kategori_item):
    """Menambahkan item baru ke stok"""
    try:
        next_id = max(stok.keys()) + 1 if stok else 1
        stok[next_id] = {
            "nama": nama,
            "harga": harga,
            "jumlah": jumlah,
            "kategori": kategori_item
        }
        return True, f"Item '{nama}' berhasil ditambahkan dengan ID {next_id}"
    except Exception as e:
        return False, f"{pesan_error} Error: {e}"

def update_stok(id_item, stok_baru):
    """Mengupdate stok item"""
    try:
        if id_item in stok:
            nama_lama = stok[id_item]["nama"]
            stok[id_item]["jumlah"] = stok_baru
            return True, f"Stok '{nama_lama}' berhasil diubah menjadi {stok_baru}"
        else:
            return False, "ID item tidak ditemukan"
    except Exception as e:
        return False, f"{pesan_error} Error: {e}"

def hapus_item(nama_hapus):
    """Menghapus item berdasarkan nama"""
    try:
        for key in list(stok.keys()):
            if stok[key]["nama"].lower() == nama_hapus.lower():
                nama_item = stok[key]["nama"]
                del stok[key]
                return True, f"Item '{nama_item}' berhasil dihapus"
        return False, f"Item dengan nama '{nama_hapus}' tidak ditemukan"
    except Exception as e:
        return False, f"{pesan_error} Error: {e}"

def get_kategori_list():
    """Mengembalikan list kategori yang tersedia"""
    return list(kategori)

def get_stok():
    """Mengembalikan dictionary stok"""
    return stok

def item_exists(id_item):
    """Memeriksa apakah item dengan ID tertentu exists"""
    return id_item in stok