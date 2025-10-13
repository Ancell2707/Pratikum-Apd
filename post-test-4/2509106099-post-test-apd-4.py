name = "Ancel"
nim = "2509106099"
percobaan = 0
total = 0

while percobaan < 3:
    Masukan_name = input(" Masukan nama Beliau : ")
    password     = input(" Masukan Password (nim) : ") 

    if Masukan_name == name and password == nim:
        print(" Selamat Login Anda Berhasil ")
        Login_Berhasil = "GAS KUYY PESAN"
        while True:
            print(" === MENU PILIHAN TIKET BIOSKOP XXI === ")
            print(" 1. Tiket Reguler  - Rp 50.000  ")
            print(" 2. Tiket VIP      - Rp 100.000 ")
            print(" 3. Tiket VVIP     - Rp 150.000 ")
            print(" 4. Keluar                       ")
            pilihan = input("Silahkan pilih Tiket yang anda mau ")
            if pilihan =="4":
                print("Terima kasih Telah menggunakan layanan ini")
                break

            

            if pilihan == "1":
                jenis  = "Reguler"
                harga  = 50000
                
            elif pilihan == "2":
                jenis    = "VIP"
                harga    = 100000

            else:
                jenis    = "VVIP"
                harga    = 150000
            jumlah_Tiket =int(input(" Masukan Jumlah Tiket Yang mau Bestie Beli "))
            confirmasi = input("Apakah ingin Lanjut membeli tiket ")
            if confirmasi == "ya":
                pass  
            elif confirmasi == "tidak":     

                for w in range (jumlah_Tiket):
                    total += harga

                    print(" ===  STRUK PEMBELIAN === ")
                    print(" Jenis Tiket yang Bestie Beli : ", jenis)
                    print(" Jumlah Tiket Yang mau Bestie Beli :", jumlah_Tiket)
                    print("Total Harga Yang Harus Bestie Bayar :",total)
                    print(" ========================================= ")
                break
        break        
            
    else:
        percobaan += 1
        print(" EAA LOGIN ANDA GAGAL ")
        print(" UPSS!!! Terlalu Banyak Percobaan: ",percobaan)
        print(" -------------------- ")










