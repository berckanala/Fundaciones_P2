from math import *

# Entradas
B = float(input("Ancho total B (m): "))
L = float(input("Largo total L (m): "))
z = float(input("Profundidad z (m): "))

# Cálculo de m y n (semidimensiones sobre z)
m = (B ) / z
n = (L ) / z

# Parte racional
numerator = 2 * m * n * sqrt(m**2 + n**2 + 1) * (m**2 + n**2 + 2)
denominator = (m**2 + n**2 + m**2 * n**2 + 1) * (m**2 + n**2 + 1)

# Parte trigonométrica
atan_arg = (2 * m * n * sqrt(m**2 + n**2 + 1)) / (m**2 + n**2 + 1 - m**2 * n**2)

# Evaluación del término arctan con ajuste de signo
if m**2 + n**2 + 1 >= m**2 * n**2:
    I = (1 / (4 * pi)) * (numerator / denominator + atan(atan_arg))
else:
    I = (1 / (4 * pi)) * (numerator / denominator + pi + atan(atan_arg))

# Cálculo del esfuerzo
print("El factor I es de: ", I)
q = float(input("Carga distribuida q (Pa): "))
delta_sigma_z = q * I
delta_sigma_z = round(delta_sigma_z, 5)

print("Incremento de esfuerzo vertical Δσz =", delta_sigma_z, "Pa")

