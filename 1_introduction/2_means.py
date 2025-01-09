import numpy as np

#Geometric mean 


def geometric_mean(n):
    h=1
    for i in range(1,n+1):
        h*=i

    return h**(1/n)

#Arithmetic mean

def arithmetic_mean(n):
    h=0
    for j in range(1,n+1):
        h+=j
    return h/n

# Harmonic mean

def harmonic_mean(n):
    h=0
    for j in range(1,n+1):
        h+=1/j
    return n/h


a = np.random.randint(100)

dict1={"Geometric mean":geometric_mean(a),"Arimethic mean":arithmetic_mean(a),"Harmonic mean":harmonic_mean(a)}

# Encontrar la clave con el valor máximo y mínimo
key_max = max(dict1, key=dict1.get)  # Clave con el valor máximo
key_min = min(dict1, key=dict1.get)  # Clave con el valor mínimo

# Imprimir resultados
print(f'Valor aleatorio generado= {a}')
print("Diccionario:", dict1)
print(f"La clave con el valor máximo es: '{key_max}' -> {dict1[key_max]}")
print(f"La clave con el valor mínimo es: '{key_min}' -> {dict1[key_min]}")