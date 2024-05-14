import getopt
import os
import sys
import time
from typing import Tuple
from mqueue import mq_open, mq_close, mq_send

# Mesaj kuyruğu adını ve maksimum mesaj uzunluğunu tanımlıyoruz.
MSGQOBJ_NAME = "/test"
MAX_MSG_LEN = 70

def main() -> int:
    msg_prio = 0
    my_pid = os.getpid()
    msg_content = ""
    create_queue = False

    # Bu kodda, kullanıcıdan -q seçeneği ile kuyruk oluşturmayı ve -p ile mesaj önceliği belirtmeyi bekliyoruz.
    opts, _ = getopt(sys.argv[1:], "qp:")
    for opt, arg in opts:
        # -q girilmişse kuyruk oluştururuz
        if opt == "-q":
            create_queue = True
        # -p girilmişse öncelik değeri atarız.
        elif opt == "-p":
            msg_prio = int(arg)
            print(f"I ({my_pid}) will use priority {msg_prio}")
        else:
            print(f"Usage: {sys.argv[0]} [-q] -p msg_prio -- ch : {opt}")
            return 1

    if msg_prio == 0:
        print(f"Usage: {sys.argv[0]} [-q] -p msg_prio")
        return 1

    try:
        # Burada kuyruk oluşturulur eğer kuyruk yoksa varolan bir kuyruk açılır.
        if create_queue:
            msg_queue = mq_open(MSGQOBJ_NAME, os.O_RDWR | os.O_CREAT | os.O_EXCL, 0o700, None)
        else:
            msg_queue = mq_open(MSGQOBJ_NAME, os.O_RDWR)
    except OSError as e:
        print(f"In mq_open(): {e}")
        return 1

    curr_time = time.time()
    # Burada mesaj içeriğini oluştururuz, değerler id ve mevcut değeri alır.
    msg_content = f"Hello from process {my_pid} (at {time.ctime(curr_time)})."

    # Burada mesaj değerini göndeririz encode() ile onu bayt türüne dönüştürürüz.
    mq_send(msg_queue, msg_content.encode(), msg_prio)

    # Burada mesaj kuyruğunu kapatıyoruz.
    mq_close(msg_queue)

    return 0

# Burada da main fonksiyonunu çağırıyoruz
if __name__ == "__main__":
    sys.exit(main())

