"""
yan_cizgi = "-"
dik_cizgi = "|"
bosluk = " "

yukseklik = int(input("Yükseklik giriniz : 15"))
genislik = int(input("Genislik giriniz : "))

for i in range(1,yukseklik + 1):
    if i == 1 or i == yukseklik:
        print(yan_cizgi*genislik)
    else:
        print(dik_cizgi + bosluk*(genislik-2) + dik_cizgi)
"""

