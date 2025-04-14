# Demetler 
# Listeler için geçerli olan pek çok özellik demet için de geçerli
# Daha az yer kaplar,daha hızlı
# Değiştirilemezler, ve hashable'dırlar yani sözlüğe çevrilebilir. Listelerde bu özellik yoktur.

t = (10, 'Ali',12.5)
print(type(t))

print("-----------------------------")

t = (10, 'Ali',12.5,[1,2,3])
print(t)
print(t[2]) # 12.5

print("-----------------------------")

t1 = (1,2,'ali',12.4,78)
l1 = list(t)
print(type(l1))

print("-----------------------------")

l2 = [1,2,3,4,5]
t2 = tuple(l2)
print(type(t2))

print("-----------------------------")

point = (10,2)
print(point)
(x,y) = point # unpacking
print(x,y) 

print("-----------------------------")

t3 = (10,'ali',12.5)
(a,b,c) = t3
print(a,b,c)

print("-----------------------------")

a = 10
b = 20
b,a = a,b
print(a,b)

print("-----------------------------")

t = 1,2,3
print(t*2) # 1,2,3,1,2,3

print("-----------------------------")

t = (10,'Ahmet','Zeynep',12.3,103)
print(10 in t) # True
print(200 not in t)

print("-----------------------------")

# Kümeler (Sets)
# Farklı elemanlardan oluşan topluluklardır.
# Aynı elemanlar tekrar edebilir ancak farklı olan elemanlardan bir küme oluşturur.
# Elemanları hashable olmalı list ve set'ler hashlenemez.
# n. kavram diye bir şey yok öncelik sonralık ilişkisi yoktur.
# sadece set() komutu ile boş küme oluşturur.
# * + işlemleri yapılmaz.

s = {1,2,3,4,5}
print(s)

