# R Veri Yapıları Notları (Türkçe Açıklamalı)

# -------------------------------------
# VEKTÖRLER Vectors
# -------------------------------------
# Vektörler, R'nin temel veri yapılarından biridir.
# Aynı türde (sayısal, karakter veya mantıksal) elemanlardan oluşan dizilerdir.
# Genellikle bir tabloya ait sütunlar vektör olarak temsil edilir.

x <- c(1, 3, 2, 10, 5)    # Sayılardan oluşan bir vektör oluştur
x = c(1, 3, 2, 10, 5)     # Alternatif atama yöntemi
x                         # Vektörü yazdır

y <- 1:5                  # 1'den 5'e kadar ardışık sayılardan oluşan vektör

# Vektörlerle temel işlemler
y + 2                     # Her elemana 2 ekler
2 * y                     # Her elemanı 2 ile çarpar
y^2                       # Her elemanı karesini alır
2^y                       # 2'nin her elemana karşılık gelen kuvvetini alır
y                         # y değişmedi

y <- y * 2                # y'yi güncelledik
y

# Diğer vektör fonksiyonları
r1 <- rep(1, 3)           # 3 tane 1'den oluşan vektör
length(r1)                # Vektörün uzunluğu
class(r1)                 # Vektörün tipi/sınıfı
a <- 1                    # Tek değerli bir vektör de mümkündür

# -------------------------------------
# MATRİSLER (Matrices)
# -------------------------------------
# Matrisler, sayısal değerlerden oluşan iki boyutlu yapılardır.
# Satırlar ve sütunlardan oluşur. Her satır/sütun bir vektör gibidir.

x <- c(1, 2, 3, 4)
y <- c(4, 5, 6, 7)
m1 <- cbind(x, y)         # İki vektörü sütunlar halinde birleştirerek matris oluştur
m1

t(m1)                     # Matrisin transpozunu al
dim(m1)                   # Matrisin boyutlarını verir (satır x sütun)

# Doğrudan matris oluşturma
m2 <- matrix(c(1, 3, 2, 5, -1, 2, 2, 3, 9), nrow = 3)
m2

# -------------------------------------
# VERİ ÇERÇEVELERİ (Data Frames)
# -------------------------------------
# Veri çerçeveleri matrislerden daha geneldir.
# Sütunlar farklı veri türlerinde olabilir (sayısal, karakter, faktör vb.).

chr <- c("chr1", "chr1", "chr2", "chr2")
strand <- c("-", "-", "+", "+")
start <- c(200, 4000, 100, 400)
end <- c(250, 410, 200, 450)

# Veri çerçevesi oluşturma
mydata <- data.frame(chr, start, end, strand)
# Sütun isimlerini değiştirme
names(mydata) <- c("chr", "start", "end", "strand")
mydata

# Alternatif oluşturma yöntemi
mydata <- data.frame(chr = chr, start = start, end = end, strand = strand)
mydata

# Veri çerçevesinden veri seçme (alt kümeleme)
mydata[, 2:4]                 # 2, 3 ve 4. sütunları seç
mydata[, c("chr", "start")] # Belirtilen sütunları ada göre seç
mydata$start                 # 'start' sütununu seç
mydata[c(1, 3), ]            # 1. ve 3. satırları al
mydata[mydata$start > 400, ] # 'start' değeri 400'den büyük olan satırları filtrele

# -------------------------------------
# LİSTELER (Lists)
# -------------------------------------
# Listeler, farklı türde verileri bir arada tutmamıza olanak sağlar.
# Her bileşen farklı türde ve yapıda olabilir (vektör, matris, sayı, metin vb.).

w <- list(
  name = "Fred",
  mynumbers = c(1, 2, 3),
  mymatrix = matrix(1:4, ncol = 2),
  age = 5.3
)
w

# Liste elemanlarına erişim
w[[3]]            # 3. eleman (mymatrix)
w[["mynumbers"]] # İsme göre erişim
w$age             # $ işareti ile erişim (yaş bilgisi)

# -------------------------------------
# FAKTÖRLER (Factors)
# -------------------------------------
# Faktörler, kategorik verileri saklamak için kullanılır.
# Özellikle istatistiksel modellerde önemlidir.

features <- c("promoter", "exon", "intron")
f.feat <- factor(features)
f.feat

# NOT: Eğer read.table() veya data.frame() ile veri okurken karakter sütunlarının faktör olarak gelmesini istemiyorsanız,
# stringsAsFactors = FALSE parametresini kullanın.

