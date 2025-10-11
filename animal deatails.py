class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        return "generic animal sound"

class Dog(Animal): #Dog inherits from Animal
    def __init__(self,name,breed):
        super().__init__(name)#call the parent class's constructor

        self.breed=breed

    def speak(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball."

#Create an instance of the child class (Dog)
my_dog=Dog("Buddy","Golden Retriever")

#access attributes and methods from both parent and child classes
print(f"name: {my_dog.name}")
print(f"Breed: {my_dog.breed}")
print(my_dog.speak())
print(my_dog.fetch())
