class Person:
    name = "anonymous"

    @classmethod  # decorator
    def changeName(cls, name):
        cls.name = name


p1 = Person()
p1.changeName("Shruti")
print(p1.name)
print(Person.name)
