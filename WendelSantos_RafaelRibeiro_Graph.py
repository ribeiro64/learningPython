# Autores:
# Wendel Williams Cardoso dos Santos - 201606840039
# Rafael Ribeiro Guedes de Oliveira - 201706840030

import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, number_of_vertices):
        self.number_of_vertices = number_of_vertices
        self.graph = [[] for i in range(self.number_of_vertices)]
        self.G = nx.DiGraph()
        self.G.add_edges_from([
            (0, 1), (1, 2), (1, 3), (1, 5), (2, 3), (2, 0), (3, 4),
            (4, 3), (5, 4), (5, 6), (6, 5), (6, 7), (7, 4), (7, 6)
        ])

    def addDirectedEdges(self, u, v):
        self.graph[u].append(v)

    def addNoDirectedEdges(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def showGraph(self):
        print('Grafo em formato lista de listas:')
        print(self.graph)
        print('')

    def showList(self):
        print('Lista de adjacências:')
        for i in range(self.number_of_vertices):
            print('{}: '.format(i), end=' ')
            for j in self.graph[i]:
                print('{} -> '.format(j), end=' ')
            print('')
        print('')

    def existEdge(self, u, v):
        print('Existência de aresta:')
        if v in self.graph[u]:
            print('Existe aresta entre os vértices {} e {}.'.format(u, v))
        else:
            print('Não existe aresta entre os vértices {} e {}.'.format(u, v))
        print('')

    def vertexDegree(self, u):
        print('Grau de um determinado vértice:')
        for i in range(len(self.graph[u])):
            i += 1
        print('O grau do vértice {} é: {}'.format(u, i))
        print('')

    def showAdjacentList(self, u):
        print('Lista de adjacência de um determinado vértice:')
        print('{}: '.format(u), end=' ')
        for j in self.graph[u]:
            print('{} -> '.format(j), end=' ')
        print('\n')

    def dfsVisit(self, u, color, foundCycle):
        graph = {}
        for i in range(len(self.graph)):
            graph[i] = self.graph[i]
        if foundCycle[0]:
            return
        color[u] = 'gray'
        for v in graph[u]:
            if color[v] == 'gray':
                foundCycle[0] = True
                return
            if color[v] == 'white':
                self.dfsVisit(v, color, foundCycle)
        color[u] = "black"

    def cycleExist(self):
        print('Verifica se o grafo é cíclico:')
        graph = {}
        for i in range(len(self.graph)):
            graph[i] = self.graph[i]
        color = {u: 'white' for u in graph}
        foundCycle = [False]
        for u in graph:
            if color[u] == 'white':
                self.dfsVisit(u, color, foundCycle)
            if foundCycle[0]:
                break
        print(graph)
        if foundCycle[0]:
            print('O grafo é cíclico.')
        else:
            print('O grafo á acíclico.')
        print('')

    def connected(self):
        print('Verifica se o grafo é conexo:')

        if nx.is_weakly_connected(self.G):
            print('O grafo é conexo.\n')
        else:
            print('O grafo não é conexo.\n')

    def stronglyConnectedComponents(self):
        print('Verifica quais e quantos são os componentes conexos:')
        numberOfComponents = nx.number_strongly_connected_components(self.G)
        components = nx.strongly_connected_components(self.G)
        print(
            'Número de componentes fortemente conexos: {}'
            .format(
                numberOfComponents
            )
        )
        print('Componentes:')
        for i in components:
            print(i)
        print('')

    def isEuleriano(self):
        print('Verifica se é Euleriano:')
        odd = 0
        for i in range(self.number_of_vertices):
            for j in range(len(self.graph[i])):
                j += 1
            if j % 2 != 0:
                odd += 1
        if odd == 0:
            print('Euleriano')
        elif odd == 2:
            print('Semieuleriano')
        else:
            print('Não é Euleriano.')
        print('')

    def plotGraph(self):
        print('O grafo está plotado...')
        nx.draw(self.G, with_labels=True, font_weight='bold')
        plt.show()


# Defini a quantidade de veŕtices do grafo
G = Graph(8)

# Criando grafo
G.addDirectedEdges(0, 1)
G.addDirectedEdges(1, 2)
G.addDirectedEdges(1, 3)
G.addDirectedEdges(1, 5)
G.addDirectedEdges(2, 0)
G.addDirectedEdges(2, 3)
G.addDirectedEdges(3, 4)
G.addDirectedEdges(4, 3)
G.addDirectedEdges(5, 4)
G.addDirectedEdges(5, 6)
G.addDirectedEdges(6, 5)
G.addDirectedEdges(6, 7)
G.addDirectedEdges(7, 4)
G.addDirectedEdges(7, 6)
# Printa Grafo (Vetor)
G.showGraph()
# Printa toda a lista de adjacência
G.showList()
# Existência de uma determinada aresta
G.existEdge(1, 2)
# Verifica o grau do vértice
G.vertexDegree(1)
# Printa a lista de adjacência de um determinado vértice:
G.showAdjacentList(1)
# Verifica se o grafo é cíclico
G.cycleExist()
# Verifica se o grafo é conexo:
G.connected()
# Informa o número e quais os componentes fortemente conexos:
G.stronglyConnectedComponents()
# Verifica se é Euleriano
G.isEuleriano()
# Plota o grafo
G.plotGraph()
