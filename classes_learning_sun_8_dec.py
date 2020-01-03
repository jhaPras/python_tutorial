class Person:
    
    def __init__(self,name,surname,height):
        self.name = name
        self.surname = surname
        self.height = height
    



    ## '@property':decorator which turns a method to an attribute
        
    @property
    def fullname(self):
        return f"{self.name, self.surname}"

    ''' decorators which modifie's the previous attribute and extends it's functionality
        and to that these decorators have the same name as attribute '''

    @fullname.setter
    def fullname(self,value):
        name,surname = value.split(" ", 1)
        self.name = name
        self.surname = surname

    @fullname.deleter
    def fullname(self):
        del self.name
        del self.surname


    def get_height(self):
        return self.height

    def set_height(self,height):
        self.height = height


jane =Person('Jane','smith','131')
print(jane.fullname)

jane.fullname = 'Jahn Doe'
print(jane.fullname)
print(jane.name)
print(jane.surname)


        
