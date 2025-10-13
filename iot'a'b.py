#Single Inheritance
class A:

    def displayA(self):
        print("Inheritance A Class")

class B(A):

    def displayB(self):
        print("Inheritance B Class")

obj = B()
obj.displayA()
obj.displayB()

print()
# Multi Label Inheritence
class A:

    def displayA(self):
        print("Inheritance A Class")


class B(A):

    def displayB(self):
        print("Inheritance B Class")

class C(B):

    def displayC(self):
        print("Inheritance C class")

obj = C()
obj.displayA()
obj.displayB()
obj.displayC()




