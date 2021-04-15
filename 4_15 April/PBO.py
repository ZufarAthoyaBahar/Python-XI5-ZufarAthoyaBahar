class Karyawan :
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(self, nama, gaji, umur):
        self.nama = nama
        self.gaji = gaji
        self.umur = umur
        Karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah(self) :
        print("Total karyawan:",Karyawan.jumlah_karyawan)

    def tampilkan_profil(self) :
        print("Nama :", self.nama)
        print("Umur :", self.umur)

    def tampilkan_gaji(self) :
        print("Nama :", self.nama)
        print("Gaji :", self.gaji)


# Membuat objek pertama dari kelas Karyawan
karyawan1 = Karyawan("Sarah", 1000000, 30)
# Membuat objek kedua dari kelas Karyawan
karyawan2 = Karyawan("Budi", 2000000, 29)

karyawan1.tampilkan_profil ()
karyawan1.tampilkan_gaji ()
karyawan2.tampilkan_profil ()
karyawan2.tampilkan_gaji ()
print("Total karyawan : ", Karyawan.jumlah_karyawan)