import threading
import time

# Bu bir sayaç, her iş parçacığı bu sayacı kullanıyor ve değerini arttırıyor.
counter = 0

def doSomeThing():
    # Bu fonksiyonda ilk önce sayac değerini bir arttırıyoruz. Daha sonra bir süre uyutup, iş parçalarının tamamlanması bekleriz.
    # Daha sonra da programı sonlandırırz.
    global counter
    counter += 1
    print("\n Job {} started\t thread:{}".format(counter, threading.currentThread().getName()))

    time.sleep(3)
    print("\n Job {} finished\t thread:{}".format(counter, threading.currentThread().getName()))

def main():
    i = 0
    # İş parçacıklarımız için bir liste oluşturuyoruz.
    threads = []

    # İki iş parçacığı oluşturacak şekilde bir döngü oluşturuyoruz.
    while i < 2:
        # İş parçacıklarının hedeflerini yukarıda belirttiğimiz doSomeThing fonksiyonu olarak belirliyoruz.
        t = threading.Thread(target=doSomeThing)
        # Oluşturulan iş parçacığı nesnesi threads listesine ekliyoruz.
        threads.append(t)
        # Her iş parçacığını başlatıyoruz.
        t.start()
        i += 1

    # Tüm iş parçacıkların bitmesi beklemek için join() fonksiyonunu kullanıyoruz
    for t in threads:
        t.join()

if __name__ == "__main__": # Burada main() fonksiyonumuzu çağırıyoruz.
    main()

