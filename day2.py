faiz= 1.59
vade= 36
krediAdi= "İhtiyaç Kredisi"

print(vade+12)

print(type(faiz))
print(type(vade))
print(type(krediAdi))

faiz= 1.59
vade= "36"
krediAdi= "İhtiyaç Kredisi"

print(int(vade)+12)
#print(int(krediAdi))
print(str(faiz))

faiz=str(faiz)
print(type(faiz))

vade=input("Lütfen istediğiniz vade sayısını giriniz:")
print(vade)
print(type(vade))
print(int(vade)+12)

vade=int(input("Lütfen istediğiniz vade sayısını giriniz:"))
print(vade)
print(type(vade))
print(vade+12)


# string interpolation
# Seçtiğiniz vade sonucu ortaya çıkan vade:
vade=input("Lütfen istediğiniz vade sayısını giriniz:")
print("Seçtiğiniz vade sonucu ortaya çıkan vade:" + vade)
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade) )

isim= "Halit"
metin= "Merhaba {name}".format(name=isim)
print(metin)

#f-string
metin= f"Hoşgeldiniz {1+1}"
print(metin)


#listeler
#döngüler
#fonksiyonlar

dizi= ["İhtiyaç Kredisi", 10, 5.2, True]
print(dizi)

krediler= ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler)
print(krediler[0])

print(len(krediler)) #length
#print(krediler[3]) => hata verir

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop()
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)

krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y Kredisi","Z Kredisi"])
print(krediler)

#for
#i=0 i<0

for i in range(10):
    print("xx")
    print(i)
print("*************")
for i in range(5,11):
    print(i)
print("*************")
for i in range(0,51,10):
    print(i)


krediler= ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
   print(kredi)
print("*************")
for i in range(3):
    print(krediler[i])
print("*************")


#sonsuz döngü
i = 0
while i < 10:
    print("x")
    i += 1
print("y")

print("*************")

while True:
    print("X")
    break

print("*************")

i=0
while i < len(krediler):
    print(krediler[i])
    i+=1

print("*************")

i=0
while i < len(krediler):
    if krediler[i] == "Konut Kredisi" :
        break
    print(krediler[i])
    i+=1

print("*** Son Döngü ***")


krediler= ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
i = 0
while i < len(krediler):
    i+=1
    print(i)
    print(krediler[i])
    if krediler[i] == "Konut Kredisi" :
        break


#fonksiyonlar


fiyat = 100 
indirim =20
#definition define
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
