class Weighted_quick_union:
  def __init__(self, n):
    #single array for parents
    self.connections = [list(range(n)), [1] * n]
    
  def debug(self):
    print(self.connections)

  def find(self, id):
    root = id
    # Primeiro, encontra a raiz
    while root != self.connections[0][root]:
        root = self.connections[0][root]

    # Depois, comprime o caminho
    while id != root:
        parent = self.connections[0][id]
        self.connections[0][id] = root  # Atualiza o pai para a raiz
        id = parent

    return root
  
  def isConnected(self, a, b):
    return self.find(a) == self.find(b)
    
  def connect(self, a, b):
    root_1 = self.find(a)
    root_2 = self.find(b)

    if root_1 == root_2: return

    if self.connections[1][root_1] < self.connections[1][root_2]:
      self.connections[0][root_1] = root_2
      self.connections[1][root_2] += self.connections[1][root_1]
    else:
      self.connections[0][root_2] = root_1
      self.connections[1][root_1] += self.connections[1][root_2] 

  def debugIsconnected(self,a,b):
    print(self.isConnected(a,b))

api = Weighted_quick_union(10)
api.connect(0,1)
api.connect(0,2)
api.connect(0,4)
api.connect(0,3)
api.connect(0,5)
api.connect(8,7)
api.connect(8,9)
api.connect(6,7)
api.connect(3,6)
api.isConnected(4,8)
api.debug()
