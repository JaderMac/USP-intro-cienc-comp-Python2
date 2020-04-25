class Triangulo:

    def __init__(self, ladoa, ladob, ladoc):
        self.ladoa = ladoa
        self.ladob = ladob
        self.ladoc = ladoc
    
    def a(self):
        return self.ladoa

    def b(self):
        return self.ladob

    def c(self):
        return self.ladoc

    def perimetro(self, ladoa, ladob, ladoc):
        return ladoa + ladob + ladoc

