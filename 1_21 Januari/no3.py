#XI 5 - 36 - Zufar Athoya Bahar
def print_faktor(x):
    print("Faaktor dari ", x, "adalah : ")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
num = int(input("Masukkan Bilangan : "))
print_faktor(num)