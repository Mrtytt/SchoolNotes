-- S�tun Ekleme (ADD)
ALTER TABLE table_name ADD new_column_name column_definition
-- AFTER komutu verilen s�tunun sonraki s�tuna ekler
ALTER TABLE contacts ADD last_name varchar(40) NOT NULL AFTER contact_id
ALTER TABLE yazar ADD yazarno INT IDENTITY(1,1)
-- S�tun ��karma (DROP)
ALTER TABLE tablo_adi DROP COLUMN s�tun_adi
ALTER TABLE yazar DROP COLUMN s�tun1,s�tun2
-- S�tun Veri T�r� De�i�tirme (ALTER)
ALTER TABLE tablo_adi ALTER COLUMN s�tun_adi veri_t�r�
ALTER TABLE yazar ALTER COLUMN yazarad varchar(25)
ALTER TABLE yazar ALTER COLUMN yazarad varchar(25) NULL
-- K�s�tlama ekleme (ADD - DROP)
ALTER TABLE tablo_adi ADD CONSTRAINT kisit_adi UNIQUE(s�tun_adi)
ALTER TABLE yazar ADD CONSTRAINT tcno_kisit UNIQUE(tcno)
ALTER TABLE tablo_adi ADD CONSTRAINT kisit_adi PRIMARY KEY(s�tun_adi)
ALTER TABLE tablo_adi DROP CONSTRAINT kisit_adi
-- Tablo - S�tun Kal�c� Olarak Ad�n� De�i�tirme
sp_rename 'yazar','yazarlar'
sp_raname 'yazar.yazarad','yazar.yazarsoyad' (T�rnak olmadan da kullan�labilir.)
EXEC komutu eklenerek �al��t�r�labilirler.
-- DROP
-- Veritaban� nesneleri ve veritaban�n� komple kald�r�r atar.
DROP TABLE table_name
DROP TABLE customers
DROP TABLE IF EXISTS customers,suppliers
-- UPDATE
UPDATE tablo_ismi SET yeni_de�er WHERE kosul_adi
UPDATE personel SET maas = 5000 WHERE id = 1;
-- Concat()
-- De�erleri birle�tirmek i�in kullan�l�r.
Concat('deg1','deg2',s�tun1,s�tun2)
Select concat(ad,soyad) as ADSOYAD from TABLO
-- Substring()
-- Veriden istenen k�sm�n al�nmas�n� sa�lar.
Substring(veri,baslangic,karakter)
Select substring('metin bilgin',6,6)
Select substring(yazarad,1,3) as Ad�_Soyad� from yazar
-- LEFT(): Metnin solundan istenilen kadar karakter al�r
SELECT LEFT('Merhaba D�nya', 3) AS Sol_Karakterler;
-- RIGHT(): Metnin sa��ndan istenilen kadar karakter al�r
SELECT RIGHT('Merhaba D�nya', 5) AS Sag_Karakterler;
-- LOWER(): Metni k���k harfe �evirir
SELECT LOWER('Merhaba D�nya') AS Kucuk_Harfler;
-- UPPER(): Metni b�y�k harfe �evirir
SELECT UPPER('Merhaba D�nya') AS Buyuk_Harfler;
-- TRIM(): Ba�taki ve sondaki bo�luklar� kald�r�r
SELECT TRIM('   Merhaba D�nya   ') AS Trimli_Metin;
-- LTRIM(): Sadece ba�taki bo�luklar� kald�r�r
SELECT LTRIM('   Merhaba D�nya   ') AS Bas_Bosluk_Temizle;
-- RTRIM(): Sadece sondaki bo�luklar� kald�r�r
SELECT RTRIM('   Merhaba D�nya   ') AS Son_Bosluk_Temizle;
-- LEN() : Verinin karakter say�s�n� bulur.
SELECT LEN('Merhaba D�nya') AS Uzunluk;
-- REPLACE() : Veriyi ba�ka bir de�erle de�i�tirir
SELECT REPLACE('Merhaba D�nya', 'Merhaba', 'Selam') AS Degistirilmis_Metin;
SELECT isim, REPLACE(isim, 'Ahmet', 'Mehmet') AS Yeni_Isim FROM personel;
-- CHARINDEX() : Aranan dize bulundu�unda, o dizenin ba�lad��� pozisyonun ilk karakterinin indeksini d�ner. E�er aranan dize bulunamazsa, 0 d�ner.
CHARINDEX(search_expression, expression, [start_location])
SELECT CHARINDEX('cat', 'concatenate')
-- Reverse() : 
SELECT REVERSE('Hello')