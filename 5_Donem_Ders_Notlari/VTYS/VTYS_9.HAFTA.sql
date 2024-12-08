-- Sütun Ekleme (ADD)
ALTER TABLE table_name ADD new_column_name column_definition
-- AFTER komutu verilen sütunun sonraki sütuna ekler
ALTER TABLE contacts ADD last_name varchar(40) NOT NULL AFTER contact_id
ALTER TABLE yazar ADD yazarno INT IDENTITY(1,1)
-- Sütun Çýkarma (DROP)
ALTER TABLE tablo_adi DROP COLUMN sütun_adi
ALTER TABLE yazar DROP COLUMN sütun1,sütun2
-- Sütun Veri Türü Deðiþtirme (ALTER)
ALTER TABLE tablo_adi ALTER COLUMN sütun_adi veri_türü
ALTER TABLE yazar ALTER COLUMN yazarad varchar(25)
ALTER TABLE yazar ALTER COLUMN yazarad varchar(25) NULL
-- Kýsýtlama ekleme (ADD - DROP)
ALTER TABLE tablo_adi ADD CONSTRAINT kisit_adi UNIQUE(sütun_adi)
ALTER TABLE yazar ADD CONSTRAINT tcno_kisit UNIQUE(tcno)
ALTER TABLE tablo_adi ADD CONSTRAINT kisit_adi PRIMARY KEY(sütun_adi)
ALTER TABLE tablo_adi DROP CONSTRAINT kisit_adi
-- Tablo - Sütun Kalýcý Olarak Adýný Deðiþtirme
sp_rename 'yazar','yazarlar'
sp_raname 'yazar.yazarad','yazar.yazarsoyad' (Týrnak olmadan da kullanýlabilir.)
EXEC komutu eklenerek çalýþtýrýlabilirler.
-- DROP
-- Veritabaný nesneleri ve veritabanýný komple kaldýrýr atar.
DROP TABLE table_name
DROP TABLE customers
DROP TABLE IF EXISTS customers,suppliers
-- UPDATE
UPDATE tablo_ismi SET yeni_deðer WHERE kosul_adi
UPDATE personel SET maas = 5000 WHERE id = 1;
-- Concat()
-- Deðerleri birleþtirmek için kullanýlýr.
Concat('deg1','deg2',sütun1,sütun2)
Select concat(ad,soyad) as ADSOYAD from TABLO
-- Substring()
-- Veriden istenen kýsmýn alýnmasýný saðlar.
Substring(veri,baslangic,karakter)
Select substring('metin bilgin',6,6)
Select substring(yazarad,1,3) as Adý_Soyadý from yazar
-- LEFT(): Metnin solundan istenilen kadar karakter alýr
SELECT LEFT('Merhaba Dünya', 3) AS Sol_Karakterler;
-- RIGHT(): Metnin saðýndan istenilen kadar karakter alýr
SELECT RIGHT('Merhaba Dünya', 5) AS Sag_Karakterler;
-- LOWER(): Metni küçük harfe çevirir
SELECT LOWER('Merhaba Dünya') AS Kucuk_Harfler;
-- UPPER(): Metni büyük harfe çevirir
SELECT UPPER('Merhaba Dünya') AS Buyuk_Harfler;
-- TRIM(): Baþtaki ve sondaki boþluklarý kaldýrýr
SELECT TRIM('   Merhaba Dünya   ') AS Trimli_Metin;
-- LTRIM(): Sadece baþtaki boþluklarý kaldýrýr
SELECT LTRIM('   Merhaba Dünya   ') AS Bas_Bosluk_Temizle;
-- RTRIM(): Sadece sondaki boþluklarý kaldýrýr
SELECT RTRIM('   Merhaba Dünya   ') AS Son_Bosluk_Temizle;
-- LEN() : Verinin karakter sayýsýný bulur.
SELECT LEN('Merhaba Dünya') AS Uzunluk;
-- REPLACE() : Veriyi baþka bir deðerle deðiþtirir
SELECT REPLACE('Merhaba Dünya', 'Merhaba', 'Selam') AS Degistirilmis_Metin;
SELECT isim, REPLACE(isim, 'Ahmet', 'Mehmet') AS Yeni_Isim FROM personel;
-- CHARINDEX() : Aranan dize bulunduðunda, o dizenin baþladýðý pozisyonun ilk karakterinin indeksini döner. Eðer aranan dize bulunamazsa, 0 döner.
CHARINDEX(search_expression, expression, [start_location])
SELECT CHARINDEX('cat', 'concatenate')
-- Reverse() : 
SELECT REVERSE('Hello')