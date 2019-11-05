"""
5. The keys in a dictionary are guaranteed to be unique, but the values are not.
Write a function called count_values that takes a single dictionary as an argument
and returns the number of distinct values it contains. Given the input {'red':
1, 'green': 1, 'blue': 2} , for example, it should return 2 . devuelve 2 porque es el
único número que no se repite
"""
colors_to_numbers= {'rojo':1,'verde':1,'azul':2,'purpura':5,'amarillo':4}
def count_values(colors_to_numbers:dict)-> int:

    return len(set(colors_to_numbers.values()))# no repite el numero gracias a un set y te muestra la longitud

print(count_values(colors_to_numbers))