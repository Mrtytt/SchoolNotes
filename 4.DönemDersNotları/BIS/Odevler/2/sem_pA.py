import sys
import os
import time
from datetime import datetime

# Burada paylaşılan bellek segmentinin adını ve boyutunu belirliyoruz.(Buna ileride direkt semafor diyeceğim)
SHMSZ = 27
SEM_NAME = "vik"


def main():
    i = 0
    key = 1000
    # Burada mutex değişkeni semaforu temsil eder.
    mutex = None

    try:
        # Burada sem_open() fonksiyonu semaforu oluşturur veya açar.
        # O_CREAT() fonksiyonu semaforu oluşturur. İkinci argüman ise semaforun erişim izinlerini belirler.
        mutex = os.sem_open(SEM_NAME, os.O_CREAT, 0o644, 1)
    except OSError:
        print("unable to create semaphore")
        os.sem_unlink(SEM_NAME)
        sys.exit(-1)

    while i < 10:
        # Burada kritik bölgeye girmek için semaforu bekliyoruz.
        os.sem_wait(mutex)
        t0 = time.time()
        print(f"Process A enters the critical section at {int(t0 * 1000) % 1000000}")
        t1 = time.time()
        print(f"Process A leaves the critical section at {int(t1 * 1000) % 1000000}")
        # Kritik bölgeden çıktıktan sonra semaforu serbest bırakıyoruz.
        os.sem_post(mutex)
        i += 1
        time.sleep(3)

    # Burada semaforu kapatıyoruz.
    os.sem_close(mutex)
    # Burada semaforu siliyoruz.
    os.sem_unlink(SEM_NAME)
    sys.exit(0)

if __name__ == "__main__": # Burada main() fonksiyonumuzu çağırıyoruz.
    main()

