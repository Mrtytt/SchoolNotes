def filterSpecialPrimes(ustSinir):
    asalSayilar = []
    def isPrime(sayi):
        if sayi < 2:
            return False
        if sayi == 2:
            return True
        if sayi % 2 == 0:
            return False
        for i in range(3,int(sayi ** 0.5) + 1,2):
            if sayi % i == 0:
                return False
        return True
    def isPalindrom(sayi):
        strSayi = str(sayi)
        if strSayi[::-1] == strSayi:
            return True
        return False
    def sumOfDigits(sayi):
        sum = 0
        while sayi >= 1:
            if sayi < 10:
                sum += sayi
                break
            else:
                sum += sayi % 10
                sayi = sayi // 10
        return sum
    for i in range(0,ustSinir):
        if isPrime(i) and isPalindrom(i) == False and isPrime(sumOfDigits(i)):
            asalSayilar.append(i)
    return asalSayilar

# deneme = filterSpecialPrimes(150)
# print(deneme)

def detectPatternNumbers(start, end):
    numbers = []
    def sumOfDigits(number):
        return sum(int(c) for c in str(number))
    def isAsc(number):
        l = list(str(number))
        s = 0
        i = 0
        while i < len(l)-1:
            if l[i] < l[i+1]:
                s += 1
            i +=1
        if s == len(l)-1:
            return True
        else:
            return False
    for i in range(start,end):
        if sumOfDigits(i) % 2 == 0 and i % 9 == 0 and isAsc(i):
            numbers.append(i)
    return numbers

deneme2 = detectPatternNumbers(100,500)
print(deneme2)
        
        
