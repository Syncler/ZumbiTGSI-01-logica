
from Fila import Queue
#chamar a partir da raiz
ROOT = "root"
#arvores = dados não lineares, como filas, pilhas, etc.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.simetric_traversal(node.lefet)
        print(node, edn='\n')
        if node.right:
            self.simetric_traversal(node.right)

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)
#Fila
    def levelorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root

        queue = Queue()
        queue.push(node)
#enquanto a fila nao for 0
        while len(queue):
            node = queue.pop()
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
            print(node, end=" ")
    
#percurso em ordem simetrica
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
#rodar mesma função esquerda
        if node.left:
            self.simetric_traversal(node.left)

#exibição dado central
        print(node)

#rodar mesma função direita
        if node.right:
            self.simetric_traversal(node.right)

#arvore binária de busca:
class BinarySearchTree(BinaryTree):
#inserir:
    def insert(self, value):
#comparação
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
#caso não tenha nenhum dado, x vira raiz
        if parent is None:
            self.root = Node(value)
#valor menor que o parent
        elif value < parent.data:
            parent.left = Node(value)
#caso seja maior
        else:
            parent.right = Node(value)

#buscar
    def search(self, value):
           return self._search(value, self.root)

    def _search(self, value, node):  
        if node is None:
            return node
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)
    
#encontrando minimo
    def min(self, node=ROOT):
        if node == ROOT:
                node = self.root
        while node.left:
                node = node.left
        return node.data
        
#encontrando máximo
    def max(self, node=ROOT):
        if node == ROOT:
                node = self.root
        while node.right:
                node = node.right
        return node.data
    
#remoção
    def remove(self, value, node=ROOT):
        if node == ROOT:
            node = self.root

#implementação recursiva
#caso base:
        if node is None:
            return node
        #menor
        if value < node.data:
            node.left = self.remove(value, node.left)
        #maior
        elif value > node.data:
            node.right = self.remove(value, node.right)
        #igual
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
#substuição
            else:
                substitute = self.min(node.right)
                node.data = substitute
                node.right = self.remove(substitute, node.right)
#termino sem alteração
        return node

if __name__ == "__main__":
    tree = BinaryTree()
    n1 = Node('6')
    n2 = Node('7')
    n3 = Node('10')
    n4 = Node('8')
    n5 = Node('17')
    n6 = Node('15')
    n7 = Node('13')
    n8 = Node('16')
    n9 = Node('20')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2
