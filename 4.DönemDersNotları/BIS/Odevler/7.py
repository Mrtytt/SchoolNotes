import os
import sys

MAX_LINE = 80

def setup(inputBuffer, args):
    # Arka planda çalışıp çalışmayacağını belirleyen bir işaret.
    background = 0
    length = len(inputBuffer)
    start = -1
    ct = 0

    for i in range(length):
        if inputBuffer[i] == ' ' or inputBuffer[i] == '\t':
            if start != -1:
                args[ct] = inputBuffer[start:i]
                ct += 1
            inputBuffer[i] = '\0'
            start = -1
        elif inputBuffer[i] == '\n':
            if start != -1:
                args[ct] = inputBuffer[start:i]
                ct += 1
            inputBuffer[i] = '\0'
            args[ct] = None
        elif inputBuffer[i] == '&':
            # Arka planda çalıştırılacaksa, işareti 1 yapar.
            background = 1
            inputBuffer[i] = '\0'
        else:
            if start == -1:
                start = i

    args[ct] = None

    return background

def main():
    while True:
        background = 0
        # Kullanıcıdan komut girdisi alır.
        inputBuffer = input("COMMAND->")
        args = inputBuffer.split()
        background = setup(inputBuffer, args)

        # Bir çocuk işlem oluşturma
        pid = os.fork()

        if pid < 0:
            sys.exit("Fork failed")
        elif pid == 0:  # Çocuk işlem
            # Çocuk işlem, girilen komutu yürütür.
            os.execvp(args[0], args)
            sys.exit("Execution failed")
        else:  # Ana işlem
            if background == 0:
                # Arka planda çalışmayacaksa, çocuk işleminin tamamlanmasını bekler.
                os.wait()

if __name__ == "__main__":
    main() # Burada da main fonksiyojnunu çağırıyoruz
    sys.exit(0)