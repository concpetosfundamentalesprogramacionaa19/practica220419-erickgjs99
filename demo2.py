"""
        Ejercicio de Suma,Multiplicacion,Division 
"""
import sys
n1 = sys.argv[1]
n2 = sys.argv[2]


n3 = int(n1) + int(n2)
n4 = int(n1) * int(n2)
n5 = int(n1) / int(n2)
n6 = int(n1) - int(n2)

print("El resultado de la suma entre "+ str(n1)+" y "+ str(n2) +" es igual a: " +str(n3))
print("El resultado de la multiplicacion entre "+ str(n1)+" y "+ str(n2) +" es igual a: " +str(n4))
print("El resultado de la division entre "+ str(n1)+" y "+ str(n2) +" es igual a: " +str(n5))
print("El resultado de la resta entre "+ str(n1)+" y "+ str(n2) +" es igual a: " +str(n6))