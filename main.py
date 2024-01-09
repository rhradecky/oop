
class Person:
    def __init__(self, name, age, gender, occupation):
        self.name =  name
        self.age = age
        self.gender = gender
        self.__occupation = occupation





    def pozdrav(self):
        print(f"Ahoj volam sa {self.name} a mam {self.age} rokov")

    def bydlisko(self):
        print(f"Ahoj volam sa {self.name} a byvam v  {self.__occupation}")


class Student(Person):
    def __init__(self, name, age, gender,occupation, score):
        super().__init__(name, age, gender, occupation)
        self.score = score

    def jeGenius(self):
        if self.score > 90:
            print(f"{self.name} je genius a {self.gender}")
        else:
            print(f"{self.name} nie je genius a {self.gender}")



patrik = Student( "Patrik", 30, "muz", "Bratislava", 95)
milan = Student( "Milan", 30, "muz", "Bratislava", 48)


print(patrik.name)
patrik.pozdrav()
patrik.jeGenius()
milan.jeGenius()



'''
class City:
    def __init__(self, city, region, country, numbOfCityzens, zip ):
        self.city =  city
        self.region = region
        self.country = country
        self.numbOfCityzens = numbOfCityzens
        self.zip = zip

    def pozdrav(self):
        print(f"Ahoj volam sa {self.name} a mam {self.age} rokov")


Bratislava = City( "Bratislava", "Zapadoslovensky", "Slovensko", 500000, 95, 84201)

print

'''
