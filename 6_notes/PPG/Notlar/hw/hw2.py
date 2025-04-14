# 4 kişiyle oynanan bir oyun olacak
# 52 karttan oluşacak
# Her oyuncuya 13 tane kart dağıtılacak >>> Demet olacak
# Kartlar "Karo", "Kupa", "Maça" ve "Sinek" >>> 4 elemanlı bir demet olacak
# 2, 3, 4, 5, 6, 7, 8, 9, 10, As, Vale, Kız, Papaz
# 52 kartlı stringlerden oluşan bir listeyi veren create_deck isimli bir fonksiyon yazınız.
# Bu fonksiyonun parametresi olmayacak. Geri dönüş değeri "Karo-2", "Kupa-2", "Karo-As",....
# biçiminde yazılardan oluşan bir listedir.
# Fonksiyondaki listeyi tüm kartları el ile yazarak OLUŞTURMAYINIZ
# distribute_deck(deck) isimli fonksiyon yaratılan desteyi dağıtacaktır.
# Bu fonksiyon 52 elemanlı kart listesini parametre olarak alacak, geri dönüş değeri
# 4 elemanlı bir demet verecektir. Demetin her bir elemanı 13 karttan oluşan bir liste olacaktır.

cardTypes = ("Karo","Sinek","Maça","Kupa")
cardValues = ("As","2","3","4","5","6","7","8","9","10","Vale","Kız","Papaz")
player_count = 4

def create_deck():
    deck = []
    for type in cardTypes:
        for value in cardValues:
            deck.append(f"{type}-{value}")
    return deck

deck = create_deck()
# print(deck)

def distribute_deck(deck):
    cards_per_player = len(deck) // player_count
    distributed = ()
    for i in range(player_count):
        player_cards = deck[i * cards_per_player : (i + 1) * cards_per_player]
        distributed += (player_cards,)
    return distributed

distributed= distribute_deck(deck)
print(distributed)