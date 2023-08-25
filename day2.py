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