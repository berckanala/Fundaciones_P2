import math

def circulo_mohr_2d():
    print("Círculo de Mohr (2D)")
    
    # Entradas del usuario
    sigma_x = float(input("σx: "))
    sigma_y = float(input("σy: "))
    tau_xy = float(input("τxy: "))
    
    # Cálculos del centro y radio
    centro = (sigma_x + sigma_y) / 2
    radio = math.sqrt(((sigma_x - sigma_y)/2)**2 + tau_xy**2)
    
    # Esfuerzos principales
    sigma1 = centro + radio
    sigma2 = centro - radio
    
    # Esfuerzo cortante máximo
    tau_max = radio

    # Resultados
    print("Centro del círculo:", centro)
    print("Radio del círculo: ", radio)
    print("σ1 (mayor): ", sigma1)
    print("σ2 (menor): ", sigma2)
    print("τmax: ", tau_max)

circulo_mohr_2d()
