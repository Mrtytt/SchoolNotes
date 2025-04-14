# -------------------------------------
# VERİ TİPLERİ (Data Types)
# -------------------------------------
# R'de yaygın olarak kullanılan 4 temel veri tipi vardır:
# numeric (sayısal), logical (mantıksal), character (karakter) ve integer (tam sayı)

# Sayısal vektör
x <- c(1, 3, 2, 10, 5)
x

# Mantıksal vektör
x <- c(TRUE, FALSE, TRUE)
x

# Karakter vektör
x <- c("sds", "sd", "as")
x
class(x)  # Tür kontrolü

# Tam sayı (integer) vektör
x <- c(1L, 2L, 3L)
x
class(x)

# -------------------------------------
# VERİ OKUMA VE YAZMA (Reading and Writing Data)
# -------------------------------------
# Genom verileri çoğunlukla BED dosya formatında olur (kromozom, başlangıç, bitiş, yön, skor gibi sütunlarla)
# BED formatı birçok genom tarayıcısı tarafından desteklenir (örneğin UCSC)

# read.table() fonksiyonu ile tablo formatında veri okunabilir

enhancerFilePath <- system.file("extdata", "subset.enhancers.hg18.bed", package="compGenomRData")
cpgiFilePath <- system.file("extdata", "subset.cpgi.hg18.bed", package="compGenomRData")

# BED dosyalarını oku
enh.df <- read.table(enhancerFilePath, header = FALSE)
cpgi.df <- read.table(cpgiFilePath, header = FALSE)

# İlk satırlara bakarak veriyi incele
head(enh.df)
head(cpgi.df)

# Veriyi dosyaya yazma (write.table())
# NOT: eval=FALSE olduğu için çalıştırılmadan örnek gösterimdir
# write.table(cpgi.df, file="cpgi.txt", quote=FALSE, row.names=FALSE, col.names=FALSE, sep="\t")

# R nesnelerini kaydetme (save, saveRDS)
# Tek ya da çok sayıda nesne kaydedilebilir
# save() ile nesne isimleri korunur; load() ile geri yüklenir
# saveRDS() ile nesne isimsiz saklanır, readRDS() ile yüklenir

# save(cpgi.df, enh.df, file="mydata.RData")
# load("mydata.RData")
# saveRDS(cpgi.df, file="cpgi.rds")
# x <- readRDS("cpgi.rds")
# head(x)

# -------------------------------------
# BÜYÜK DOSYALARI OKUMA (Reading Large Files)
# -------------------------------------
# read.table() büyük dosyalar için yavaş olabilir, alternatif paketler:
# - data.table
# - readr

# Örnek kullanım (eval=FALSE):
# library(data.table)
# df.f <- fread(enhancerFilePath, header = FALSE, data.table = FALSE)

# library(readr)
# df.f2 <- read_table(enhancerFilePath, col_names = FALSE)
