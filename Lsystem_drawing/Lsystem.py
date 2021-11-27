class Lsystem:
    def __init__(self, Omega, P):
        self.v = set(Omega + "".join(P.values()))
        self.state = Omega
        self.production = str.maketrans(P)

    def derive(self, n=1):
        for _ in range(n):
            self.state = self.state.translate(self.production)
