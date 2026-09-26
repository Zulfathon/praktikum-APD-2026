nama = input("Masukkan Nama: ")
umur = int(input("Masukkan Umur: "))

if umur < 13:
    print("Mohon maaf, anda belum cukup umur untuk menonton")
    exit()
else:
    print("Silahkan Pilih Jenis Tiket")
    print("1. Reguler")
    print("2. Premium")
    print("3. VIP")

    jenisTiket = input ("Masukkan Jenis Tiket (Reguler/Premium/VIP): ")
    if jenisTiket == "Reguler":
        hargaTiket = 50000
    elif jenisTiket == "Premium":
        hargaTiket = 75000
    elif jenisTiket == "VIP":
        hargaTiket = 100000
    else:
        print("Jenis Tiket Tidak Valid")
        exit()
    statusMember = input("Status Member (Ya/Tidak): ")
    biayaAdmin = 2000 if statusMember == "Tidak" else 0
    diskon = 0.20 if statusMember == "Ya" else 0.0
    totalDiskon = hargaTiket * diskon 

totalBayar = int(hargaTiket + biayaAdmin - totalDiskon)
print("Total Bayar:", totalBayar)
uangBayar = int(input("Masukkan Uang Bayar: "))
if uangBayar < totalBayar:
    print("Mohon maaf, uang anda tidak cukup!")
    exit()
else:
    kembalian = uangBayar - totalBayar
print()
print("STRUK HASIL PEMBAYARAN")
print("Nama Pembeli:", nama)
print("Umur:", umur)
print("Jenis Tiket:", jenisTiket)
print("Status Member:", statusMember)
print("Total Bayar:", totalBayar)
print("Kembalian:", kembalian)
print()
print("TERIMA KASIH, SELAMAT MENONTON!")