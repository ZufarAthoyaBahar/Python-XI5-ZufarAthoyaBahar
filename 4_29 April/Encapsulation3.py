class Siswa:

    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas

    #decorator
    @property
    def nis(self):
        pass

    #getter
    @nis.getter
    def nis(self):
        return self.__nis

    #setter
    @nis.setter
    def nis(self, newnis):
        self.__nis = newnis

bahar = Siswa(13456, "Zufar Bahar", "XI MIPA 5")

print(bahar.nis)
bahar.nis = 13486
print(bahar.nis)