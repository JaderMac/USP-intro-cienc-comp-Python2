import ex
import pytest

class testaDistanciaPontos:
    @pytest.mark.parametrize("ent1, ent2, ent3, ent4, saida",[
    (1,1,1,1,0),
    (1,1,2,2,1.41),
    (10,10,20,20,14.14),
    (10,10,10,9,1),
    ])
    def testa_CalculaDistancia(self,ent1, ent2, ent3, ent4, saida):
        assert Distanciapontos().CalculaDistancia(ent1, ent2, ent3, ent4) == saida