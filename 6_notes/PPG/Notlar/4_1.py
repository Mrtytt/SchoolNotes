# Python'da Tuple, List, Dictionary ve Set Veri Yapıları

# 1. List (Liste)
# - Sıralıdır (Ordered)
# - Değiştirilebilir (Mutable)
# - Aynı veya farklı türde elemanlar içerebilir
# - Aynı elemanı birden fazla kez içerebilir (Duplicate Allowed)

my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # Eleman ekleme
my_list[0] = 10    # Eleman değiştirme
print("List:", my_list)


# 2. Tuple (Demet)
# - Sıralıdır (Ordered)
# - Değiştirilemez (Immutable)
# - Aynı veya farklı türde elemanlar içerebilir
# - Aynı elemanı birden fazla kez içerebilir (Duplicate Allowed)

my_tuple = (1, 2, 3, 4, 5)
# my_tuple[0] = 10  # Hata! Tuple değiştirilemez.
print("Tuple:", my_tuple)


# 3. Dictionary (Sözlük)
# - Sıralıdır (Python 3.7+ için Ordered)
# - Değiştirilebilir (Mutable)
# - Anahtar-değer çiftleri içerir (Key-Value Pairs)
# - Aynı anahtar tekrar edemez (Keys are unique)

my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
my_dict["age"] = 26  # Değer güncelleme
my_dict["job"] = "Engineer"  # Yeni anahtar-değer ekleme
print("Dictionary:", my_dict)


# 4. Set (Küme)
# - Sırasızdır (Unordered)
# - Değiştirilebilir (Mutable) ancak elemanları değiştirilemez olmalıdır (Immutable)
# - Her eleman benzersizdir (Unique elements)
# - Aynı elemanı birden fazla kez içeremez (No Duplicates)

my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # Eleman ekleme
my_set.add(3)  # Aynı eleman eklenmez
print("Set:", my_set)


# Ortak Özellikler:
# - Hepsi koleksiyon veri yapılarıdır.
# - İçlerinde farklı veri türlerini barındırabilirler.
# - Döngülerle (for, while) üzerinde gezilebilirler.
# - len() fonksiyonu ile eleman sayıları bulunabilir.

print("List Length:", len(my_list))
print("Tuple Length:", len(my_tuple))
print("Dictionary Length:", len(my_dict))
print("Set Length:", len(my_set))


# Farklar:
# - List ve Tuple sıralıdır, Set sırasızdır.
# - List ve Dictionary değiştirilebilir, Tuple değiştirilemez.
# - Set'te aynı eleman bir kez bulunur, diğerlerinde tekrar edebilir.
# - Dictionary, anahtar-değer çiftleri ile çalışır.

