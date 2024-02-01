



class Munkatars():
    def __init__(self,nev,beosztas,telefon,email):
        self.nev = nev
        self.beosztas = beosztas
        self.telefon = telefon
        self.email = email


    def __str__(self):
        return (f"{self.nev}\t"
                f"{self.beosztas}\t"
                f"{self.telefon}\t"
                f"{self.email}")


