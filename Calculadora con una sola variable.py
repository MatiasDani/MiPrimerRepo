print("Calculadora con una sola variable \n")

print("********************")
print("* Menu de opciones *")
print("******************** \n")

print("""1. Suma
2. Resta
3. Multiplicacion
4. Divicion
5. Divicion entera
6. Exponente
7. Modulo o resto""", "\n")

numero = int(input("Introduce la opcion deseada:"))

if numero == 1:
    print("Elegiste Suma\n")
    numero = int(input("Introduce el primer valor:"))
    numero += int(input("Introduce el segundo valor:"))
    print("El resultado de la suma es: ",numero)
    

elif numero == 2:
    print("Elegiste Resta\n")
    numero = int(input("Introduce el primer valor:"))
    numero -= int(input("Introduce el segundo valor:"))
    print("El resultado de la Resta es: ",numero)

elif numero == 3:
    print("Elegiste Multiplicacion\n")
    numero = int(input("Introduce el primer valor:"))
    numero *= int(input("Introduce el segundo valor:"))
    print("El resultado de la Multiplicacion es: ",numero)


elif numero == 4:
    print("Elegiste Divicion\n")
    numero = float(input("Introduce el primer valor:"))
    numero /= float(input("Introduce el segundo valor:"))
    print("El resultado de la Divicion es: ", round(numero, 2))

elif numero == 5:
    print("Elegiste Divicion entera\n")
    numero = int(input("Introduce el primer valor:"))
    numero //= int(input("Introduce el segundo valor:"))
    print("El resultado de la divicion entera es: ",numero)


elif numero == 6:
    print("Elegiste Exponente\n")
    numero = int(input("Introduce el primer valor:"))
    numero **= int(input("Introduce el segundo valor:"))
    print("El resultado del exponente es: ",numero)

elif numero == 7:
    print("Elegiste Modulo o resto\n")
    numero = int(input("Introduce el primer valor:"))
    numero %= int(input("Introduce el segundo valor:"))
    print("El resultado del modulo o resto es: ",numero)
    
else:
    print("El numero que elegiste no existe.")




























    
    
    
    




