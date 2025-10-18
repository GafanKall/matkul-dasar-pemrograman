nilai_mhs = int(input("Masukkan Nilai Mahasiswa :"))

def grade(n):
    return (
        "Masukkan nilai yang valid antara 0 - 100" if n < 0 or n > 100 else
        "Nilai Mahasiswa : A" if nilai_mhs >= 80 else
        "Nilai Mahasiswa : B" if nilai_mhs >= 70 else
        "Nilai Mahasiswa : C" if nilai_mhs >= 60 else
        "Nilai Mahasiswa : D" if nilai_mhs >= 30 else
        "Nilai Mahasiswa : E"
    )
print(grade(nilai_mhs))