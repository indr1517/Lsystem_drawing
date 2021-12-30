class Lsystem:
    def __init__(self, Omega, P):
        self.v = set(Omega + "".join(P.values()))
        self.Omega = Omega
        self.state = Omega
        self.P = P
        self.production = str.maketrans(P)

    def derive(self, n=1):
        for _ in range(n):
            self.state = self.state.translate(self.production)

    def set_Omega(self,sentence):
        self.Omega = sentence
        self.state = sentence

    def set_production(self,k,v):
        self.P[k] = v
        self.production = str.maketrans(self.P)

    def get_state(self):
        return self.state