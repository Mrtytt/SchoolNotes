# Koşullar
a = int(input("Sayı gir: "))
print("Çift" if a % 2 == 0 else "Tek")

a = int(input("Sayı gir: "))
if a < 0:
    print("Negatif")
elif a > 0:
    print("Pozitif")
else:
    print("Sıfır")

# while döngüsü
i = 0
while i < 10:
    print(i)
    i += 1

# Liste üzerinde while döngüsü
a = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < len(a):
    print(a[i], end='')
    i += 1

# Ortalama hesaplama
import statistics
a = [4, 6, 87, 3, 45, 12, 48, 18, 22, 26]
print("Toplam:", sum(a), "Ortalama:", statistics.mean(a))

# for döngüsü örnekleri
s = "Bursa Uludağ Üniversitesi"
for c in s:
    print(c, end=' ')

d = {'A': 1, 'B': 2}
for k in d:
    print(k, '=>', d[k])

# range kullanımı
for i in range(1, 10):
    print(i, end=' ')

# Asal sayı kontrolü
n = int(input("Sayı gir: "))
if n < 2:
    print("Geçersiz")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Asal değil")
            break
    else:
        print("Asal")

# Ternary (üçlü) operatör
n = int(input("Sayı gir: "))
print(100 if n % 2 == 0 else 200)

# Fonksiyon örnekleri
def square(a): return a * a
print(square(5))

def getOddEven(l):
    odd, even = [], []
    for i in l:
        (even if i % 2 == 0 else odd).append(i)
    return odd, even

print(getOddEven([1,2,3,4,5,6,7,8,9]))

import math
def get_mean_stddev(l):
    mean = sum(l)/len(l)
    stddev = math.sqrt(sum((x-mean)**2 for x in l)/len(l))
    return mean, stddev

print(get_mean_stddev([1,2,3,5,6,8]))
