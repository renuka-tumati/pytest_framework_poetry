# Python program showing a
# use of property() function

class Geeks:

    def __init__(self):
        self._age = 0
        self._name = ""
        self._city = ""

    # function to get value of _age
    def get_age(self):
        print("getter method called")
        return self._age

    # function to set value of _age
    def set_age(self, a):
        print("setter method called")
        self._age = a

    # function to delete _age attribute
    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age)

    @property
    def name(self):
        print("name getter")
        return self._name

    @name.setter
    def name(self, name):
        print("name setter")
        self._name = name


mark = Geeks()

mark.age = 10
mark.name = "mark"

print(mark.age, mark.name)