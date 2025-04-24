def foo():
    print(a)

a = 10
foo()  # geçerli

def foo():
    print(a)


foo()  # ERROR!!!
a = 10


def foo():
    bar()


def bar():
    pass


foo()  # geçerli

""" 
İçlemler (Comprehensions) 
1- Liste İçlemleri (list comprehension) 
2- Küme İçlemleri (set comprehension) 
3- Sözlük İçlemleri (dictionary comprehension) 
4- Üretici Fonksiyon İçlemleri 
"""
# Liste İçlemleri
# [<ifade> <for döngüsü> [if koşulu]]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# listenin içindeki her bir elemanın karesi
b = [x * x for x in a]
print(b)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for x in a:
    b.append(x * x)
print(b)

a = [3, 6, 2, 10, 34, 23, 19]
b = [x % 2 == 0 for x in a]
print(b)
# [False, True, True, True, True, False, False]

names = ['Sabri', 'Yiğit', 'Aysun', 'Tunahan', 'Murat']
a = [len(name) for name in names]
print(a)
# [5, 5, 5, 7, 5] Herbir ismin karakter uzunluğu

names = ['Sabri', 'Yiğit', 'Aysun', 'Tunahan', 'Murat']
# isimleri tersten yazdırmak istersek
a = [name[::-1] for name in names]
print(a)
# ['irbaS', 'tiğiY', 'nusyA', 'nahanuT', 'taruM']

a = [3, 6, 8, 10, 39, 34, 37, 42, 43, 65, 82]
b = [x for x in a if x % 2 == 0]
print(b)
# [6, 8, 10, 34, 42, 82]

names = ['Sabri', 'Yiğit', 'Aysun', 'Tunahan', 'Murat']
a = [name for name in names if 'a' in name]
print(a)
# ['Sabri', 'Tunahan', 'Murat'] içerisinde 'a' karakteri olan isimler

names = ['Sabri', 'Yiğit', 'Aysun', 'Tunahan', 'ahmet', 'Murat']
aNames = [name for name in names if name[0] == 'a' or name[0] == 'A']
print(aNames)
# ['Aysun', 'ahmet']  ilk karakteri 'a' ya da 'A' olan isimler

names = ['Sabri', 'Yiğit', 'Aysun', 'Tunahan', 'ahmet', 'Murat']
aNames = [name for name in names if name[0].lower() == 'a']
print(aNames)
# ['Aysun', 'ahmet']  ilk karakteri 'a' ya da 'A' olan isimler
cities = ['Ankara', 'Bursa', 'Mersin', 'İstanbul', 'İzmir',
          'adana']
xCities = [city[:3].upper() for city in cities if
           city.lower().find('a') != -1]
print(xCities)
# ['ANK', 'BUR', 'İST', 'ADA']   içerisinde 'a' karakteri bulunan şehirlerin ilk 3 karakterinden yeni bir liste
# Yazılardan oluşan bir liste oluşturunuz. Bu listedeki palindrom
# olan elemanları içlemler yoluyla bir liste biçiminde elde ediniz
# anastas mum satsana, kabak, ey edip adanada pide ye
texts = ['anastas mum satsana', 'salih', 'kabak',
         'mustafa', 'ey edip adanada pide ye']
palindromes = [text for text in texts if text.lower() == text[::-1].lower()]
print(palindromes)
# ['anastas mum satsana', 'kabak', 'ey edip adanada pide ye']

# bursa, izmir
# bi, bz, bm, bi, br, ui, uz, um, ui, ur, ri, rz, rm, si, ar ....
s = [a + b for a in 'bursa' for b in 'izmir']
print(s)
# ['bi', 'bz', 'bm', 'bi', 'br', 'ui', 'uz', 'um', 'ui', 'ur', 'ri', 'rz', 'rm', 'ri', 'rr', 'si', 'sz', 'sm', 'si', 'sr', 'ai', 'az', 'am', 'ai', 'ar']

# Küme İçlemleri
s = {ch for ch in 'bursa'}
print(s)
# {'b', 'r', 's', 'a', 'u'}

# Sözlük içlemleri
d = {i: str(i) for i in [1, 2, 3, 4, 5]}
print(d)
# {1: '1', 2: '2', 3: '3', 4: '4', 5: '5'}

# Üretici İçlemler
x = (i * i for i in range(10))
print(type(x))
for i in x:
    print(i, end=' ')
''' 
<class 'generator'> 
0 1 4 9 16 25 36 49 64 81 
'''
