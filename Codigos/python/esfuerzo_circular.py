import math

def esfuerzo_circular_eje():
    print("Carga circular - punto en el eje")
    
    q = float(input("Carga distribuida q (Pa): "))
    z = float(input("Profundidad z (m): "))
    r = float(input("Radio del círculo a (m): "))
    
    delta_sigma_z = q * (1 - 1/(1+(r/z)**2)**(3/2))
    
    print("Incremento de esfuerzo vertical Δσz =")
    print(delta_sigma_z, "Pa")

esfuerzo_circular_eje()
