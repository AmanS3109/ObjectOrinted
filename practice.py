class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        add = 0
        for val in self.marks:
            add += val
        print("Hi your name is ", self.name, "your marks is: ", add/3)


s1 = Student("Aman", [95, 96, 90])
s2 = Student("Shruti", [95, 96, 97])
s1.name = "Tony Stark"
s1.marks = [99, 99, 100]
s1.average()
s2.average()