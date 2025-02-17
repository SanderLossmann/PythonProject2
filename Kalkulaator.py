class cal():  # Loodi klass
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def liitmine(self):
        return self.a + self.b  # öeldakse pythonile kuidas liita

    def lahutamine(self):
        return self.a - self.b  # Öeldakse pythonile kuidas lahutada

    def korrutamine(self):
        return self.a * self.b  # Öeldakse pythonile kuidas korrutada

    def jagamine(self):
        return self.a / self.b  # Öeldakse pythonile kuidas jagada

    def jaak(self):
        return self.a % self.b  # Öeldakse pythonile kuidas leida jääki

    def ruutjuur(self):
        return self.a ** self.b  # Öeldakse pythonile kuidas leida ruutjuurt


a = int(input("Sisesta esimene number: "))  # Küsitakse, et sisestaksid oma esimese numbri mida tahad arvutada
b = int(input("Sisesta teine number: "))  # Küsitakse, et sisestaksid oma teise numbri mida tahad arvutada

kalk = cal(a, b)

while True:  # Alustatakse tsüklit
    def menu():
        x = (
            '1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Ruutjuure leidmine\n0  Sisesta uuesti üks liitmise operaator.  ')  # Luuakse menu kus saad valida kas tahad liita, lahutada, korrutada, jagada, jääki leida või ruutjuurt leida
        print(x)  # Prinditakse eelnevalt tehtud menu


    menu()
    valik = int(input(
        'Sisesta üks valikutest: '))  # Tehakse sulle rida kus saad teha valiku kas tahad oma numbreid liita, lahutada jne

    if valik == 1:  # Kui valik on 1
        print("Vastus: ", kalk.liitmine())  # Siis liidetakse sisestatud numbrid ja prinditakse vastus
        break  # Tsükkel lõppeb
    elif valik == 2:  # Kui valik on 2
        print("Vastus: ", kalk.lahutamine())  # Siis lahutatakse sisestatud numbrid ja prinditakse vastus
        break  # Tsükkel lõppeb
    elif valik == 3:  # Kui valik on 3
        print("Vastus: ", kalk.korrutamine())  # Siis korrutatakse sisestatud numbrid ja prinditakse vastus
        break  # Tsükkel lõppeb
    elif valik == 4:  # Kui valik on 4
        print("Vastus: ", kalk.jagamine())  # Siis jagatakse sisestatud numbrid ja prinditakse vastus
        break  # Tsükkel lõppeb
    elif valik == 5:  # Kui valik on 5
        print("Vastus: ", kalk.jaak())  # Siis leitakse jääk ja prinditakse see
        break  # Tsükkel lõppeb
    elif valik == 6:  # Kui valik on 6
        print("Vastus: ", kalk.ruutjuur())  # Siis otsitakse sinu arvude ruutjuur ja prinditakse see
        break  # Tsükkel lõppeb
    elif valik == 0:  # Kui valik on 0
        print('Sisesta uuesti üks liitmise operaator')  # Siis prinditakse "Sisesta uuesti üks liitmise operaator"
        break  # Tsükkel lõppeb





