# Haga un programa que lea una lista de números reales que guarda las ventas de todos los meses de un año de
# trabajo, e imprima: las ventas de cada mes, el promedio de ventas del año y cuántos meses se vendió más que el
# promedio.

anual_sales = [10,30,45,46,53,62,73,38,39,410,17,110]
anual_average = 0
best_month = 0
for month_sales in anual_sales:
    print(f"Las ventas del mes {anual_sales.index(month_sales) + 1} son {month_sales}")
    anual_average += month_sales
    if month_sales > best_month:
        best_month = anual_sales.index(month_sales) + 1
anual_average = anual_average / len(anual_sales)
print(f"El promedio de ventas anual fue de {anual_average}")
print(f"El mes con mayor ventas fue el mes {best_month}")
