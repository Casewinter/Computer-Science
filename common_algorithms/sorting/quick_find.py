conjunto = list(range(1, 11))

class Union:
    def __init__(self, conjunto):

      self.conexoes = [conjunto, conjunto] #base id

      pass 

    def conectado(self, a, b):
      #achar o id referente
      id_1 = self.conexoes[1][a -1]
      id_2 = self.conexoes[1][b -1]
      print(self.conexoes)
      return id_1 == id_2 

    def conexao(self, a, b):
      if self.conectado( a, b):
        return 

      id_1 = self.conexoes[1][a -1]
      id_2 = self.conexoes[1][b -1]

      for i, id in enumerate(self.conexoes[1]):
        if id == id_1:
          self.conexoes[1][i] = id_2

      pass


api = Union(conjunto)

print(api.conectado(1, 2))
api.conexao(3,4)
api.conexao(5,1)
api.conexao(4,1)
print(api.conectado(3, 4))