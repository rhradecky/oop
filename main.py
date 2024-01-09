class Person:
    def __init__(self, name, age, gender, occupation):
        self.name =  name
        self.age = age
        self.gender = gender
        self.occupation = occupation


    def pozdrav(self):
        print(f"Ahoj volam sa {self.name} a mam {self.age} rokov")

    def bydlisko(self):
        print(f"Ahoj volam sa {self.name} a byvam v  {self.occupation} ")

    def zostarni(self, kolko):
        self.age += 5


richard = Person( "Richard", 30, "technik", "Ivanka")




print(richard.pozdrav())
richard.zostarni(5)
print(richard.pozdrav())
