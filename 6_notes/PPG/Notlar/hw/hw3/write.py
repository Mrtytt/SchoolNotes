import shelve

# Şehir ve ilçelerin bulunduğu dosyayı açıyoruz
with open("city-village.txt", "r", encoding="utf-8") as dosya:
    satirlar = dosya.readlines()

# shelve ile 'city' adlı veri tabanı oluşturuyoruz
with shelve.open("city") as veritabani:
    for satir in satirlar:
        satir = satir.strip()
        if "=>" in satir:
            sehir, ilceler = satir.split("=>")
            sehir = sehir.strip()
            ilce_listesi = [ilce.strip() for ilce in ilceler.split(",")]
            veritabani[sehir] = ilce_listesi

print("Veriler başarıyla kaydedildi.")
