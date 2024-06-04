import os
import mmap
import struct

# Burada POSIX IPC nesnesinin adını belirtiyoruz. Bu paylaşılan bellek segmentinin yolunu belirliyor.
SHMOBJ_PATH = "/foo1423"
# Burada mesajın maksimum uzunluğunu belirliyoruz.
MAX_MSG_LENGTH = 50
# Burada mesaj türünü belirtiyoruz.
TYPES = 8

# Burada mesaj sınıfını tanımlıyoruz. Her bir mesaj bir tip ve içerik içerir.
class Msg:
    def __init__(self):
        self.type = 0
        self.content = b"\0" * MAX_MSG_LENGTH

def main():
    # Burada paylaşılan bellek segmentinin boyunu hesaplıyoruz. Tek bir mesajı saklamak için yeterli bir boyut belirlenir.
    shared_seg_size = 1 * struct.calcsize(Msg)  

    # Bellek segmentini açıyoruz, O_RDWR fonksiyonu segmenti okuma ve yazma işlemi açar.
    shmfd = os.open(SHMOBJ_PATH, os.O_RDWR)
    if shmfd < 0:
        print("In shm_open()")
        exit(1)
    print(f"Created shared memory object {SHMOBJ_PATH}")

    # Burada segmenti belleğe haritalıyoruz. Bu sayede segmente erişim sağlanır.
    # Burada with kullanarak belirli bir işlem sona erdiğinde bellek haritasını otomatik olarak kapanmasını sağlıyoruz.
    with mmap.mmap(shmfd, shared_seg_size, access=mmap.ACCESS_READ | mmap.ACCESS_WRITE) as shared_msg:
        # Bu değişken mesajı depolamak için bir Msg nesnesi oluşturur.
        shared_msg_obj = Msg()
        # Burada segmentteki bir nesneyi çözümlüyoruz. Örn:Yukarıda oluşturduğumuz
        struct.unpack_into(shared_msg_obj.__class__.__name__, shared_msg, 0, shared_msg_obj)
        print(f"Message type is {shared_msg_obj.type}, content is: {shared_msg_obj.content.decode().strip()}")

    return 0

if __name__ == "__main__": # Burada main() fonksiyonumuzu çağırıyoruz.
    main()

