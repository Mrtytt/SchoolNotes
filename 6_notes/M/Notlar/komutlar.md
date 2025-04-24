# AAA
- Toplama sonrası ASCII düzenlemesi yapar. (AH ve AL)
- **ADC**
    - Toplama yapar.
- **DAA**
    - Toplamadan sonra ondalık düzenlemesi yapar. İki BCD...

# AAD
- Bölme işlemi sonucu ASCII düzenlemesi yapar.
- **DIV**
    - İşaretsiz bölme işlemi yapar.

# AAM
- Çarpma sonrasında ASCII düzenlemesini yapar.

# AAS 
- Çıkarma sonrasında ASCII düzenlemsini yapar.
- **DAS**
    - Çıkartmadan sonra ondalık düzenlemesini yapar. İki BCD...

# AND 
- İki operand arasında mantıklsal **VE** işlemi yapar.

# CALL 
- Bir prosedürü çağırır ve dönüş adresini stack'e push eder.

# CBW
- Byte değerini word'e çevirir.

# Flag

## CLC
- Carry flag sıfırlanır.

## CLD 
- Direction Flag sıfırlanır.

## CLI 
- Interrupt enable flag sıfırlanır.

## CMC 
- Carry flag terslenir 0 => 1

# Karşılaştırma
## CMP 
- Karşılatırma yapar soldaki operand'ı sağdakinden çıkartır ancak operandlar değişmez sadece bayrak bitleri değişir.

## CMPSB
- ES:[DI] ile DS:[SI] arasında bayt karşılaştırır.

## CMPSW
- Word karşılaştırır.

# CWD
- İşaretli sayılarda word boyutunu doubleword boyutuna genişletir.

# DEC
- Azaltma işlemi yapar.

# HLT
- Programı kapatır.