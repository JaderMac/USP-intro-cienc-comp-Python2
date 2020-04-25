class DistanciaPontos:

  def definePontoUm(self):
    Xponto1=int(input("Entre com a coordenada X do primeiro ponto: "))
    Yponto1=int(input("Entre com a coordenada Y do primeiro ponto: "))
    return Xponto1, Yponto1

  def definePontoDois(self):
    Xponto2=int(input("Entre com a coordenada X do segundo ponto: " ))
    Yponto2=int(input("Entre com a coordenada Y do segundo ponto: "))
    return Xponto2, Yponto2

  def CalculaDistancia(self, Xponto1, Yponto1, Xponto2, Yponto2):
    Difx = (Xponto1 - Xponto2)**2 
    Dify = (Yponto1 - Yponto2)**2 
    distancia = (Difx + Dify)**(1/2)
    return distancia

  def classificadistancia(self, distancia):
    if distancia > 10:
      return "Longe"
    else:
      return "Perto"

  def main(self):
    p1, p2 = self.definePontoUm()
    p3, p4 = self.definePontoDois()
    dis = self.CalculaDistancia(p1,p2,p3,p4)
    print(self.classificadistancia(dis))

dist = DistanciaPontos().CalculaDistancia(10,10,10,9)
print(dist)