--create proc Stokum2(@gir_deger int=null)
--as
--	Select * from kitap where turno=@gir_deger
--go

-- exec Stokum2 4

-----------------------------------------------------------
-- FUNCTION
--Create Function fonksiyon--fonksiyon.adi 
--(
--	--parametrelerin eklendi�i alan
--	@param1 int,@param2 int
--)
--Returns int -- geri d�necek olan verinin t�r� 
--AS
--Begin
--	-- �nce geri d�necek de�er tan�mlan�r
--	Declare @donen int 
--	-- SQL ifadeleri d�nen parametreye de�er aktar�m� gibi i�lemler
--	Return @donen
--END


--Create Function BuyukHarf(@gelen varchar(20)) Returns varchar(20)
--AS
--Begin
--Return Upper(@gelen)
--END
--select dbo.BuyukHarf('Metin')


--Create Function FarkAl(@sayi1 int,@sayi2 int) Returns int
--AS
--Begin
--	Declare @sonuc int = @sayi1 - @sayi2
--	Return @sonuc
--END
--select dbo.FarkAl(15,5)

--------------------------------------------------
-- TRIGGER
--create trigger silme
--on database
--for drop_tabl,alter_table
--as
--print 'de�i�iklik yap�lamaz'
--rollback


-- create trigger silinemez on urunler