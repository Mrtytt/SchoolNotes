import os
import sys

def main():
    if os.fork():
        # Ebeveyn işlem zombie porcess'e dönüyor.
        print("Ebeveyn işlem çalışıyor, pid:", os.getpid())
        while True:
            pass
    else:
        # Çocuk işlem
        print("Çocuk işlem sonlandırılıyor, pid:", os.getpid())
        sys.exit(0)

if __name__ == "__main__":
    main() # Burada da main fonksiyojnunu çağırıyoruz
    sys.exit(0)