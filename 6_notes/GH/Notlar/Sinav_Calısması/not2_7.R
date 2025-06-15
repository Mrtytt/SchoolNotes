# -------------------------------------
# R Base Graphics - Grafik Cizimleri (Detayli Anlatim)
# -------------------------------------

# Bu bolumde R'in temel grafik sistemini (base graphics) kullanarak
# farkli turlerde grafikler cizecegiz ve ozellestirme seceneklerine bakacagiz.

# -------------------------------------
# Histogram Cizimi (Histogram Plot)
# -------------------------------------

# rnorm(n) fonksiyonu normal dagilimdan n adet deger uretir
# Burada 50 deger uretiyoruz
x <- rnorm(50)

# Histogram ile dagilimin yaklasik seklini gosteririz
hist(x, 
     main="Histogram: Normal Dagilimdan Ornekleme", # Grafik basligi
     xlab="Degerler",   # X ekseni etiketi
     col="skyblue")     # Cubuk rengi # nolint

# -------------------------------------
# Renk ve Baslik Ozellestirme
# -------------------------------------

# Histogrami bu kez kirmizi renkte ve farkli bir baslikla cizelim
hist(x, main <- "Merhaba Histogram!", col <- "red")

# -------------------------------------
# Dagilim Grafigi (Scatter Plot)
# -------------------------------------

# Yeni bir y vektoru olustur (50 rastgele deger)
y <- rnorm(50)

# Iki vektor arasinda iliskiyi gormek icin scatter plot kullanilir
plot(x, y, 
     main="Rassal Orneklerin Dagilim Grafigi", 
     xlab="x degerleri", 
     ylab="y degerleri",
     col="darkgreen")

# -------------------------------------
# Kutu Grafigi (Boxplot)
# -------------------------------------

# Boxplot, verinin medyan, çeyrekler ve aykiri degerlerini gostermek icin kullanilir
boxplot(x, y, 
        main="Kutu Grafigi: x ve y Vektorleri",
        names = c("x","y"),
        col = c("orange", "lightblue"))

# -------------------------------------
# Cubuk Grafigi (Bar Plot)
# -------------------------------------

# Yuzdelik degerler ornek olarak alindi
perc <- c(50, 70, 35, 25)

# Barplot ile oransal dagilim gosterimi
barplot(height = perc,
        names.arg = c("CpGi","Exon","CpGi","Exon"),
        ylab = "Yuzdeler",
        main = "Hayali Yuzdelik Dagilim",
        col = c("red", "red", "blue", "blue"))

# Grafik uzerine aciklayici bir legenda ekleyelim
legend("topright",
       legend = c("Test", "Kontrol"),
       fill = c("red", "blue"))

# -------------------------------------
# Ekstra: Grafik Ozellestirme Ipuclari
# -------------------------------------

# ?plot ve ?par komutlari ile R'in grafik parametrelerine bakilabilir
# ornegin: par(mfrow=c(2,2)) birden fazla grafiği ayni anda göstermek icin kullanilir
# renk secenekleri icin colors() fonksiyonu kullanilarak R'deki tum renk adlari gorulebilir

