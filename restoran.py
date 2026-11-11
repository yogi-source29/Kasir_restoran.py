# APLIKASI KASIR RESTORAN

total = 0
print("1. Nasi Goreng - 25.000")
print("2. Mie Ayam - 15.000")
print("3. Ayam Geprek - 20.000")
print("4. Sate Ayam - 30.000")
print("5. Bakso - 18.000")
print("0. Selesai Memilih")

while True:
    pilihan = int(input("Masukkan Nomor Menu :"))
    if pilihan == 0 : 
        break
    if pilihan == 1 :
        harga = 25000
    elif pilihan == 2 :
        harga = 15000
    elif pilihan == 3 :
        harga = 20000
    elif pilihan == 4 :
        harga = 30000
    elif pilihan == 5 :
        harga = 18000
    else :
        print("Menu tidak tersedia")
        continue
    jumlah = int(input("Masukkan Jumlah Pesanan :"))
    subtotal = harga *  jumlah
    total = total + subtotal

# Menghitung Diskon

if total >= 200000 :
    diskon = total * 0.2
    total_bayar = total-diskon
else :
    diskon = 0
    total_bayar = total 

print("Total Belanja :RP.", total)
print("Diskon :", diskon)
print("Potongan :RP.", total - total_bayar)
print("----------------------")
print("Total Bayar :RP.", total_bayar)
print("Terima kasih")
