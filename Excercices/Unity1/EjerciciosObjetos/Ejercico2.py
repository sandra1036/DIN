from Ejercicio1 import Country
class Continent:


    def __init__(self,name:str,countries:list):
        self.name=name
        self.countries=countries

    def total_population(self,countries:list)->int:
        total=0
        for country in self.countries:
            total=total+country.population

        return total


    def __str__(self):
        return '{} \n {} has a population of {} and is {} square km'.format(north_america,self.name,self.countries)


if __name__=="__main__":
    print()
    canada = Country('Canada', 34482779, 9984670)
    usa = Country('United States of America', 313914040, 9826675)
    m = Country('Puerto Rico', 895895421, 1518596526)
    countries = [canada, usa, m]
    north_america=Continent("North America",countries)

    for county in north_america.countries:
        print(county)

    print()
    print("Total: ",north_america.total_population(countries))



