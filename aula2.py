import os #para utilizar funções do sistema operacional

def exibir_nome_programa():
    print("""𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤""")

def exibirOpcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

#definindo uma função
def finalizar_app():
    os.system('cls') #o comando é: os.system
    print('Finalizando o app\n')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: ')) #precisa transformar em inteiro por causa por padrão é string e no if está como int

    if opcao_escolhida == 1:
        print('Cadastrar restaurante\n')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizar_app() #utilizando função para facilitar

def main():
    exibir_nome_programa()
    exibirOpcoes()
    escolher_opcao()

if __name__ == '__main__': #consigo dividir o arquivo em partes para facilitar
    main() #preciso criar uma função principal que contém as outras funções do programa
    


#Para versatilizar ainda mais e tornar o código menos complexo, existe
#a função match() que é basicamente um switch
#Estrutura do match():
# match expressao:
#     case padrao_1:
#         código a ser executado
#     case padrao_2:
#         código a ser executado
#     case _:
#         código a ser executado caso os outros padrões não forem atendidos