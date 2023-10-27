#sumar numeros pares en python

print("ingrese el numero inicial: ")
a = int(input())
print("ingrese el numero final: ")
b = int(input())
suma=0
print("los numeros pares del rango: ")
while a <= b:
    if a % 2 == 0:
        print(a)
        suma = suma + a
    a+=1
print("la suma de los numeros pares es: ",suma)
