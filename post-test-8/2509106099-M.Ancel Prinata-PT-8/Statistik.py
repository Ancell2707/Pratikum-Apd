from prettytable import PrettyTable

try:
    from Stok_Manager import stok
except ImportError:
    print("Modul stok_manager tidak ditemukan. Menggunakan data default...")
from Stok_Manager import stok

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
        print(f"Terjadi kesalahan! Error: {e}")
        return {"total_nilai": 0, "jumlah_item": 0, "item_kosong": 0, "rata_rata": 0}

def tampilkan_statistik_stok():
    """
    Prosedur tanpa parameter untuk menampilkan statistik stok dalam bentuk tabel
    """
    try:
        statistik = hitung_total_nilai_stok()
        kategori_count = {}
        
        for key in stok:
            kat = stok[key]["kategori"]
            kategori_count[kat] = kategori_count.get(kat, 0) + 1
        
        # Tabel statistik utama
        table_main = PrettyTable()
        table_main.field_names = ["Metrik", "Nilai"]
        table_main.add_row(["Total Nilai Stok", f"Rp{statistik['total_nilai']:,.2f}"])
        table_main.add_row(["Jumlah Item Tersedia", statistik['jumlah_item']])
        table_main.add_row(["Item Habis", statistik['item_kosong']])
        table_main.add_row(["Rata-rata Nilai per Item", f"Rp{statistik['rata_rata']:,.2f}"])
        table_main.title = "STATISTIK STOK"
        
        # Tabel distribusi kategori
        table_kategori = PrettyTable()
        table_kategori.field_names = ["Kategori", "Jumlah Item"]
        for kat, count in kategori_count.items():
            table_kategori.add_row([kat, count])
        table_kategori.title = "DISTRIBUSI ITEM PER KATEGORI"
        
        return table_main, table_kategori
        
    except Exception as e:
        error_table = PrettyTable()
        error_table.field_names = ["Error"]
        error_table.add_row([f"Terjadi kesalahan! Error: {e}"])
        return error_table, None