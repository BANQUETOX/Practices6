# Haga un programa que lea una lista de números enteros e imprima cuántos son positivos, cuántos son negativos y
# cuántos son iguales a cero. El programa debe pedirle al usuario el número de números que quiere guardar y
# reservar memoria suficiente para que la lista pueda guardar todos los números.

amount_numbers = int(input("Cuantos numeros quiere analizar?"))
numbers = []
for number in range(0,amount_numbers):
    number_value = int(input(f"Cual es el valor del numero #{number + 1} "))
    numbers.append(number_value)
for number in numbers:
    if number == 0:
        print(f"{number} es igual a 0")
    elif number + number > 0:
        print(f"{number} es positivo")
    else:
        print(f"{number} es negativo")

