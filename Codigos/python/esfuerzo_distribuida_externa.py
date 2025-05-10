import math

def esfuerzo_fuera_eje():
    print("Carga uniforme sobre círculo (fuera del eje)")
    
    q = float(input("Carga distribuida q (Pa): "))
    a = float(input("Distancia entre la carga y el punto (m): "))
    z = float(input("Profundidad z (m): "))
    b = float(input("Distancia de la carga distribuida (m): "))
    
    beta = math.atan(a / z)
    alpha = math.atan((a+b)/ z)-beta
    
    delta_sigma_z = (q / math.pi) * (alpha + math.sin(alpha) * math.cos(alpha + 2 * beta))
    
    print("Incremento de esfuerzo vertical Δσz =")
    print(delta_sigma_z, "Pa")

esfuerzo_fuera_eje()
