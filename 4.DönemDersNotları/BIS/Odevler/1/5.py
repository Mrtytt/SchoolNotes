import os
import sys

def main():
    # Ana işlem bir şeyler yapar ve ardından fork() işlemini çağırıyoruz
    print("Ana işlem bazı işlemler yapar ve ardından fork() çağrısı yapar...\n")

    # Ana işlem, çocuk işlem oluşturur ve işlemlerini yürütmeye devam ediyor
    if os.fork():
        # Ana işlem, tamamen farklı bir şey yapıyor
        print("...Ana işlem tamamen farklı bir işlem gerçekleştirir\n")
    else:
        # Çocuk işlem, bir işlemin yerine geçerek işlemi başlatır
        print("Çocuk işlem bir işlemi çalıştırır...\n")
        # Çocuk işlem, /bin/ls komutunu çağırarak /etc/apache2/conf.d/ dizinini listeleniyor
        os.execl("/bin/ls", "/bin/ls", "-1", "/etc/apache2/conf.d/", None)

if __name__ == "__main__":
    main() # Burada da main fonksiyojnunu çağırıyoruz
    sys.exit(0)