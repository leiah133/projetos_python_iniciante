import os



carros =[
    ("Chervrolet tracker", 120),
    ("Chervrolet Onix", 85),
    ("Chevrolet Spin", 65),
    ("Hyundai HB20", 85),
    ("Hyundai Tucson", 85),
    ("Fiat Uno", 45),
    ("Fiat Mobi", 70 ),
    ("Fiat Pulse", 130)
    ]

alugados = []



def mostrar_lista(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} /dia.".format(i, car[0], car[1]))

mostrar_lista(carros)

while True:
    os.system("clear")
    print(" -------------------------------------------------------")
    print("Bem Vindo a Locadora de Carros")
    print(" -------------------------------------------------------")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")
    op = int(input())

    os.system("clear")

    if op == 0:
        mostrar_lista(carros)
         

    elif op == 1:
        mostrar_lista(carros)
        print("==================")
        print("Escolha o código do carro:")
        codigo = int(input())
        print("Por quantos dias você deseja alugar este carro?")
        dias = int(input())
        os.system("clear")

        print("vc escolheu {} por {} dias.".format(carros[codigo][0], dias))
        print("")
        print("o aluguel totalizaria R$ {}. Deseja alugar?".format(dias *  carros[codigo][1]))


        print(" 0 - SIM | 1 - NÃO")
        conf = int(input())
        if conf==0:
            print("Parabens voce alugou o {} por {} dias. ".format(carros[codigo][0], dias))
            alugados.append(carros.pop(codigo))



    elif op == 2:
        if len(alugados) == 0 :
            print("Não há nenhum carro para ser devolvido.")
        else:
            print("Segue a lista de carros alugados. Qual voce deseja Devolver?")
            mostrar_lista(alugados)
            print("")
            print("Escolha o código do carro que deseja devolver:")
            codigo = int(input())

            if conf == 0:
             print("Obrigado por devolver o carro {} dias.?".format(alugados[codigo][0]))
             carros.append(alugados.pop(codigo))



    print("")
    print("==================")
    print("Digite 0 para continuar | Digite 1 para SAIR")

    if float(input()) == 1:
        break