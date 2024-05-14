import os 
import sys

def main():
    print("Message before fork.") # Fork fonksiyonundan önce ekrana mesaj veriyoruz.
    os.fork() # Fork fonksiyonu
    print("Message after fork.") # Fork fonksiyonundan sonra ekrana mesaj veriyoruz.

if __name__ == "__main__":
    main() # Burada da main fonksiyojnunu çağırıyoruz
    sys.exit(0)
