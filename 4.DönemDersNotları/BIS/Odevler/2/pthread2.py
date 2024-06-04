import threading
import time

# Her bir Hello World string'ini mesajlar listesine ekliyoruz. 
messages = [
    "English: Hello World!",
    "French: Bonjour, le monde!",
    "Spanish: Hola al mundo",
    "Klingon: Nuq neH!",
    "German: Guten Tag, Welt!"
]

# İş parçacığı sınıf oluşturup değerleri almasını sağlıyoruz
class ThreadData:
    def __init__(self, thread_id, sum, message):
        self.thread_id = thread_id
        self.sum = sum
        self.message = message

def print_hello(thread_data):
    time.sleep(1) # Uygulamanın 1 saniye uyumasını sağlıyoruz
    print(f"Thread {thread_data.thread_id}: {thread_data.message} Sum={thread_data.sum}") # O iş parçacığının id, mesaj ve toplam değerini ekrana yazdırıyoruz.

def main():
    threads = [] # İş parçacıkları listemiz
    sum = 0 # Toplam

    for i in range(len(messages)):
        sum += i # Toplam değeri kümülatif olarak arttırıyoruz
        thread_data = ThreadData(i, sum, messages[i]) # İş parçacıklarımızın değerlerini giriyoruz
        thread = threading.Thread(target=print_hello, args=(thread_data,)) # İş parçacıklarını oluşturuyoruz
        threads.append(thread)
        thread.start()

    # İş parçacıklarının bitmesini bekliyoruz.
    for thread in threads: 
        thread.join()

if __name__ == "__main__":
    main()

"""
Açıklamalar:
1. messages listesi: Her bir "Hello World" mesajını farklı dillerde içeren bir liste oluşturuluyor.
2. ThreadData Sınıfı: İş parçacıkları için thread_id, sum ve message değerlerini tutan bir sınıf oluşturuluyor.
3. print_hello Fonksiyonu: Bu fonksiyon, bir ThreadData örneğini alıyor, 1 saniye uyuyor ve ardından o iş parçacığının bilgilerini ekrana yazdırıyor.
4. main Fonksiyonu: 
    - İş parçacıklarını tutmak için bir liste oluşturuluyor.
    - Toplam değeri toplam olarak başlatılıyor.
    - Mesajlar listesi üzerinde iterasyon yapılarak her bir mesaj için ThreadData örneği oluşturuluyor.
    - Her bir ThreadData örneği ile yeni bir iş parçacığı başlatılıyor ve bu iş parçacığı listeye ekleniyor.
    - Son olarak, tüm iş parçacıklarının bitmesini beklemek için join fonksiyonu kullanılıyor.
5. Programın Ana Kısmı: main fonksiyonu, programın çalıştırıldığı kısımdır ve doğrudan çalıştırıldığında main fonksiyonunu çağırır.
"""