# veri_turleri_ve_listeler.py

# Veri Türleri
a = 5
print(type(a))  # int - Tam sayı

b = 3.2
print(type(b))  # float - Ondalıklı sayı

c = True
print(type(c))  # bool - Mantıksal (doğru/yanlış)

s = 'Bilgisayar'
print(type(s))  # str - Metin (string)

n = None
print(type(n))  # NoneType - Boş/Hiçbir şey değil

# Matematiksel işlemler ve karşılaştırma
a = 5
b = 10
c = a + b
print(c)  # 15

# Ondalıklı sayılarla işlem ve karşılaştırma
a = 0.3
b = 0.2
c = a - b
print(c)  # 0.09999999999999998
if (c == 0.1):
    print("True")
else:
    print("False")  # Gerçekte 0.1 değil, False döner

# Koşullu ifadeler
a = 10
if (a > 0):
    print("Pozitif bir sayı girdiniz")
    print("Girdiğiniz sayı 0'dan büyük bir sayıdır")
elif (a < 0):
    print("Negatif bir sayı girdiniz")
else:
    print("Girdiğiniz sayı sıfırdır")

# Matematiksel işlemler
print(5 ** 4)     # 625
print(10 / 3)     # 3.333...
print(10 // 3)    # 3 (tam bölme)

# print fonksiyonunun kullanımı
a, b, c = 10, 20, 30
print(a, b, c, sep=', ')  # 10, 20, 30
print(a, b, c, sep='')    # 102030
print(a, b, c, sep='', end='.')  # 102030.

# Kullanıcıdan giriş alma
# a = int(input('Bir değer giriniz: '))
# print(a ** 2)

# Liste veri tipi
liste = [1, 2, 3]
print(liste)
print(type(liste))

karisik = [1, 2.5, 'Ali', 'Murat']
print(karisik)

ic_ice = [1, 2.5, 'Ali', 'Murat', [20, 30, 'Kemal']]
print(ic_ice)

# Liste erişim
a = [10, 20, 30, 40, 50]
print(a[-1])  # Son eleman

a = [1, [2, 3, 4], 5, [6, 7, 8]]
print(a[1][-1])  # 4
print(a[-1][-2])  # 7

# Dilimleme (slicing)
a = list(range(10, 110, 10))
print(a[1:3])
print(a[::2])
print(a[8:1:-1])

# Liste kopyalama (referans ve değer kopyalama)
a = [10, 20, 30]
b = a
print(id(a), id(b))  # Aynı id, aynı nesne

b = a[:]
print(id(a), id(b))  # Farklı id, kopyalanmış nesne

# Liste birleştirme
a = [10, 20, 30]
b = [1, 2, 3]
print(a + b)

# Liste işlemleri
a = list("Bursa Uludağ Üniversitesi")
print(a)

a = [10, 20, 30, 40, 50, 60, 70]
a[2:4] = [1, 2, 3]
print(a)

a[2:4] = [13]
print(a)

a[2:4] = []
print(a)

a[0:0] = [1, 2]
print(a)

# Hatalı kullanım örneği (dilimleme step ile ise aynı sayıda eleman gerekir)
# a[0:8:2] = [10, 20, 30]  # HATA

# range fonksiyonu
print(list(range(10)))
print(list(range(10, 20, 2)))
print(list(range(100, 90, -2)))

# Üyelik işlemleri
a = [1, 2, 3, 'Ali']
print(3 in a)
print('Ahmet' not in a)

# Liste metodları
a = [1, 2, 3]
a.append(100)
print(a)

a.append([10, 20])
print(a)

a.extend([10, 20])
print(a)

a.insert(2, 99)
print(a)

a.pop()
print(a)

a.clear()
print(a)

a = [10, 20, 'Ali', 'Ahmet', 'Ali']
a.remove('Ali')
print(a)

print(a.index('Ahmet'))

a = [10, 20, 'Ali', 'Ahmet', 'Ali']
print(a.count('Ali'))

# Sıralama işlemleri
nums = [3, 58, 2, 9]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

names = ['Ali', 'Muhammed', 'Fatma']
names.sort()
print(names)

names.sort(key=len)
print(names)

# Kopyalama
a = [3, 58, 2]
b = a.copy()
print(b)

# Değişken atama
a, b, c = ['Atakan', 'Rüzgar', 'Ahmet']
print(a, b, c)
