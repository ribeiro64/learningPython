# Rafael Ribeiro Guedes de Oliveira - 201706840030
# Wendel Williams Cardoso dos Santos - 201606840039

class Hash:

    def __init__(self, length):
        self.table = {}
        self.length_max = length

    def hashFunction(self, key):
        value = int(key)
        return value % self.length_max

    def full(self):
        return len(self.table) == self.length_max

    def show(self):
        for i in self.table:
            print("Hash[%d] = " % i, end="")
            print(self.table[i])

    def remove(self, key):
        position = self.search(key)
        if position != -1:
            del self.table[position]
            print("-> Dado da posicao %d apagado" % position)
        else:
            print("Item nao encontrado")

    def search(self, key):
        position = self.hashFunction(key)
        if self.table.get(position) == None:  # se esta posição não existe
            return -1  # saida imediata
        if self.table[position] == key:
            return position
        return -1

    def insert(self, item):
        if self.full():
            print("-> ATENÇÃO Tabela Hash CHEIA")
            return
        position = self.hashFunction(item)
        if self.table.get(position) == None:  # se posicao vazia
            self.table[position] = item
            print("-> Inserido HASH[%d]" % position)
        else:  # se posicao ocupada
            print("-> Ocorreu uma colisao na posicao %d<-" % position)
# fim Classe Hashlinear


hashLength = int(input('Digite o tamanho da tabela hash: '))
table = Hash(hashLength)
print("\n****************************************************")
print("      Tabela HASH Sem Colisões (%d itens) " % hashLength)
print("****************************************************")
for i in range(0, hashLength, 1):
    print("\nInserindo elemento %d" % (i + 1))
    item = input("Digite o valor numerico inteiro: ")
    table.insert(item)
item = input("\nDigite o valor numerico inteiro para buscar: ")
position = table.search(item)
if position == -1:
    print("Item nao encontrado")
else:
    print("Item encontrado na posicao: ", position)
#item = input("\nDigite o valor numerico inteiro para apagar: ")
# table.remove(item)
print("\nImprimindo conteudo")
table.show()
print("\n")
