##  A Introduction in Classes (Python 3.7!)


'''
--> Class in general are just blueprints of some functions bound together to achieve one bigger goal 
--> Classes starts with single definition statement and is required to have one positional argument(self) for the functions 
    defined inside the class while calling.
--> self is automatically assigned to the object created or when the object is instaniated from the class
'''

class Person:

    __species = 'Human'

    def __init__(self,name,age,gender):

        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        print(f'Hello {self.name} ! it\'s a pleasure seeing you here.')

a = Person('bryden',28,'Male')
print(a.age)
print(a.name)
a.greet()

print (dir(Person))

print(Person.__doc__)


