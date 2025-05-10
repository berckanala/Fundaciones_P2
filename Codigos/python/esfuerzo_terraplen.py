import math

def esfuerzo_terraplen_b1b2():
    print("Terraplén con bordes B1 y B2")

    q = float(input("Carga distribuida q (Pa): "))
    B1 = float(input("Distancia al borde izquierdo B1 (m): "))
    B2 = float(input("Distancia al borde derecho B2 (m): "))
    z = float(input("Profundidad z (m): "))

    alpha1= math.atan((B1+B2)/z)-math.atan(B1/z)
    alpha2 = math.atan(B1 / z)

    delta_sigma_z = (q / math.pi) * ((B1+B2)/B2*(alpha1+alpha2)-(B1/B2*alpha2))

    print("Incremento de esfuerzo vertical Δσz =")
    print(delta_sigma_z, "Pa")

esfuerzo_terraplen_b1b2()
