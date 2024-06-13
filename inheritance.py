class A:
    varA = "Welcome to class A"


class B:
    varB = "Welcome to class B"


class C(A, B):  # inherit the property of class A and B
    varC = "Welcome yo class C"


c1 = C()
print(c1.varB)
print(c1.varA)
print(c1.varC)
