 #LOGIN
MasukanName = "Muhammad Ancel Prinata"
MasukanNim = 2509106099

NamaLengkap = input('Masukan Nama Lengkap Anda:')
NIM = int(input('Masukan Nim Anda: '))
if NamaLengkap == MasukanName and NIM == MasukanNim:
    print("Login anda berhasil")

    print('silahkan pilih opsi dibawah ini')
    print('Harga semua Paket adalah Rp.1.500.000')
    print('1. Paket Bronze : Biaya administrasi 1%, akses dasar ke lagu-lagu populer.')
    print('2.Paket Silver  : Biaya administrasi 3%, akses lagu premium dan playlist kustom.')
    print('3.Paket Gold    : Biaya administrasi 5%, akses lagu premium, playlist kustom, dan mode offline.')
    print('4.Paket Platinum: Biaya administrasi 7%, akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis.')
    BiayaLangganan = 1500000
    input_paket = input("pilih paket yang anda inginkan (1-4)")

# PaketB = input("apakah anda ingin membeli paket B")
# PaketS = input("Apakah anda ingin membeli paket S")
# PaketG = input("Apakah anda ingin membeli paket G")
# PaketP = input("Apakah anda ingin membeli paket P")

# totalB = BiayaLangganan+(BiayaLangganan * 0.01)
# totalS = BiayaLangganan+(BiayaLangganan * 0.03)
# totalG = BiayaLangganan+(BiayaLangganan * 0.05)
# totalP = BiayaLangganan+(BiayaLangganan * 0.07)


# ya = True
# tidak =not ya


    if input_paket == "1":
        biaya_administrasi = 0.01
        paket = "bronze"
        fitur_akses = "lagu-lagu populer"
    elif input_paket == "2":
        paket = "silver"
        biaya_administrasi = 0.03
        fitur_akses = "akses lagu premium dan playlist kustom"
    elif input_paket == "3":
        paket = "gold"
        biaya_administrasi = 0.05
        fitur_akses = "akses lagu premium, playlist kustom, dan mode offline"
    elif input_paket == "4":
        paket = "platinum"
        biaya_administrasi = 0.07
        fitur_akses = "akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis"
    else:
        print('Pilihan input tidak tersedia')
    total_biaya = BiayaLangganan + (BiayaLangganan * biaya_administrasi)
    print("Nama               :", NamaLengkap)
    print("nim                :",NIM)
    print("paket yang dipilih :",paket)
    print("fitur yang di dapat:",fitur_akses)
    print(f"total yang dibayar : Rp {total_biaya:,.0f}")

else:
    print("username/NIM anda salah silahkan coba lagi ")
exit()
        