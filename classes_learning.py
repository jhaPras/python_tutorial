class Parrot:

    species = "bird"


    def __init__(self,name,age,breed):
        self.name = name
        self.age  = age
        self.breed = breed



class Bird:
    def __init__(self):
        print('Bird is ready')

    def whoisThis(self):
        print('Bird')
    def swim(self):
        print('swim faster!')


class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print('Penguin is ready')

    def whoisThis(self):
        print('Penguin')

    def run(self):
        print('Well that\'s a good joke but i ain\'t feel like laughing')



peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
