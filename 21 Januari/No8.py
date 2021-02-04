#XI 5 - 36 - Zufar Athoya Bahar
def modus(list_angka):
    count = 0
    terbanyak = list_angka
    for i in list_angka:
        x = list_angka.count(i)
        if x >= count:
            count = x
            terbanyak = i
    return(terbanyak)

list_angka = input("Masukan angka = ")
print("Modusnya = ", modus(list_angka))
    