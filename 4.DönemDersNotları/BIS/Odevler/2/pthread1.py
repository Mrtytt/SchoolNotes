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

def print_hello(thread_id):
    time.sleep(1)  # Uygulamanın 1 saniye uyumasını sağlıyoruz
    print(f"Thread {thread_id}: {messages[thread_id]}")

def main():
    threads = []
    
    # Her bir mesaj için iş parçacığı oluşturuyoruz
    # İş parçacıkları için bir id değeri atıyoruz.
    for i in range(len(messages)):
        thread = threading.Thread(target=print_hello, args=(i,))
        threads.append(thread)
        thread.start()

    # Bütün iş parçacıklarının bitmesini bekliyoruz
    for thread in threads:
        thread.join()

if __name__ == "__main__": # Main fonksiyonunu çağırırız. 
    main()

"""
Bu Python kodu, çoklu iş parçacığı 
kullanarak çeşitli dillerde "Hello World" 
mesajlarını ekrana yazdırır. İlk olarak, farklı 
dillerde mesajları içeren bir liste oluşturulur. 
Ardından, her bir mesaj için bir iş parçacığı oluşturan 
'print_hello' fonksiyonu tanımlanır. Bu fonksiyon, 
bir saniye bekledikten sonra iş parçacığının kimliği ve 
mesajı ekrana yazdırır. 'main' fonksiyonunda, tüm mesajlar için 
iş parçacıkları oluşturulup başlatılır ve 
her bir iş parçacığının tamamlanması beklenir. En sonunda, 
'if name == "main":' koşulu ile 'main' fonksiyonu çağrılır ve 
program çalıştırıldığında iş parçacıkları eşzamanlı olarak mesajları ekrana yazdırır.
"""
