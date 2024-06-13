class Student:
    def __init__(self, physics, chem, maths):
        self.physics = physics
        self.chem = chem
        self.maths = maths

    @property
    def percentage(self):
        return str((self.physics + self.chem + self.maths) / 3) + " % "


s1 = Student(99, 85, 98)
print(s1.percentage)
