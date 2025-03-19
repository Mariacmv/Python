#1:
# Crie uma classe chamada ContaBancaria com um construtor que aceita
# os parâmetros titular e saldo. Inicie o atributo ativo como False 
# por padrão.

class ContaBancaria:
    def __init__(self, titular='', saldo=0, ativo=False):
        self.titular = titular
        self.saldo = saldo
        self.ativo = ativo #se passar um valor padrão nos parâmetros então não é necessário passar na inicialização

#2:
# Na classe ContaBancaria, adicione um método especial __str__ que 
# retorna uma mensagem formatada com o titular e o saldo da conta. 
# Crie duas instâncias da classe e imprima essas instâncias.

    def __str__(self):
        return f'Titular: {self.titular} | Saldo: {self.saldo}'
    
# conta1 = ContaBancaria(titular = 'Maria', saldo = 3000)
# print(conta1)
# conta2 = ContaBancaria(titular = 'Magda', saldo = 10000)
# print(conta2)

#3:
# Adicione um método de classe chamado ativar_conta à classe 
# ContaBancaria que define o atributo ativo como True. Crie uma 
# instância da classe, chame o método de classe e imprima o valor de 
# ativo.

    @classmethod
    def ativar_conta(cls):
        ativo = True

#4:
# Refatore a classe ContaBancaria para utilizar a abordagem 
# "pythonica" na criação de atributos. Utilize propriedades, se 
# necessário.

#5:
# Crie uma instância da classe e imprima o valor da propriedade 
# titular.

#6:
# Crie uma classe chamada ClienteBanco com um construtor que aceita 5
# atributos. Instancie 3 objetos desta classe e atribua valores aos 
# seus atributos através do método construtor.

#7:
# Crie um método de classe para a conta ClienteBanco.

