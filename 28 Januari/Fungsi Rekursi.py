# Contoh fungsi rekursi 
# Menentukan faktorial dari bilangan 
def faktorial(x):
    if x == 1:
        return 1
    else:
        return (x*faktorial(x-1))
bil = 4
print("Faktorial dari", bil, " adalah", faktorial(bil))