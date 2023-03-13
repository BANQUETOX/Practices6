# Haga un programa que lea una lista de números reales que guarda los saldos de las cuentas de ahorro de un grupo
# de clientes de un banco y que lea otra lista que guarda los nombres de los clientes a los que corresponde cada
# cuenta, así el saldo de la cuenta[i] pertenece al cliente[i] del banco. El programa debe hacer un reporte e imprimir
# el nombre de cada cliente y el saldo de su cuenta de ahorro. Recuerde que el programa debe pedirle al usuario el
# número de clientes del banco y reservar memoria suficiente para que la lista pueda guardar todas las notas.
#Modifique el programa anterior para que además imprima el saldo promedio de las cuentas de ahorro del banco.

amount_accounts = int(input("Cuantas cuentas quiere registrar?"))
accounts = []
clients = []
accounts_average = 0
for account in range(0,amount_accounts):
    client_name = input(f"Cual es el nombre de la cuenta #{account + 1} ")
    account_value = int(input(f"Cual es el saldo de la cuenta #{account + 1} "))
    accounts_average += account_value
    accounts.append(account_value)
    clients.append(client_name)
for account in accounts:
    print(f"El saldo del cliente {clients[accounts.index(account)]} es de {accounts[accounts.index(account)]}")
print(f"El saldo promedio en las cuentas de ahorro es de {accounts_average / amount_accounts}")