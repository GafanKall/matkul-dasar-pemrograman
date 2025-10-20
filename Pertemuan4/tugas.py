# Tugas 1, PT. DINGIN DAMAI (Study Case)

gaji_pokok = 300000

# Input data karyawan
nama_karyawan = input("Masukkan nama karyawan : ")
golongan = int(input("Masukkan golongan karyawan [1/2/3] : "))
pendidikan = input("Masukkan pendidikan karyawan [SMA/D1/D3/S1] : ")
jumlah_jam_kerja = int(input("Masukkan jumlah jam kerja karyawan : "))

# Hitung tunjangan jabatan
if golongan == 3:
    tunjangan_jabatan = 0.15 * gaji_pokok 
elif golongan == 2:
    tunjangan_jabatan = 0.10 * gaji_pokok
elif golongan == 1:
    tunjangan_jabatan = 0.05 * gaji_pokok
else :
    tunjangan_jabatan = 0

# Hitung tunjangan pendidikan
if pendidikan == "S1" :
    tunjangan_pendidikan = 0.30 * gaji_pokok
elif pendidikan == "D3" :
    tunjangan_pendidikan = 0.20 * gaji_pokok
elif pendidikan == "D1" :
    tunjangan_pendidikan = 0.15 * gaji_pokok
elif pendidikan == "SMA" :
    tunjangan_pendidikan = 0.025 * gaji_pokok
else :
    tunjangan_pendidikan = 0

# Hitung honor lembur
if jumlah_jam_kerja > 8 :
    jam_lembur = jumlah_jam_kerja - 8
    honor = jam_lembur * 3500
else : 
    honor = 0
    jam_lembur = 0



print ("\n========== GAJI KARYAWAN ========")
print (f"Karyawan bernama : {nama_karyawan}")
print ("Honor yang diterima")
print (f"Tunjangan jabatan : {tunjangan_jabatan:,.2f}")
print (f"Tunjangan pendidikan : {tunjangan_pendidikan:,.2f}")
print (f"Honor lembur : {honor:,.2f}")
print ("-----------------------------------------------------")
print (f"Total gaji : {gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + honor}")