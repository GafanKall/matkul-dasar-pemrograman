print("========== Latihan 1 ==========\n")

produk = input("Masukkan nama produk : ")
harga = int(input("Masukkan harga produk : "))
jumlah = int(input("Masukkan jumlah produk : "))

total = harga * jumlah

print(f"""
- Nama Produk   : {produk}
- Harga Produk  : {harga}
- Jumlah Produk : {jumlah}
- Total Harga   : {total:,.2f}
""")

print("========== Latihan 2 ==========\n")

nim = int(input("Masukkan NIM      : "))
nama = (input("Masukkan Nama       : "))
jurusan = (input("Masukkan Jurusan : "))
alamat = (input("Masukkan Alamat   : "))

print(f"""
- NIM     : {nim}
- Nama    : {nama}
- Jurusan : {jurusan}
- Alamat  : {alamat}
""")