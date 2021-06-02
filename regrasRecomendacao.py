
"""
@author: Joao da Silva Muniz Neto && Mateus Monteiro Santos
"""

from experta import Rule, Fact, KnowledgeEngine, AND

#classe de regras para a recomendacao do carro
class RegrasRecomendacao(KnowledgeEngine):
    #variaveis para as respostas
    carro = ""
    cordoCarro = ""
    precodoCarro = ""

    #regra 1 - polo -> hatch, 1.0t, automatico, ar condicionado, vidros eletricos 
    @Rule( AND(  Fact(tipoHatch='True'), Fact(motor1t='True') ,Fact(automatico='True'),Fact(ar_condicionado='True'),Fact(vidros_eletricos='True')) )
    def escolhaPolo(self):
        self.carro = "Polo 1.0 turbo"
        self.cordoCarro = "Azul, cinza, branco, preto e vermelho"
        self.precodoCarro = "R$ 80.000,00"

    #regra 2 - UP -> hatch, 1.0t, manual, vidros eletricos
    @Rule( AND(  Fact(tipoHatch='True'), Fact(motor1t='True') ,Fact(manual='True'),Fact(vidros_eletricos='True')) )
    def escolhaUp(self):
        self.carro = "Up 1.0 turbo"
        self.cordoCarro = "Azul, cinza e vermelho"
        self.precodoCarro = "R$ 50.000,00"

    #regra 3 - virtus -> seda, 1.0t, manual, ar condicionado, direcao eletrica, vidros eletricos
    @Rule( AND(  Fact(tipoSeda='True'), Fact(motor1t='True') ,Fact(manual='True'), Fact(ar_condicionado='True'), Fact(direcao_eletrica='True'), Fact(vidros_eletricos='True')) )
    def escolhaVirtus(self):
        self.carro = "Virtus 1.0 turbo"
        self.cordoCarro = "Azul, verde, cinza e vermelho"
        self.precodoCarro = "R$ 90.000,00"
    
    #regra 4 - tcross -> suv, 1.4t, manual, ar condicionado, farol, vidro eletrico, camera de re
    @Rule( AND(  Fact(tipoSuv='True'), Fact(motor14t='True') ,Fact(manual='True'), Fact(ar_condicionado='True'), Fact(farol_de_milha='True'),  Fact(vidros_eletricos='True'), Fact(camera_de_re='True'),) )
    def escolhaTcross(self):
        self.carro = "T-cross 1.4 turbo"
        self.cordoCarro = "Azul e vermelho"
        self.precodoCarro = "R$ 110.000,00"    

    #regra 5 - tiguan -> suv, 1.4t, automatico, ar condicionado, farol de milha, camera de re, direcao eletrica, vidros eletricos, piloto automatico
    @Rule( AND(  Fact(tipoSuv='True'), Fact(motor14t='True') ,Fact(automatico='True'), Fact(ar_condicionado='True'), Fact(farol_de_milha='True'), Fact(camera_de_re='True'), Fact(direcao_eletrica='True'), Fact(vidros_eletricos='True'), Fact(piloto_automatico='True')) )
    def escolhaTiguan(self):
        self.carro = "Tiguan 1.4 turbo"
        self.cordoCarro = "Preto e branco"
        self.precodoCarro = "R$ 140.000,00"

    #regra 6 - jetta -> seda, 2.0t, automatico, ar condicionado, farol de milha, camera de re, direcao eletrica, vidros eletricos, piloto automatico
    @Rule( AND(  Fact(tipoSeda='True'), Fact(motor2t='True') ,Fact(automatico='True'), Fact(ar_condicionado='True'), Fact(farol_de_milha='True'), Fact(camera_de_re='True'), Fact(direcao_eletrica='True'), Fact(vidros_eletricos='True'), Fact(piloto_automatico='True')) )
    def escolhaJetta(self):
        self.carro = "Jetta 2.0 turbo"
        self.cordoCarro = "Vermelho e branco"
        self.precodoCarro = "R$ 160.000,00"