import math

def esfuerzo_puntual():
    print("Boussinesq - Carga puntual vertical")
    
    Q = float(input("Carga puntual Q (N): "))
    z = float(input("Profundidad z (m): "))
    r = float(input("Distancia radial r (m): "))
    
    R_cuad =(r/z)**2
    delta_sigma_z = (3*Q)/(2*math.pi*z**2)*((1)/(1+R_cuad))**(5/2)
    
    print("Incremento de esfuerzo vertical Δσz =")
    print(delta_sigma_z, "Pa")

esfuerzo_puntual()
