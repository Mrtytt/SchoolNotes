# Demetler (Tuples)
t = (10, 'Ali', 12.5)
print(type(t))  # <class 'tuple'>


t = (10, 'Ali', 12.5, [1, 2, 3])
print(t)
print(t[2])  # 12.5


t = (1, 2, 'Ali', 12.4, 78)
l = list(t)
print(type(l))  # <class 'list'>


l = [1, 2, 3, 4, 5]
t = tuple(l)
print(type(t))  # <class 'tuple'>


point = (10, 2)
print(point)
(x, y) = point
print(x)  # 10
print(y)  # 2


t = (10, 'Ali', 12.5)
(a, b, c) = t
print(b)  # Ali


a = 10
b = 20
b, a = a, b
print(a)  # 20


t = 1, 2, 3
print(t * 2)  # (1, 2, 3, 1, 2, 3)


t = (10, 'Ahmet', 'Zeynep', 12.3, 103)
print(10 in t)  # True


# Kümeler (Sets)
s = {1, 2, 3, 4, 5}
print(s)
print(type(s))  # <class 'set'>


s = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 5, 5, 4, 3, 4}
print(s)  # {1, 2, 3, 4, 5}

# s = {1, 'Ali', 12.3, [2, 3, 4], 10, 'Zeynep'}  # TypeError: unhashable type: 'list'


s = {1, 'Ali', 12.3, (2, 3, 4), 10, 'Zeynep'}
print(s)  # {1, 10, (2, 3, 4), 'Ali', 'Zeynep', 12.3}

# s = {1, 'Ali', 12.3, (2, 3, 4, [5, 6, 7]), 10, 'Zeynep'}  # TypeError

# t = {1, 2, 3}
# print(t * 3)  # TypeError


s = {}  # dictionary\sss = set()
print(type(s))   # <class 'dict'>
print(type(set(s)))  # <class 'set'>


s = {1, 2, 3, 'Ahmet', 'Zeynep', 12.6}
print(1 in s)  # True


s = {1, 2, 3, 'Ahmet', 'Zeynep', 12.6}
b = {1, 2, 3}
print(b.issubset(s))  # True
print(b <= s)         # True


a = {1, 2, 3, 'Ahmet', 'Zeynep', 12.6}
b = {1, 2, 3}
print(a >= b)            # True
print(a.issubset(b))     # False


a = {1, 2, 3, 'Ahmet', 'Zeynep', 12.6}
b = {3, 4, 'Hakan', 'Arda', 'Zeynep', 12.6, 10}
c = a.union(b)
print(c)


a = {1, 2, 3, 'Ahmet', 'Zeynep', 12.6}
b = {3, 4, 'Hakan', 'Arda', 'Zeynep', 12.6, 10}
c = a.intersection(b)
print(c)


a = {1, 2, 3, 'Ahmet', 'Zeynep', 12.6}
b = {3, 4, 'Hakan', 'Arda', 'Zeynep', 12.6, 10}
c = a.difference(b)
print(c)


s = input('Birinci yazıyı giriniz : ')
k = input('İkinci yazıyı giriniz : ')
print(set(s) == set(k))


# Sözlükler (Dictionaries)
d = {'Ali': 123, 'Bob': 456, 'Alice': 256}
print(type(d))  # <class 'dict'>


cities = {
    'İstanbul': ['Beykoz', 'Beşiktaş', 'Esenler', 'Kadıköy', 'Şişli'],
    'Ankara': ['Çankaya', 'Ulus', 'Kızılay'],
    'Mersin': ['Akdeniz', 'Tarsus', 'Anamur'],
    'Bursa': ['Nilüfer', 'Yıldırım', 'Orhangazi', 'Osmangazi']
}
print(cities.get(2), 'Not Found')


d = {1: 'Ali', 2: 'Mehmet', 3: 'Gül'}
k = d.copy()
print(k)
print(d.keys())
print(d.values())
