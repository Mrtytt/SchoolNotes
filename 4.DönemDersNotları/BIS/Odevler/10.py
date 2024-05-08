import os
import sys
import errno

num_of_childs = 5

def main():
    pid = []
    # Belirtilen sayıda çocuk işlem oluışturuluyor
    for i in range(num_of_childs):
        new_pid = os.fork()
        if new_pid == 0:
            # Çocuk işlem
            os._exit(100 + i)
        else:
            # Ana işlem, çocuk işlem PID'sini listeye ekliyor
            pid.append(new_pid)

    # Tüm çocuk işlemlerin tamamlanması bekleniyor
    for _ in range(num_of_childs):
        wpid, child_status = os.wait()
        if os.WIFEXITED(child_status):
            # Çocuk işlem normal şekilde sonlandıysa çıktı veriliyor
            print(f"Çocuk {wpid} çıkış durumuyla sonlandı: {os.WEXITSTATUS(child_status)}")
        else:
            # Çocuk işlem anormal şekilde sonlandıysa çıktı veriliyor
            print(f"Çocuk {wpid} anormal şekilde sonlandı")

if __name__ == "__main__":
    main() # Burada da main fonksiyonunu çağırıyoruz
    sys.exit(0)

