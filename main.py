class Person:
    def __init__(self, name, age, gender, occupation, color):
        self.__name =  name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.color = color

    def pozdrav(self):
        print(f"Ahoj volam sa {self.__name} a mam {self.age} rokov")

    def bydlisko(self):
        print(f"Ahoj volam sa {self.__name} a byvam v  {self.occupation}")

    def zostarni(self, kolko):
        self.age += 5


richard = Person( "Richard", 30, "muz", "Ivanka", "modra")


print(richard.pozdrav())

richard.__name = "Fero"

print(richard.pozdrav())
#richard.zostarni(5)
#print(richard.color)

print(richard.bydlisko())
