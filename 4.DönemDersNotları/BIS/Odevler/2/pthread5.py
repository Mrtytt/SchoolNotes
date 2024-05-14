import random
import threading

# Burada oluşturulacak olan iş parçacığı sayısını ve her bir iş parçacığı için yapılacak toplama işlemi sayısını belirler.
NUM_THREADS = 4
ITERATIONS = 1000000

# Bu fonksiyonda rastgele değerler üretip iterasyon sayısı kadar toplama işlemi yapıyoruz
def busy_work(tid):
    result = 0.0
    print(f"Thread {tid} starting...")
    for _ in range(ITERATIONS):
        result += random.random()
    # Burada da hangi thredin hangi sonucu ürettiğini yazdırıyoruz.
    print(f"Thread {tid} done. Result = {result:.2f}")

def main():
    # İş parçacıklarımız için bir liste oluşturuyoruz.
    threads = []
    for t in range(NUM_THREADS):
        # İş parçacıklarının hedeflerini yukarıda belirttiğimiz fonksiyon olarak belirliyoruz.
        thread = threading.Thread(target=busy_work, args=(t,))
        # İş parçacıklarının ana iş parçacığı tamamlanmasıyla sonlanması için deamon olark belirtiyoruz.
        thread.daemon = True
        # İş parçacıklarını başlatıyoruz.
        thread.start()
        threads.append(thread)
    # Fonksiyonun bittiğini belirtiyoruz.
    print("Main: program completed. Exiting.")

if __name__ == "__main__": # Main fonksiyonunu çağırıyoruz.
    main()

