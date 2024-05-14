import os
import sys
import time
from multiprocessing import Semaphore
from datetime import datetime

# Burada paylaşılan bellek segmentinin adını belirliyoruz.(Buna ileride direkt semafor diyeceğim)
SEM_NAME = "/vik"

def main():
    i = 0
    mutex = None

    try:
        # Semafor nesnesini oluşturup mutex değişkenine atıyoruz.
        # Bu nesne ile kiritk bölgeye giriş ve çıkışlarını kontrol ediyoruz.
        mutex = Semaphore(0)
        # Semafora kilitleme işlemi yapıyoruz.
        mutex.acquire()
    except Exception as e:
        print(f"reader: unable to execute semaphore: {e}")
        sys.exit(-1)

    while i < 10:
        # Semafora kilitleme işlemi yapıyoruz.
        mutex.acquire()
        # Burada geçerli zamanı alıyoruz.
        t0 = datetime.now()
        print(f"Process B enters the critical section at {t0.microsecond % 1000000}")
        t1 = datetime.now()
        print(f"Process B leaves the critical section at {t1.microsecond % 1000000}")
        # Semaforu serbest bırakıyoruz
        mutex.release()
        i += 1
        # Sistemi 2 sn boyunca uyutuyoruz.
        time.sleep(2)

    # Semaforu serbest bırakıyoruz
    mutex.release()

    sys.exit(0)

if __name__ == "__main__": # Burada main() fonksiyonumuzu çağırıyoruz.
    main()
