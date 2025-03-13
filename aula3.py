import os #para utilizar funções do sistema operacional

#definindo as listas que serão utilizadas ao longo do programa
restaurantes = ['Pizzaria', 'Hamburgueria'] 


def exibir_nome_programa():
    print("""𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤""")

def exibirOpcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

#definindo uma função
def finalizar_app():
    exibir_subtitulo('Finalizar app')

def exibir_subtitulo(texto):
    os.system('cls') #o comando é : os.system
    print(texto)
    print('\n')
    
def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()
    
def opcao_invalida(): #criando uma função para casos de erro
    print('Opção inválida\n')
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes')
    
    for restaurante in restaurantes: #estrutura que percorre a lista 
        print(f'- {restaurante}') #imprimirá cada restaurante
    
    voltar_menu()

def cadastrar_novo_restaurante():
    #utilizando uma lista para armazenar as informações do resturante
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante) #adiciono a linha. Chamo o nome dela e utilizo a função append que adiciona um elemento ao final da lista e passo como parâmetro o que quero armazenar na lista
    print(f'O restaurante: {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu()

def escolher_opcao():
    try: #para exceções
        opcao_escolhida = int(input('Escolha uma opção: ')) #precisa transformar em inteiro por causa por padrão é string e no if está como int

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app() #utilizando função para facilitar
        else:
            opcao_invalida()
    except: #aqui entra a exceção, oq não entrar no padrão, no esperado
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibirOpcoes()
    escolher_opcao()

if __name__ == '__main__': #consigo dividir o arquivo em partes para facilitar
    main() #preciso criar uma função principal que contém as outras funções do programa
    

#Loop while
 #É usado quando a qunatidade de iterações é desconhecida
 #Estrutura:
   #while condição:
        #o que será repetido
        
