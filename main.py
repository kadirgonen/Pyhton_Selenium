print("Kodlamaio")
baslik = "Taşıt Kredisi"
print(baslik)
# string => metinsel ifade
baslik1 = "İhtiyaç Kredisi"
print(baslik1)
# int, integer => tam sayı
vade = 36
ekVade= 6
vade2 = "36"

# float, decimal, double
aylikOdeme = 200.50

# boo, boolean => True veya False
yukselisteMi = False

# matematiksel operatörler

#+
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

#-
print(5 - 5)
print(vade - 12)
print(vade - ekVade)
print(36 - 6)

#*
print(5 * 5)
print(vade * 12)
print(vade * ekVade)
print(10 * 10)

#/
print(5 / 5)
print(vade / 12)
print(vade / ekVade)
print(10 / 2)

yeniVade= vade / 2
fiyat= 100
indirimliFiyat= fiyat - 20 

print(yeniVade)
print(indirimliFiyat)

# % => mod operatör
print(10%2)
print(vade %5)
print(vade %ekVade)
print(30%10)

# mantıksal operatör

print(1==1)
print(1==2)

print(1>2)
print(3>1)
print(1>1)
print(1>=1)

print(1<2)
print(3<1)
print(1<1)
print(1<=1)

print(1!=1)
print(1!=2)

# or and

print(1>2 or 5>2)
print(1>2 and 5>2)
print(1>2 or 5>2 and 3>2)

print(1>2 and 5>2 and 3>2)

print(1>2 or 2>1 and 3>2)


# karar yapıları
# if else
sayi1=10
sayi2=15
#sayi1 sayi2'den büyükse ekrana sayi1 daha büyüktür yazdır
#condition

#indent
if(sayi1>sayi2):
  print("Sayi 1 Sayi 2'den büyüktür")
  print("Hala if bloğunun içerisindeyim")
print("Burası if bloğunun dışıdır.")

if(sayi1<sayi2):
  print("Sayi 1 Sayi 2'den küçüktür")
  print("Hala if bloğunun içerisindeyim")
#eğer if bloğuna girmez ise
else:
  print("Sayi 1 Sayi 2'den büyüktür")

print("Burası if bloğunun dışıdır.")

sayi1=15
sayi2=15

#indent

if(sayi1<sayi2):
  print("Sayi 1 Sayi 2'den küçüktür")
  print("Hala if bloğunun içerisindeyim")
#eğer if bloğuna girmez ise
elif sayi1==sayi2:
  print("İki sayı eşittir")
#eğer if ve else if bloklarının hiçbirine girmez ise
else:
  print("Sayi 1 Sayi 2'den büyüktür")

print("Burası if bloğunun dışıdır.")