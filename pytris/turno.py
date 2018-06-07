class Partita(object):
    p1=""
    p2=""
    change = True


    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2

    def Mossa(self,p):
        print("Posiziona qualcosa in una casella")

    def Turno(self):
        if(self.change == True):
            p = self.p1
        else:
            p = self.p2
        print(p, ' è il tuo turno')
        self.Mossa(p)

