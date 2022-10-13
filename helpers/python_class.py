class Dog:
    breed = "Pug"

    """Class methods must have an extra first parameter in the method definition.
     We do not give a value for this parameter when we call the method, Python provides it"""
    def __init__(self, age, name):
        self._age = age
        self._name = name

    """Class methods must have an extra first parameter in the method definition.
    We do not give a value for this parameter when we call the method, Python provides it"""
    @property
    def name(self):
        print("name:getter")
        return self._name

    @name.setter
    def name(self, value):
        print("name:setter")
        self._name = value

    @name.deleter
    def name(self):
        print("name:deleter")
        del self._name


pug1 = Dog(12,"Tommy")
print(pug1.name)
print(pug1.breed)
pug1.age = 13

del pug1.name
print(pug1.breed, pug1.age)
""" print(pug1.name) """
