class Country:

    def __init__(self,name,population,area):
        self.name=name
        self.population=population
        self.area=area



    def is_langer(self,other)-> bool:
        (Country,Country)

        return self.area>other.area


    def population_density(self) -> float:
        return self.population/self.area

    def __str__(self)-> str:
        return '{} has a population of {} and is {} square km'.format(self.name,self.population,self.population_density())

    def __repr__(self) -> str:
        return "Country({0},{1},{2})".format(self.name,self.population,self.area)

if __name__=="__main__":

    canada=Country("Canada", 34482779, 9984670)
    print("Name: ", canada.name)
    print("Population: ", canada.population)
    print("Area:", canada.area)
    print()

    usa=Country("United States of America", 313914040, 9826675)
    print("Name: ", usa.name)
    print("Population: ", usa.population)
    print("Area:", usa.area)
    print()

    print("Longitud: ", canada.is_langer(usa))
    print("Longitud: ", usa.is_langer(canada))
    print()

    print("Population_Density: ", canada.population_density())
    print("Population_Density: ", usa.population_density())
    print()

    print("String:", canada.__str__())
    print("String:", usa.__str__())
    print()

    print("String _repr_", canada.__repr__())
    print("String _repr_", usa.__repr__())
