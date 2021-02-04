# Program menggunakan lambda 1 argumen
kuadrat = lambda x: x*x
# Output: 9 
print(kuadrat(3))
# Lambda dengan 2 argumen
kali = lambda x, y: x*y
# Output: 12 
print(kali(4,3))

# Filter bilangan ganjil dari list 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
list_ganjil = list(filter(lambda x: x%2 != 0, my_list)) 
# Output: [1, 3, 5, 7, 9] 
print(list_ganjil)

# Program untuk menghasilkan kuadrat bilangan 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
kuadrat = list(map(lambda x: x*x, my_list)) 
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ] 
print(kuadrat)