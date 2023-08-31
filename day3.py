#sınıflar => classlar
#modules
#paket yönetimi

class Human:
    def talk(self):
        print("Human is talking..")
    def walk(self):
        print("Human is walking..")

#instance => örnek
human1= Human()
human1.talk()
human1.walk()

print("**************")

class Human:
    def talk(self,sentence):
        print(f"Human: {sentence}")
    def walk(self):
        print("Human is walking..")

#instance => örnek
human1= Human()
human1.talk("Merhaba")
human1.walk()

print("**************")

class Human:
    name = "Halit"
    def talk(self,sentence):
        name= "Ercan"
        print(f"{name}: {sentence}")
    def walk(self):
        print("Human is walking..")

#instance => örnek
human1= Human()
human1.talk("Merhaba")
human1.walk()

print("**************")

class Human:
    name = "Halit"
    def talk(self,sentence):
        name= "Ercan"
        print(f"{self.name}: {sentence}")
    def walk(self):
        print("Human is walking..")

#instance => örnek
human1= Human()
human1.talk("Merhaba")
human1.walk()

print("**************")

class Human:
    name = "Halit"
    def talk(self,sentence):
        name= "Ercan"
        print(f"{self.name}: {sentence}")
    def walk(self):
        print("Human is walking..")

#instance => örnek
human1= Human()
human1.name ="Enes"
human1.talk("Merhaba")
human1.walk()

human2= Human()
human2.name = "Cem"
human2.talk("Selam")
human2.walk()

print("**************")

class Human:
    name = "Halit"
    #built-in
    #constructor
    #initialize
    def __init__(self) :
        print("Bir human instance'i üretildi")
    def talk(self,sentence):
        name= "Ercan"
        print(f"{self.name}: {sentence}")
    def walk(self):
        print("Human is walking..")

#instance => örnek
human1= Human()
human1.name ="Enes"
human1.talk("Merhaba")
human1.walk()
print(human1)

human2= Human()
human2.talk("Selam")
human2.walk()
print(human2)

print("**************")

class Human:
    name = "Halit"
    #built-in
    #constructor
    #initialize
    def __init__(self,name) :
        self.name = name
        print("Bir human instance'i üretildi")
    def __str__(self) :
        return f"STR Fonksiyonundan dönen değer: {self.name}"
    def talk(self,sentence):
        name= "Ercan"
        print(f"{self.name}: {sentence}")
    def walk(self):
        print("Human is walking..")

#instance => örnek
human1= Human("Enes")
human1.talk("Merhaba")
human1.walk()
print(human1)

human2= Human("Halit")
human2.talk("Selam")
human2.walk()
print(human2)