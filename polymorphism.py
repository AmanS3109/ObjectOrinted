class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def showNumber(self):
        print(self.real, "+", self.imaginary, "i")

    def __add__(self, num2):  # dunder function
        newReal = self.real + num2.real
        newImaginary = self.imaginary + num2.imaginary
        return Complex(newReal, newImaginary)

    def __sub__(self, num2):  # dunder function
        newReal = self.real - num2.real
        newImaginary = self.imaginary - num2.imaginary
        return Complex(newReal, newImaginary)


c1 = Complex(1, 2)
c1.showNumber()
c2 = Complex(2, 4)
c2.showNumber()
c3 = c1 + c2
c3.showNumber()
c3 = c1 - c2
c3.showNumber()
c3 = c2 - c1
c3.showNumber()
