import os

print("=======")

operations = {
    "+": "Soma",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão",
    "^": "Potência",  # Exponenciação
}

while True:
    os.system('clear')
    i = 0
    for op_index, name in operations.items():
        print(i, ":", name)
        i += 1

    print("")
    print("Escolha a operação que deseja realizar:")
    op_index = int(input())

    op_string = list(operations.keys())[op_index]

    print("")
    print('{} escolhida.'.format(op_string))
    print("")
    print("Qual o primeiro valor?")
    v1 = float(input())
    print("Qual o segundo valor?")
    v2 = float(input())

    if op_string == '+':
        result = v1 + v2
    elif op_string == '-':
        result = v1 - v2
    elif op_string == '*':
        result = v1 * v2
    elif op_string == '/':
        result = v1 / v2
    elif op_string == '^':
        result = v1 ** v2

    print("")
    print(" {} {} {} = {}".format(v1, op_string, v2, result))
    print("")
    print("=======")

    print("Deseja continuar?sim/nao)")
    resp = str(input()).upper()
    if resp == 'nao':
        break
