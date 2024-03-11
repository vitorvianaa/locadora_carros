import os
os.system("cls")
#carros disponiveis para alugar
portifolio = {
    #Nome do carro --> valor da diaria
    "Chevrolet Tracker" : 120,
    "Chevrolet Spin" : 90,
    "Hyundai HB20" : 85,
    "Hyundai Tucson" : 120,
    "Fiat Uno" : 60,
    "Fiat Mobi" : 70,
    "Volkswagen Gol" : 80,
    "Volkswagen Amarok": 150
}
#carros alugados disponiveis para devolucao
alugados = {

}

def verCarros(): ## Chama todos os carros que tenhos disponivel para locação
    iprincipal = 0
    while iprincipal == 0:
        print("Carros disponiveis para alugar:")
        print("===========")
        i = 0
        for carro, diaria in portifolio.items():
            print(f"\nCodigo do carro [{i}] - {carro} - Diaria: R${diaria} / dia")
            i += 1
        print("\n===========")
        print("Digite 1 para sair")
        input()
        iprincipal = 1
    return 0

def alugarCarro(): ##Lista os carros disponiveis
    iprincipal = 0
    while iprincipal == 0:
        print("Carros disponiveis para alugar:")
        print("===========")
        i = 0
        for nome, diaria in portifolio.items(): ## percorro o dic de carros disponiveis e imprimo em ordem
            print(f"\nCodigo do carro [{i}] - {nome} - Diaria: R${diaria} / dia")
            i += 1 ## uso para saber o indice do carro escolhido
        print("\n===========")
        print("Digite o codigo do caro que deseja alugar para sair")
        carroAlugado = int(input()) # pego o indice do carro escolhido e guardo em uma variavel
        listaCarros = list(portifolio.keys()) ## pego todas as chaves do meu dic e jogo em uma lista
        listaDiaria = list(portifolio.values()) ## pego todas os values do meu dic e tambem jogo em uma lista
        os.system("cls")
        
        print(f"Você escolheu o carro : {listaCarros[carroAlugado]}. Deseja alugar por quantos dias?")
        diasAlugados = int(input()) # pego os dias alugados
        print(f"Revise seu pedido:\nCarro escolhido: {listaCarros[carroAlugado]}") #conferindo a escolha do usuario
        print(f"Total de diarias: {diasAlugados}")
        print(f"Valor Total do pedido: R${diasAlugados * listaDiaria[carroAlugado]}")
        print("Digite 1 para confimar o pedido ou 0 para sair")
        confirmarPedido = int(input())
        if confirmarPedido == 1: #verifico se ele quer confirmar o pedido ou voltar para o menu de locação
            os.system("cls")
            iprincipal = 1
        elif confirmarPedido == 0:
            iprincipal = 1
            os.system("cls")
            continue
        alugados[listaCarros[carroAlugado]] = listaDiaria[carroAlugado] #jogo para o dic alugados atraves da minha lista com o indice que captei
        portifolio.pop(listaCarros[carroAlugado]) # apago do meu dic "carros disponiveis"
    return int(confirmarPedido) 

def devolverCarro():
    iprincipal = 0
    while iprincipal == 0:
        print("Lista de carros alugados: ")
        i = 0
        for nome in alugados.keys(): #printo a lista dos carros alugados
            print(i, "-", nome)
            i += 1
        print("Qual o codigo do carro você deseja revolver?")
        devolvendo = int(input()) # pergunto qual o indice do carro que deseja devolver
        print("Devolução realizada com sucesso!")
        listaCarros = list(alugados.keys())
        listaCarrosDiarias = list(alugados.values())
        portifolio[listaCarros[devolvendo]] = listaCarrosDiarias[devolvendo]  #retiro do dic alugados e mando p dic de disponivel novamente
        alugados.pop(listaCarros[devolvendo])
        iprincipal = 1
    return  0

#rodando o sistema em loop infinito
#toda funcao retona um valor para minha variavel opMenu. Ela que controla qual funcao vou chamar em determinado momento
opMenu = 0
while True:
    os.system("cls")
    if opMenu == 0:
        print("===========")
        print("Bem-Vindo a Locadora Viana!")
        print("===========\n")
        print("O que deseja fazer?\n")
        print("[1] - Ver carros disponiveis | [2] - Alugar um carro | [3] - Fazer uma devolução\n")
        opMenu = int(input())

    if opMenu == 1:
        os.system("cls")
        ver = int(verCarros())
        opMenu = ver     
    elif opMenu == 2:
        os.system("cls")
        alugar = int(alugarCarro())
        if alugar == 0:
            opMenu == 2
            continue
        print("-----Pedido Confirmado-----")
        print("\nDigite 0 para voltar") 
        opMenu = int(input())
    elif opMenu == 3:
        os.system("cls")
        devolver = devolverCarro()
        os.system("cls")
        print("-----Devolução Feita com sucesso-----")
        print("Digite 0 para voltar") 
        opMenu = int(input())


