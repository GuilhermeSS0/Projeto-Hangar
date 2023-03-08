import time
from datetime import datetime, timedelta

# FUNÇÃO MENU PARA COMEÇAR A DECIDIR AS OPÇÕES


def menu():
    print(" ### Hangares G & F ###")
    print("|1| - Solicitar vaga no hangar!")
    print("|2| - Retirar uma aeronave do hangar!")
    print("|3| - Retirar todas as aeronaves do hangar!")
    print("|4| - Mostrar todas as aeronaves no hangar!")
    print("|5| - Adiantar tempo!")
    print("|6| - Mostrar informações do tempo!")
    print("|7| - Sair!")

    opc = int(input("""
    Opção a seguir? 
    """))

    return opc


# FUNÇÃO PARA ADICIONAR UM AVIÃO AO HANGAR
def solicitar_hangar(hangar, fila_espera, horario, data_programa, cont_entrou):

    vaga = int(input("""
    Insira a identificação da aeronave: """))

    # AQUI VALIDA SE A IDENTIFICAÇÃO TEM 06 DIGITOS E SÓ ACEITA SE TIVER 06 DIGITOS
    while len(str(vaga)) != 6:

        vaga = int(
            input("""
            Insira a identificação da aeronave contendo 06 (SEIS) algarismos!
            """))

    # SE O HANGAR ESTIVER COM MENOS DO QUE O NECESSÁRIO DE AVIÕES VAI VALIDAR E ENTRAR O AVIÃO NO HANGAR
    if len(hangar) < 2:

        hangar.append(vaga)

        tempo = data_programa

        horario.append(tempo)

        cont_entrou += 1

        return hangar, fila_espera, horario, data_programa, cont_entrou

    # SE JÁ TIVER AVIÕES NO HANGAR AQUI VALIDA PARA ENTRAR NA FILA DE ESPERA
    # SE A FILA ESTIVER ZERADA A FILA VIRA A RECEBE A IDENTIFICAÇÃO DA VAGA
    if len(hangar) == 2:

        if fila_espera == 0:

            fila_espera = vaga

            print(f"""
            Identificação da aeronave na fila de espera: {fila_espera}
            """)

            return hangar, fila_espera, horario, data_programa, cont_entrou

        else:
            print("""
            Sem vagas, vá para outro hangar.
            """)

        return hangar, fila_espera, horario, data_programa, cont_entrou


# FUNÇÃO PARA RETIRAR A AERONAVE, QUANDO A IDENTIFICAÇÃO FOR ESCRITA...
# O AVIÃO É RETIRADO DO HANGAR E O QUE ESTA NA FILA DE ESPERA ENTRA NO HANGAR
def retirar_hangar(hangar, fila_espera, cont_saiu, cont_entrou, horario):

    retirar = int(input("""
    Qual aeronave deseja retirar do hangar: 
    """))

    for i in range(len(hangar)):

        if retirar == hangar[i]:

            temporario = horario[i]

            horario.pop(i)

            hangar.pop(i)

    if fila_espera == 1:

        hangar.append(fila_espera)

        fila_espera = 0

        cont_entrou += 1

    cont_saiu += 1

    return hangar, fila_espera, cont_saiu, cont_entrou, horario


# RETIRAR TODOS OS AVIÕES, A LISTA DO HANGAR ZERA E A FILA DE ESPERA TAMBÉM
def retirar_all(hangar, fila_espera):

    hangar = []

    fila_espera = 0

    return hangar, fila_espera


# AQUI MOSTRA AS AERONAVES QUE ESTÃO NO HANGAR
def mostrar_hangar(hangar, horario):

    if hangar != []:

        for i in range(len(hangar)):

            print(f"""
                Aeronaves estacionadas no hangar: Identificação da aeronave: {hangar[i]}.  
                Hora de entrada: {horario[i][3]}:{horario[i][4]}:{horario[i][5]} do dia {horario[i][2]}/{horario[i][1]}/{horario[i][0]}.
                """)

        if fila_espera == 0:

            print("""
                Aeronave na fila de espera: Não há aeronave na espera!
                """)

        else:

            print(f"""
                Aeronave na fila de espera: {fila_espera}.
            """)

    else:

        print("""
        Não há aeronaves no hangar!
        """)


