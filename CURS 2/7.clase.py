
class Student:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def __str__(self):
        return f"Studentul {self.nume} are {self.varsta} de ani."

    def invata(self):
        print("Studentul invata.")


std = Student("Teodor", 20)
print(std)
string_generat = str(std)
print(type(string_generat))

print(std.__dict__)

print(dir(std))