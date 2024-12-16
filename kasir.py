print("----------------- Program Kasir Sederhana -----------------")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def fungsimakanan():
   global totalmakan
   global porsi
   global makan
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Nasi Goreng - Rp 15000")
   print("2. Soto - Rp 15000")
   print("3. Mie Ayam - Rp 10000")
   print("4. Bakso - Rp 13000")
   print("5. Indomie - Rp 10000")
   print("6. Roti Bakar - Rp 18000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalmakan=porsi*15000
       print (porsi," porsi Nasi Goreng Telur = Rp", totalmakan)
       makan=("Nasi Goreng")
   elif nomor==2:
       totalmakan=porsi*15000
       print (porsi," porsi Soto = Rp", totalmakan)
       makan=("Soto")
   elif nomor==3:
       totalmakan=porsi*10000
       print (porsi, " porsi Mie Ayam = Rp", totalmakan)
       makan=("Mie Ayam")
   elif nomor==4:
       totalmakan=porsi*13000
       print (porsi, " porsi Bakso = Rp", totalmakan)
       makan=("Bakso")
   elif nomor==5:
       totalmakan=porsi*10000
       print (porsi, " porsi Indomie = Rp", totalmakan)
       makan=("Indomie")
   elif nomor==6:
       totalmakan=porsi*18000
       print (porsi, " porsi Roti Bakar = Rp", totalmakan)
       makan=("Roti Bakar")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()
   lanjut = input('Apakah anda ingin memesan Lagi [Y/N] ? ')
   if lanjut == 'Y':
      fungsimakanan()

def fungsiminuman():
   global totalminum
   global minum
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es teh - Rp 5000")
   print("2. Es jeruk - Rp 6000")
   print("3. Es kopi - Rp 5000")
   print("4. Jus Alpukat - Rp 8000")
   print("5. Cappucino Cincau - Rp 5000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalminum=gelas*5000
       print (gelas," Es Teh = Rp", totalminum)
       minum=(" Gelas Es Teh")
   elif nomor==2:
       totalminum=gelas*6000
       print (gelas, " Gelas Es Jeruk = Rp", totalminum)
       minum=("Es Jeruk")
   elif nomor==3:
       totalminum=gelas*5000
       print (gelas, " Gelas Es Kopi = Rp", totalminum)
       minum=("Es Kopi")
   elif nomor==4:
       totalminum=gelas*8000
       print (gelas, " Gelas Jus Alpukat = Rp", totalminum)
       minum=("Jus Alpukat")
   elif nomor==5:
       totalminum=gelas*6000
       print (gelas, " Gelas Cappucino Cincau = Rp", totalminum)
       minum=("Cappucino Cincau")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()
   lanjut = input('Apakah anda ingin memesan Lagi [Y/N] ? ')
   if lanjut == 'Y':
      fungsiminuman()


fungsimakanan()
fungsiminuman()
totalsemua=totalmakan+totalminum

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== S T R U K   B E L I =========")
print("==================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",porsi,makan,"( Rp", totalmakan,")")
print ("\t\t ",gelas,minum,"( Rp", totalminum,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("===== T E R I M A K A S I H =====")
print("==================================")