class Student():
    def __init__(self, name):
        self.name = name


s1 = Student("Shruti")
print(s1.name)  # print Shruti
del s1.name  # because of del keyword used to delete name attribute
print(s1.name)  # AttributeError: 'Student' object has no attribute 'name'

