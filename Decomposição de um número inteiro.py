def decompor_numero(numero):
    if numero >= 1000 or numero < 0:
        print("O número deve ser menor que 1000.")
        return

    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    resultado = []

    if centenas > 0:
        resultado.append(f"{centenas} {'centena' if centenas == 1 else 'centenas'}")
    if dezenas > 0:
        resultado.append(f"{dezenas} {'dezena' if dezenas == 1 else 'dezenas'}")
    if unidades > 0:
        resultado.append(f"{unidades} {'unidade' if unidades == 1 else 'unidades'}")

    if resultado:
        print(f"{numero} = {', '.join(resultado[:-1])} e {resultado[-1]}")
    else:
        print("0 unidades")

numero = int(input("Informe um número inteiro menor que 1000: "))
decompor_numero(numero)
