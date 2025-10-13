#Example 2: school Management
#Parent
class Person:

    def __init__(self,name,age):
        self.Name = name
        self.age = age


class Student(Person):

    def __init__(self,name,age,rollno=278):
        super().__init__(name,age)
        self.roll_no=rollno



    def introduce(self):
        print(f"My name is {self.Name},age{self.age},roll number{self.roll_no}.")


obj=Student("Xeeshan",21)
obj.introduce()
