class HashLinearColisao:

    def __init__(self, length):
        self.table = {}
        self.max_length = length

    def hashFunction(self, key):
        value = int(key)
        return (value % int(self.max_length))

    def full(self):
        return len(self.table) == self.max_length

    def show(self):
        for i in self.table:
            print("Hash[%d] = " % i, end="")
            print(self.table[i])

    def apaga(self, key):
        position = self.search(key)
        if position != -1:
            del self.table[position]
            print("-> Item da posicao %d apagado <-" % position)
        else:
            print("-> Item nao encontrado <-")

    def search(self, key):
        position = self.hashFunction(key)
        if self.table.get(position) == None:  # se esta posição não existe
            return -1  # saida imediata
        if self.table[position] == key:  # se o item esta na posição indicada pela função hash
            return position
        else:
            # busca do item em toda hash (pois ele pode ter sido inserido apos colisão)
            for i in self.table:
                if self.table[i] == key:
                    return i
        return -1

    def insert(self, item):
        if self.full():
            print("-> ATENÇÃO Tabela Hash CHEIA")
            return
        position = self.hashFunction(item)
        if self.table.get(position) == None:  # se posicao vazia
            self.table[position] = item
            print("-> Inserido HASH[%d] <-" % position)
        else:  # se posicao ocupada
            print("-> Ocorreu uma colisao na posicao %d <-" % position)
            while True:
                if self.table[position] == item:  # se o item ja foi cadastrado
                    print("-> ATENCAO Esse item ja foi cadastrado")
                    return
                if position == (self.max_length - 1):
                    position = -1
                position = position + 1  # incrementa mais uma posição
                if self.table.get(position) == None:
                    self.table[position] = item
                    print("-> Inserido apos colisao HASH[%d]" % position)
                    break


hashLength = int(input('Digite o tamanho da tabela hash: '))
table = HashLinearColisao(hashLength)
print("\n****************************************************")
print("      Tabela HASH Colisoes Linear (%d itens) " % hashLength)
print("****************************************************")
for i in range(0, hashLength, 1):
    print("\nInserindo item %d" % (i + 1))
    item = input("Digite o valor numérico inteiro: ")
    table.insert(item)
item = input("\nDigite o valor numérico para buscar: ")
position = table.search(item)
if position == -1:
    print("-> Item nao encontrado <-")
else:
    print("-> Item encontrado na posicao: <-", position)
#item = input("\n - Forneca valor para apagar: ")
# tab.apaga(item)
#print("\nImprimindo conteudo")
table.show()
print("\n")
