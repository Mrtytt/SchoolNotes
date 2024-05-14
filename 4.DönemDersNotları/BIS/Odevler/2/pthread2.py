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

