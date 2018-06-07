class Partita:
    p1=""
    p2=""

    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2

    def turno(self):
        print(self.p1, ' è il tuo turno')
        print(self.p2, ' è il tuo turno')