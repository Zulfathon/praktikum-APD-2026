barang_1 = 15000
barang_2 = 25000
barang_3 = 10000
barang_4 = 5500
barang_5 = 5000
barang_6 = 20000
daftar_barang = [barang_1, barang_2, barang_3, barang_4, barang_5, barang_6]
nim = 16

total_belanjaan = barang_1 + barang_2 + barang_3 + barang_4 + barang_5 + barang_6
pajak = 0.15 * total_belanjaan
total_bayar = total_belanjaan + pajak
rata_rata = total_bayar / len(daftar_barang)
bolean = nim < rata_rata

print("Hasil Perhitungan Koperasi Desa Merah Putih")
print()
print("Harga Barang 1 :", barang_1)
print("Harga Barang 2 :", barang_2)
print("Harga Barang 3 :", barang_3)
print("Harga Barang 4 :", barang_4)
print("Harga Barang 5 :", barang_5)
print("Harga Barang 6 :", barang_6)
print("Total belanjaan :", total_belanjaan)
print("Pajak :", pajak)
print("Daftar Barang :", daftar_barang)
print("Total Bayar :", total_bayar)
print("Rata-Rata Harga :", rata_rata)
print("NIM :", nim)
print("Status Boolean :", bolean)