import os 
import sys

def main():
    # Ana işlem bir çocuk işlemi oluşturuyoruz
    if os.fork():
        # Ana işlem bir çocuk işlemi daha oluşturuyoruz
        if os.fork():
            # Ana işlem ikinci çocuk işlemi tarafından oluşturulan bir torun işlemi oluşturur ve "2" yazdırıyoruz
            print("2 ")
        else:
            # İkinci çocuk işlemi kendi bir torun işlemi oluşturuyoruz
            os.fork()
            # İkinci çocuk işlemi "1" yazdırıyoruz
            print("1 ")
    else:
        # İlk çocuk işlemi "3" yazdırıyoruz
        print("3 ")
    # Ana işlem ve tüm çocuk işlemleri, "4" yazdırıyoruz
    print("4 ")

if __name__ == "__main__":
    main() # Burada da main fonksiyojnunu çağırıyoruz
    sys.exit(0)