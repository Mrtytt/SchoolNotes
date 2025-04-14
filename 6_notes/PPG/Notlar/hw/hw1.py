import datetime

dob_str = input("Doğum tarihinizi GG-AA-YYYY formatında giriniz: ")
dob = datetime.datetime.strptime(dob_str, "%d-%m-%Y")
dot = datetime.datetime.today()

def tarih_yazdir(date_of_birth, date_of_today):
    print("Doğum Tarihiniz :", date_of_birth.strftime("%d-%m-%Y"))
    print("Bugünün Tarihi :", date_of_today.strftime("%d-%m-%Y"))

def yasanan_gun(date_of_birth, date_of_today):
    fark = date_of_today-date_of_birth
    print(str(fark.days) + " gündür yaşıyorsunuz.")

if dob < dot:
    tarih_yazdir(dob, dot)
    yasanan_gun(dob, dot)
if dob == dot:
    print("Bugün doğum gününüz! İyi ki doğdunuz :)")
else:
    print("Hata doğum tarihi bugünden sonra olamaz!")



    
