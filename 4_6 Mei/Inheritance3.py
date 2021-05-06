# INHERiTANCE / PEWARISAN
# super class / parent class
class Manusia:
    # konstruktor
    def __init__(self, nama, jk, usia):
        self.nama = nama
        self.jk = jk
        self. usia = usia

    def info(self):
        print("Nama : {}\nJenis Kelamin : {}\nUsia : {}".format(self.nama, self.jk, self.usia))
        print("---------------------")

    def makan(self):
        print("Sedang makan nasi")
        print("---------------------")

# sub class / child class
class Pelajar(Manusia):
    # Konstruktor anak
    def __init__(self, nama, jk, usia, nis, nilai):
        Manusia.__init__(self, nama, jk, usia)
        self.nis = nis
        self.nilai = nilai

    def belajar(self):
        print("{} Sedang belajar".format(self.nama))
        print("---------------------")

    # methode overriding
    def makan(self):
        print("{} sedang sarapan pagi dengan nasi".format(self. nama))
        print("---------------------")

# sub class / child class
class Pekerja(Manusia):
    # konstruktor anak
    def __init__(self, nama, jk, usia, nip, gaji):
        Manusia.__init__(self, nama, jk, usia)
        self.nip = nip
        self.gaji = gaji

    def bekerja(self):
        print("{} sedang bekerja". format(self.nama))
        print("---------------------")

# instansiasi objek
Rudi = Pelajar("Rudianto", "Laki-Laki", 16, "13636", 90)
Wawan = Pekerja("Iwan", "Laki-Laki", 29, "1983463", 5000000)

# pemanggilan
Rudi.info()
Rudi.belajar()
Rudi.makan()
Wawan.info()
Wawan.bekerja()
Wawan.makan()