nama = str(input("Masukan nama anda: "))
nim = str(input("Masukan NIM anda: "))
hargaLaptop = int(input("Masukan harga laptop anda: "))

print(f"\n{nama} dengan NIM {nim} ingin membeli laptop seharga {hargaLaptop:,}".replace(',', '.'))


hargaLenovo = int(hargaLaptop - (hargaLaptop * 0.10))
hargaAsus = int(hargaLaptop - (hargaLaptop * 0.07))
hargaAcer = int(hargaLaptop - (hargaLaptop * 0.05))


print(f"\nHarga Lenovo setelah diskon 10% : {hargaLenovo:,}".replace(',', '.'))
print(f"Harga Asus setelah diskon 7%  : {hargaAsus:,}".replace(',', '.'))
print(f"Harga Acer setelah diskon 5% : {hargaAcer:,}".replace(',', '.'))