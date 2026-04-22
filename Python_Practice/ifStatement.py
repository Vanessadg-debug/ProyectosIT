
"""The variables a and b have missing values. Fill them so that the code inside the if statement will be executed! 
(make sure the if condition is true)
At the end of the program, the value of c should be 3."""

a=15
b=0

c=0
if a < b or b >= 10:
    c = 2

c += 1

print(f"c={c}")

"""De acuerdo al ejercicio el valor de c empieza en 0 y cada que salga del cliclo quiere que se muestre C con el valor de 3,
para ello es obligatorio que entre en ciclo y se cumplan una de esas dos condiciones  para que C tome el valor de 2 
y saliendo del ciclo se sume 1 y asi C=2+1=3
una de las dos se debe cumplir
"""

