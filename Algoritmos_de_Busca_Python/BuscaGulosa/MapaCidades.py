class cidade:
    def __init__(self,nome,distanciaObjetivo):
        self.nome = nome
        self.visitado = False
        self.distanciaObjetivo = distanciaObjetivo
        self.adjacentes = []
        
    def addCidadesAdjacentes(self,cidade):
        self.adjacentes.append(cidade)

'''c = cidade("teste")
c.nome
c.visitado'''