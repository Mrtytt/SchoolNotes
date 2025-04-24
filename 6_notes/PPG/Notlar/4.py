# Python Değişken Kapsamı, enumerate, map ve Fonksiyonlar Özeti

# enumerate kullanımı
a = [10, 20, 30, 40, 50]
print(type(enumerate(a)))  # enumerate objesi
d = {'ali': 10, 'hakan': 20, 'gül': 30}
print(list(enumerate(d)))  # [(0, 'ali'), (1, 'hakan'), (2, 'gül')]

# En büyük elemanın indeksini bulma
a = [12, 15, 38, 84, 42]
max_index = 0
for i in range(1, len(a)):
    if a[i] > a[max_index]:
        max_index = i
print("Max indeks =", max_index)

# enumerate ile en büyük eleman
e = enumerate(a)
max_val = next(e)
for t in e:
    if t[1] > max_val[1]:
        max_val = t
print("Max indeks =", max_val[0])

# Global ve yerel değişkenler
x = 10
def foo(): print(x)
foo()
x = 20
foo()
print(x)

def local_example():
    y = 20
    print(y)
local_example()

# Global kullanımı
x = 100
def local_x():
    x = 200
    print(x)
local_x()
print(x)

x = 10
def update_global():
    global x
    x = 20
update_global()
print(x)  # 20

# map fonksiyonu kullanımı
a = [1, 2, 3]
def square(n): return n*n
print(list(map(square, a)))
print([i*i for i in a])  # aynı işlemin comprehension hali

# İç içe fonksiyonlar ve scope
def outer():
    val = 10
    def inner():
        print('val =', val)
    inner()
outer()

# nonlocal kullanımı
def example():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)
example()  # 20

# global & nonlocal farkları
x = 10
def g():
    global x
    x = 20
    def inner():
        global x
        x = 30
    inner()
g()
print(x)  # 30

# Asal sayıları yazdıran fonksiyon
def writePrimes(n):
    def isPrime(val):
        if val < 2:
            return False
        if val == 2:
            return True
        if val % 2 == 0:
            return False
        for i in range(3, int(val ** 0.5) + 1, 2):
            if val % i == 0:
                return False
        return True
    for i in range(2, n+1):
        if isPrime(i):
            print(i, end=' ')
writePrimes(30)
