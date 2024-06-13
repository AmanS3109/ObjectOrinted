# creating class
class Student:

    # default constructor
    def __int__(self):
        pass

    college_name = "Mumbai University"

    # parametric constructor
    def __init__(self, name, grade):  # to avoid redundancy we use constructor
        print(self)  # <__main__.Student object at 0x000001F5CFCA9690>
        self.name = name
        self.grade = grade

    # methods
    def get_marks(self):
        return self.grade


s1 = Student("Shruti Shukla \n", 10)
s2 = Student("Aman Singh", 8)
print(s1.college_name, s1.name,
      s2.college_name, s2.name)  # calling attributes

print(s1.get_marks(), s2.get_marks())  # calling methods
