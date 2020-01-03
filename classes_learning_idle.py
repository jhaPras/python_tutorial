class Animal:
    def __init__(self,species,prop,_special):
        self.species = species
        self.prop = prop
        self._special = special

    @property
    def intro(self):
        print(f'{self.species} has property {self.prop}')

    def spe(self,_special):
        print(f'this class has this special property {self._special}')


p = Animal('Mammal','Swim','Dance')

p.intro
print(p.species)
p.spe()