# FUNÇÃO QUE FAZ COM QUE OS DIAS AVANÇEM
def avancar_dias(avancarDias, data_programa):

    data = datetime.fromtimestamp(time.mktime(data_programa))

    avancarDias = int(avancarDias)

    nova_data = data + timedelta(days=avancarDias)

    nova_data = nova_data.timetuple()

    print(
        f"Foram adiantados {avancarDias} dias, agora estamos no dia, {nova_data[2]}/{nova_data[1]}/{nova_data[0]}")

    return nova_data


# FUNÇÃO PARA VER A INFORMAÇÃO DO TEMPO
# PUXA A HORA DO PROGRAMA QUANDO ATUALIZADA TAMBÉM
def info_tempo(data_programa):

    print(f"""
        A Hora do sistema no momento é: {data_programa[3]}:{data_programa[4]}:{data_programa[5]}
        A data do sistema no momento é: {data_programa[2]}/{data_programa[1]}/{data_programa[0]}
        """)


# FUNÇÃO DO CONTADOR DE ENTRADAS, PARA SER CHAMADA.
def contadorE(cont_entrou):

    cont_entrou

    return cont_entrou


# FUNÇÃO DO CONTADOR DE SAIDAS, PARA SER CHAMADA.
def contadorS(cont_saiu):

    cont_saiu

    return cont_saiu


# FUNÇÃO PARA CALCULAR O PAGAMENTO DAS AERONAVES ASSIM QUE SAIREM DO HANGAR
def calcular_pagamento(dias):

    if dias == 0:

        valor_pagar = 127

    elif dias < 30:

        valor_pagar = 127 * dias

    elif dias >= 30:

        valor_pagar = 115 * dias

    return valor_pagar


# VARIÁVEIS UTILIZADAS COMO GLOBAIS PARA PODER INTEGRAR AS FUNÇÕES AS AÇÕES
hangar = []

fila_espera = 0

horario = []

data_programa = time.localtime()

cont_entrou = 0

cont_saiu = 0

opc = 0

opcao = 0


# LAÇO DE REPETIÇÃO DO MENU
while opc != 7:

    opc = menu()

    if opc > 7 or opc < 1:
        print("Inválido - Tente novamente!")

    elif opc == 1:
        hangar, fila_espera, horario, data_programa, cont_entrou = solicitar_hangar(
            hangar, fila_espera, horario, data_programa, cont_entrou)

    elif opc == 2:
        hangar, fila_espera, cont_saiu, cont_entrou, horario = retirar_hangar(
            hangar, fila_espera, cont_saiu, cont_entrou, horario)

    elif opc == 3:
        hangar, fila_espera = retirar_all(hangar, fila_espera)

    elif opc == 4:
        mostrar_hangar(hangar, horario)

    elif opc == 5:

        while opcao != 2:

            opcao = int(input(f"""
                    |1| - Avançar dias.
                    |2| - Sair.
                    Qual sua opção?\n"""))

            if opcao == 1:

                avancarDias = int(input("Quantos dias gostaria de avançar?"))

                data_programa = avancar_dias(avancarDias, data_programa)

            elif opcao == 2:
                break

            else:
                print("Opção Inválida!")

    elif opc == 6:
        info_tempo(data_programa)

    elif opc == 7:

        print(f"""
        Total de aeronaves que pousaram no hangar: {(contadorE(cont_entrou))}
        Total de aeronaves retiradas do hangar: {(contadorS(cont_saiu))}
        Valor em caixa: 
        """)

        print("""
        ### Bon voyage!! ###
        """)
