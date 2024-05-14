import os
import mmap
import time
import string
from mqueue import mq_open, mq_close, mq_send

# Bir önceki örnekteki gibi mesaj kuyruğu adını ve maksimum mesaj uzunluğunu tanımlıyoruz. 
MSGQOBJ_NAME = "/test"
MAX_MSG_LEN = 10000

def main():
    try:
        # Burada mesaj kuyruğunu açıyoruz, O_RDWR işlemi mesaj kuyruğunu okuma ve yazma için açıyor. Açılmazsa ERROR döndürüyor
        msgq_id = os.mq_open(MSGQOBJ_NAME, os.O_RDWR)
    except OSError as e:
        print(f"In mq_open(): {e}")
        return 1

    # Burada id'si verilen kuyruğun niteliklerini alıp ekrana yazdırıyoruz
    msgq_attr = os.mq_getattr(msgq_id)
    print(f"Queue \"{MSGQOBJ_NAME}\":\n\t- stores at most {msgq_attr.mq_maxmsg} messages\n\t- large at most {msgq_attr.mq_msgsize} bytes each\n\t- currently holds {msgq_attr.mq_curmsgs} messages")

    # Kuyruktan bir mesaj alıyoruz, alınan mesajın bayt dizisi ve mesajı gönderenin kimliğini döndürüyoruz.
    try:
        msgsz, sender = os.mq_receive(msgq_id, MAX_MSG_LEN)
        msgcontent = msgsz.decode()
        print(f"Received message ({len(msgcontent)} bytes) from {sender}: {msgcontent}")
    except OSError as e:
        print(f"In mq_receive(): {e}")
        return 1

    # Mesaj kuyruğunu kapatıyoruz.
    os.mq_close(msgq_id)
    # Mesaj kuyruğunu siliyoruz.
    os.mq_unlink(MSGQOBJ_NAME)

    return 0

if __name__ == "__main__": # Main fonksiyonunu çağırıyoruz.
    exit(main())

