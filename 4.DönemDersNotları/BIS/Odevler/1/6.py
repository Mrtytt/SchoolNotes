import os 
import atexit
import sys

def parentCleaner():
    # Ana işlem temizlik işlemlerini gerçekleştiriyor
    print("Ana işlem temizlik yapıyor...\n")

def main():
    # Ana işlem, bir çocuk işlemi oluşturuyor
    if os.fork():
        # Ana işlem, çocuk işlemi sonlandırmak için atexit ile parentCleaner fonksiyonunu kaydediyor
        atexit.register(parentCleaner)
        # Ana işlem, kendi PID'sini yazdırıyor
        print("Bu ana işlem {}\n".format(os.getpid()))
    else:
        # Çocuk işlem, kendi PID'sini yazdırır.
        print("Bu çocuk işlem {}\n".format(os.getpid()))

if __name__ == "__main__":
    main() # Burada da main fonksiyojnunu çağırıyoruz
    sys.exit(0)