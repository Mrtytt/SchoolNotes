--declare @sayi1 int = 10
--declare @sayi2 int = 20

--declare @sayi3 int = @sayi1 + @sayi2
--select @sayi3

--declare @selam varchar(20) = 'Merhaba Dünya'
--print @selam

--Declare @personelim Table (no int identity(1,1), adsoyad varchar(20) not null)
--insert into @personelim values ('metin')
--insert into @personelim values ('besim')
--select * from @personelim

--IF Exists (Select * from kitap where puan>20)
--	Print('Puaný 20 den fazla kitap vardýr')
--Else 
--	Select kitapadi,puan from kitap where puan<=20

--Declare @say varchar(15)
--Select @say= COUNT(*) from kitap
--if (@say<50)
--	Begin
--		Print 'kitap Sayýsý' +@say + 'yetersiz miktar'
--	End
--Else Print 'kitap yeterli'

--Select kitapadi,turno=case turno	
--						when '1' then 'Dram'
--						when '2' then 'Komedi'
--						else 'Belirsiz'
--						End
--from kitap

--Declare @sayac int = 6,@fakt int = 1
--while @sayac<>0
--begin 
--set @fakt = @fakt * @sayac
--set @sayac = @sayac-1
--end 
--print @fakt

--Declare @sayac INT = 1
--While @sayac <= 10
--Begin
--	Print @sayac
--	Set @sayac = @sayac + 1
--END

