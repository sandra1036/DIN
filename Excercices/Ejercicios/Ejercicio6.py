"""
After doing a series of experiments, you have compiled a dictionary showing
the probability of detecting certain kinds of subatomic particles. The particles’
names are the dictionary’s keys, and the probabilities are the values: {'neutron':
0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14} . Write a function that takes
a single dictionary of this kind as input and returns the particle that is least
likely to be observed. Given the dictionary shown earlier, for example, the
function would return 'meson' .
"""
#Devuelve el menor de los numeros y te sale el item
particle_to_probability={'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07,'neutrino': 0.14}

def least_likely(particle_to_probability):

 smallest = 1
 name = ''
 for particle in particle_to_probability:
     probability = particle_to_probability[particle]
     if probability < smallest:
        smallest = probability
        name = particle

 return name

if __name__=="__main__":
    print(least_likely(particle_to_probability))