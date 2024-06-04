import os
import mmap
import random
import time
from ctypes import Structure, c_int, c_char, sizeof

# Burada POSIX IPC nesnesinin adını belirtiyoruz. Bu paylaşılan bellek segmentinin yolunu belirliyor.
SHMOBJ_PATH = "/foo1423"
# Burada mesajın maksimum uzunluğunu belirliyoruz.
MAX_MSG_LENGTH = 50
# Burada mesaj türünü belirtiyoruz.
TYPES = 8

# Burada msg_s sınıfını tanımladık. Bu sınıf tür ve içerik içerir.
class msg_s(Structure):
    _fields_ = [("type", c_int),
               ("content", c_char * MAX_MSG_LENGTH)]

def main():
    # Burada paylaşılan bellek segmentinin boyunu hesaplıyoruz. Tek bir mesajı saklamak için yeterli bir boyut belirlenir.
    shared_seg_size = (1 * sizeof(msg_s))   
    
    # Bellek segemntini açıyoruz, O_RDWR fonksiyonu segmenti okuma ve yazma işlemi açar.
    # O.CREAT nesneyi oluştururken, O.EXCL işlemi nesnenin önceden var olup olmadığını kontrol eder.
    shmfd = os.open(SHMOBJ_PATH, os.O_CREAT | os.O_EXCL | os.O_RDWR, 0o600)
    if shmfd < 0:
        print("In shm_open()")
        exit(1)
    print(f"Created shared memory object {SHMOBJ_PATH}")
    
    # Burada segmentin boyutunu belirliyoruz. Harita oluşmadan önce bunu yapıyoruz.
    os.ftruncate(shmfd, shared_seg_size)

    # Burada segmenti belleğe haritalıyoruz. Bu sayede segmente erişim sağlanır.
    shared_msg = mmap.mmap(shmfd, shared_seg_size, access=mmap.ACCESS_WRITE)
    if shared_msg is None:
        print("In mmap()")
        exit(1)
    print(f"Shared memory segment allocated correctly ({shared_seg_size} bytes).")
    
    # Burada zaman fonksiyonunu kullanarak rastgele sayı üretiyoruz.
    random.seed(time.time())
    
    # Burada mesajın türünü ve içeriğini belirliyoruz.
    shared_msg.type = random.randint(0, TYPES - 1)
    shared_msg.content = f"My message, type {shared_msg.type}, num {random.randint(0, 1000000)}".encode()

if __name__ == "__main__": # Burada main() fonksiyonumuzu çağırıyoruz.
    main()