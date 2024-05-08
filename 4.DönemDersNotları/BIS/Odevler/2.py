import os
import sys

def main():
    print("Process id :",os.getpid()) # Çağıran işlemin işlem tanıtıcısını öğrendik.
    forkResult = os.fork() # Fork fonksiyonunu çağırdık.
    print("Process id : {} - result: {}".format(os.getpid(),forkResult)) # Çağıran işlemin işlem tanıtıcısını ekrana yazdırdık.

if __name__ == "__main__":
    main() # Main fonksiyonunu çağırdık.
    sys.exit(0)
