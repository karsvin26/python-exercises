print('##  Program Python Diskon Potongan Harga ##')
print('============================================')
print()
 
total_belanja = int(input('Total Belanja: Rp.'))
 
if (total_belanja >= 100000) and (total_belanja < 200000):
  harga_akhir = total_belanja - (0.23*total_belanja)
  print('Selamat, anda mendapat diskon 23%')
elif (total_belanja >= 200000) and (total_belanja < 3000000):
  harga_akhir = total_belanja - (0.25*total_belanja)
  print('Selamat, anda mendapat diskon 25%')
elif (total_belanja >= 3000000):
  harga_akhir = total_belanja - (0.28*total_belanja)
  print('Selamat, anda mendapat diskon 28%')
else:
  harga_akhir = total_belanja
   
print('Total bayar: Rp.',round(harga_akhir))
