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
human2.talk("Merhaba")
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

human2= Human()
human2.name = "Cem"
human2.talk("Merhaba")
human2.walk()
