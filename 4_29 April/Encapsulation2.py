class Siswa:

    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas

    #getter
    def getnis(self):
        return self.__nis

    #setter
    def setnis(self, newnis):
        self.__nis = newnis

bahar = Siswa(15355, "Zufar Bahar", "XI MIPA 5")

print(bahar.getnis())
bahar.setnis(13567)
print(bahar.getnis())
