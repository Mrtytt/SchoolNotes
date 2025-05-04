import shelve

def sehirleri_listele(veritabani):
    print("\n--- Şehirler ---")
    for sehir in veritabani:
        print(sehir)

def sehir_ve_ilceler(veritabani):
    print("\n--- Şehirler ve İlçeleri ---")
    for sehir in veritabani:
        ilceler = veritabani[sehir]
        print(f"{sehir} => {', '.join(ilceler)}")

def sehir_arama(veritabani):
    aranan = input("Hangi şehri arıyorsunuz? ").strip()
    if aranan in veritabani:
        print(f"{aranan} şehrinin ilçeleri: {', '.join(veritabani[aranan])}")
    else:
        print("Bu şehir bulunamadı.")

def sehir_ekle(veritabani):
    yeni_sehir = input("Eklemek istediğiniz şehir: ").strip()
    if yeni_sehir in veritabani:
        print("Bu şehir zaten kayıtlı.")
    else:
        ilceler = input("İlçeleri virgülle ayırarak giriniz: ")
        ilce_listesi = [i.strip() for i in ilceler.split(",")]
        veritabani[yeni_sehir] = ilce_listesi
        print("Şehir başarıyla eklendi.")

def menu():
    with shelve.open("city", writeback=True) as veritabani:
        while True:
            print("\n----- MENÜ -----")
            print("1) Şehirleri Listele")
            print("2) Şehirleri ve Onların İlçelerini Listele")
            print("3) Şehir Ara")
            print("4) Şehir Ekle")
            print("5) Çıkış")

            secim = input("Seçiminiz (1-5): ").strip()

            if secim == "1":
                sehirleri_listele(veritabani)
            elif secim == "2":
                sehir_ve_ilceler(veritabani)
            elif secim == "3":
                sehir_arama(veritabani)
            elif secim == "4":
                sehir_ekle(veritabani)
            elif secim == "5":
                print("Programdan çıkılıyor...")
                break
            else:
                print("Lütfen 1 ile 5 arasında bir seçim yapınız.")

if __name__ == "__main__":
    menu()
