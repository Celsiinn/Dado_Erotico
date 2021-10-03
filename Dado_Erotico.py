import time
import emoji
from random import*

def separador():
    print("*-------------------------------------------------------------------------------------------------*")










print("*--------------BEM VINDO AOS JOGOS DE DADOS EROTICOS PARA HETEROS-------------------------------*")
print(emoji.emojize("\n 1 - Acoes :heart_eyes: \n 2 - Posicoes :smiling_imp: \n 3 - Lugares :house:\n 4 - Roupa :bikini:", use_aliases=True))
print("")
escolha_dos_dados = int(input("Digite sua escolha"))
separador()
if escolha_dos_dados == 1:  #codigo do jogo de acao
    print("*-------------------------BEM VINDO AO JOGO DE DADOS COM ACOES------------------*")
    while escolha_dos_dados == 1:
        acao = ["Dar uma Chupada leve", "Passar a mao" , "Dar um Beijo" , "Dar uma Chupada com vontade" ,"Passar a Lingua"]
        parte_do_corpo = ["no Peito", "na Buceta", "em Qualquer parte do corpo", "na Raba","no Pesoço"]
        acao_escolhida = choice(acao)
        parte_escolhida = choice(parte_do_corpo)
        print(f"Voce deve {acao_escolhida} {parte_escolhida} ")
        time.sleep(1)
        if escolha_dos_dados !=1:
            break
elif escolha_dos_dados == 2: #Codigo do jogo de posicao
    print("*--------------------JOGO DE POSICOES SEXUAIS-------------------------------------*")
    print("")
    posicoes = ["Lancadora", "Caranguejo", "Picada do Escorpiao", "Trapezio", "Arco", "Espelho do Prazer", "Sonolenta", "Molde","Libelula", "Marqueza", "Maripoza", "Cadeira","Surpresa", "Arvore", "Mochila", "Joelhos", "Ponte"]
    posicao_sorteada = choice(posicoes)
    print(f"A posicao escolhida foi {posicao_sorteada}")
    print('')
    print("*---------------------#USEM CAMISINHA#--------------------------------------------*")
    print('')
    print("Deseja Sortear outra Posicao? \n 1 - SIM \n 2 - NAO")
    outra_posicao = int(input("Digite sua escolha"))

    while outra_posicao == 1:
        print("*--------------------JOGO DE POSICOES SEXUAIS-------------------------------------*")
        print("")
        posicoes = ["Lancadora", "Caranguejo", "Picada do Escorpiao", "Trapezio", "Arco" , "Espelho do Prazer", "Sonolenta", "Molde","Libelula", "Marqueza", "Maripoza", "Cadeira","Surpresa", "Arvore", "Mochila", "Joelhos", "Ponte"]
        lugares = ["Quarto" , "Sala" , "Banheira ou Chuveiro","Cozinha"]
        posicao_sorteada = choice(posicoes)
        print(f"A posicao escolhida foi {posicao_sorteada}")
        print('')
        print("*---------------------#USEM CAMISINHA#--------------------------------------------*")
        print('')
        print("Deseja Sortear outra Posicao? \n 1 - SIM \n 2 - NAO")
        outra_posicao = int(input("Digite sua escolha"))
        if outra_posicao != 1:
            break
elif escolha_dos_dados == 3: # Codigo de jogo dos lugares
    print("*--------------------JOGO DOS LUGARES-------------------------------------*")
    print("")
    lugares = ["Quarto" , "Sala" , "Banheira ou Chuveiro","Cozinha"]
    lugar_escolhido = choice(lugares)
    posicoes = ["Lancadora", "Caranguejo", "Picada do Escorpiao", "Trapezio", "Arco", "Espelho do Prazer", "Sonolenta", "Molde", "Libelula", "Marqueza", "Maripoza", "Cadeira","Surpresa", "Arvore", "Mochila", "Joelhos", "Ponte"]
    lugares = ["Quarto" , "Sala" , "Banheira ou Chuveiro","Cozinha"]
    posicao_sorteada = choice(posicoes)
    print(f"O Lugar escolhido foi {lugar_escolhido} e a posicao sugerida foi a {posicao_sorteada}")
    print('')
    print("*---------------------#USEM CAMISINHA#--------------------------------------------*")
    print('')
    print("")
    print("Deseja Sortear outra Posicao? \n 1 - SIM \n 2 - NAO")
    outro_lugar = int(input("Digite sua escolha"))

    while outro_lugar == 1:
        print("*--------------------JOGO DOS LUGARES-------------------------------------*")
        print("")
        lugares = ["Quarto", "Sala", "Banheira ou Chuveiro", "Cozinha"]
        lugar_escolhido = choice(lugares)
        posicoes = ["Lancadora", "Caranguejo", "Picada do Escorpiao", "Trapezio", "Arco" , "Espelho do Prazer", "Sonolenta", "Molde", "Libelula", "Marqueza", "Maripoza", "Cadeira","Surpresa", "Arvore", "Mochila", "Joelhos", "Ponte"]
        lugares = ["Quarto" , "Sala" , "Banheira ou Chuveiro","Cozinha"]
        posicao_sorteada = choice(posicoes)
        print(f"O Lugar escolhido foi {lugar_escolhido} e a posicao sugerida foi a {posicao_sorteada}")
        print('')
        print("*---------------------#USEM CAMISINHA#--------------------------------------------*")
        print("")
        print("Deseja Sortear outra Lugar e Posicao? \n 1 - SIM \n 2 - NAO")
        outro_lugar = int(input("Digite sua escolha"))
        if outro_lugar != 1:
            break


elif escolha_dos_dados == 4: # Codigo de peca de roupa
    print("*----------------------JOGO DA PECA DE ROUPA--------------------------")
    print("")
    peca_de_roupa_masculina = ["Camisa", "Calca ", "Cueca"]
    peca_de_roupa_feminina = ["Camisa", "Calca", "Sutian", "Calcinha"]
    escolha_masculina = choice(peca_de_roupa_masculina)
    escolha_feminina = choice(peca_de_roupa_feminina)
    print(f"Homem tire a (o) {escolha_feminina} da sua parceira")
    print(f"Mulher tire a {escolha_masculina} do seu parceiro")
    print("")
    print("Deseja Sortear outra peca de roupa? \n 1 - SIM \n 2 - NAO")
    outro_peca = int(input("Digite sua escolha"))

    while outro_peca == 1:
        print("*----------------------JOGO DA PECA DE ROUPA--------------------------")
        print("")
        peca_de_roupa_masculina = ["Camisa", "Calca ", "Cueca"]
        peca_de_roupa_feminina = ["Camisa", "Calca", "Sutian", "Calcinha"]
        escolha_masculina = choice(peca_de_roupa_masculina)
        escolha_feminina = choice(peca_de_roupa_feminina)
        print(f"Homem tire a (o) {escolha_feminina} da sua parceira")
        print(f"Mulher tire a {escolha_masculina} do seu parceiro")
        print("")
        print("Deseja Sortear outra peca de roupa? \n 1 - SIM \n 2 - NAO")
        outro_peca = int(input("Digite sua escolha"))
        if outro_peca != 1:
            break





