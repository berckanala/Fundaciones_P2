import math

def esfuerzo_circular_arctan_simple():
    print("Carga distribuida circular (centro, usando arctan)")
    
    q = float(input("Carga distribuida q (Pa): "))
    b = float(input("Largo carga distribuida (m): "))
    z = float(input("Profundidad z (m): "))
    
    delta_sigma_z = (q / math.pi) * (2*math.atan(b / z) + (2*(z/b))/((z/b)**2+1))
    
    print("Incremento de esfuerzo vertical Δσz =")
    print(delta_sigma_z, "Pa")

esfuerzo_circular_arctan_simple()
