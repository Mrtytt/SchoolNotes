import os
import sys

def main():
    # Ana işlem, kendi işlemini başlatmadan önce bir şeyler yapar.
    print("{} Ana işlem bir şeyler yapar...\n".format(os.getpid()))

    # fork() işlemi gerçekleştirilir. Eğer fork() çağrısı 0'dan farklı bir değer döndürürse, bu ana işlemde devam eder.
    if os.fork():
        # Ana işlem, farklı bir işlem yapar.
        print("{} Ana işlem tamamen farklı bir şey yapar\n".format(os.getpid()))
    else:
        # Çocuk işlem, ana işlemden ayrılarak kendi işlemini gerçekleştirir.
        print("{} Çocuk işlem bazı işler yapabilir\n".format(os.getpid()))

if __name__ == "__main__":
    main()
    sys.exit(0)