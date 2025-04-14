"""
b= 20;c=30
print(b,c,sep=", ") # Sep komutu aralara ne konulacağını belirler. # 20, 30
print(b,c,sep="",end=".") # End komutu imleti en sona getirir. # 2030.
"""

# -----------------------------------------------------------------

"""
def kare(sayi):
    # return sayi*sayi
    return sayi ** 2

sayi = int(input("Lütfen bir sayi giriniz : "))
sonuc = kare(sayi)

print("Sonuç :", sonuc)
"""

"""
Lütfen bir sayi giriniz : 10
Sonuç : 100
"""

# ------------------------------------------------------------------

# Dolaşılabilir Nesneler
# Listeler,kümeler,sözşükler,demetler ve str

"""
# Listeler
a = [1,2,3]
print(a) # [1, 2, 3]
print(type(a)) #<class 'list>

x = [1,2.5,'Ali',True] # Heterojen olarak farklı değişkenleri tutabilir.
print(x) # [1, 2.5, 'Ali', True]

xx = [1, 2.5, 'Ali', True,[20,30,40],65]
print(xx)
print(xx[4][1]) # 30
print(xx[-1]) # 3

a = [10,20,30,40,50]
print(a[1:3]) # 20 30
print(a[0:len(a)]) # 10,20,30,40,50
print(a[1:15]) # [20, 30, 40, 50]
"""

"""
a = [10,20,30,40,50]
b = a
print('b = ',id(b))
print('a = ',id(a))
# Bu sayede farklı adresleri gösteren bir kopya liste oluşturulur
b = a[:]
print('b = ',id(b))
print('a = ',id(a))
"""

a = [10,20,30,40,50]
b = [110,120,130,140,150]
c = a + b
print(c)

x = list("Bursa Uludag Universitesi")
print(x)

a[2:4] = [1,2,3]
print(a)