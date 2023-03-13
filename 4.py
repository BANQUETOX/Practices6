# Haga un programa que lea una lista de números reales que guarda los saldos de las cuentas de ahorro de un grupo
# de clientes de un banco y que lea otra lista que guarda los nombres de los clientes a los que corresponde cada
# cuenta, así el saldo de la cuenta[i] pertenece al cliente[i] del banco. El programa debe hacer un reporte e imprimir
# el nombre de cada cliente y el saldo de su cuenta de ahorro. Recuerde que el programa debe pedirle al usuario el
# número de clientes del banco y reservar memoria suficiente para que la lista pueda guardar todas las notas.
amount_accounts = int(input("Cuantas cuentas quiere registrar?"))
accounts = []
clients = []
for account in range(0,amount_accounts):
    account_value = int(input(f"Cual es el saldo de la cuenta #{account + 1} "))
    client_name = input(f"Cual es el nombre de la cuenta #{account + 1} ")
    accounts.append(account_value)
    clients.append(client_name)
for account in accounts:
    print(f"El saldo del cliente {clients[accounts.index(account)]} es de {accounts[accounts.index(account)]}")