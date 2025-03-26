from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): #herdará da classe itemcardapio
    def __init__(self, nome, preco, descricao): 
        super().__init__(nome, preco) #super permite o acesso à outra classe e faz esta classe herdar da outra
        self.descricao = descricao #porque descrição é referente a prato
        
    def __str__(self):
        return self._nome