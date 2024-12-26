#Lazy approach

conjunto = list(range(1, 11))

class Union:
    def __init__(self, conjunto):

      self.conexoes = [conjunto, conjunto] #base id

      pass 

    def busca(self, id):
        id =  self.conexoes[1][id - 1]
        base = self.conexoes[0][id - 1]
    
        while(id != base):
            id = self.conexoes[base][id]

        return id

    def conectado(self, a, b):
      #achar o id 
      root_1 = self.busca(a)
      root_2 = self.busca(b)

      return root_1 == root_2
    

    def conexao(self, a, b):
      if self.conectado( a, b):
        return 
      self.conexoes[1][a - 1] = b
      pass


api = Union(conjunto)

# api.conectado(1, 2)
# api.conexao(3, 4)
# print(api.conectado(3,4))
# api.conexao(5,1)
# api.conexao(4,1)


class UnionRefactor:
  def __init__(self, n):
    #single array for parents
    self.connections = list(range(n))
  def find(self, id):
    #find root parent
    while id != self.connections[id]:
       id = self.connections[id]
    return id
  
  def isConnected(self, a, b):
    return self.find(a) == self.find(b)
    
  def connect(self, a, b):
   
    if not(self.isConnected(a,b)):
       self.connections[a] = b


