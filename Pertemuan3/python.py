nama = input("Masukkan nama user : ")
kode_brg = input("Masukkan kode barang : ")
harga = int(input("Masukkan harga barang : "))
jumlah_brg = int(input("Masukkan jumlah barang : "))

print("\n==============================")

print(f"""
- Nama          : {nama}
- Kode Barang   : {kode_brg}
- Harga Barang  : {harga}
- Jumlah Barang : {jumlah_brg}
- Total Harga   : {jumlah_brg * harga:,.2f}
""")