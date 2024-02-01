



class Munkatars():
    munkaslista = []
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

    @classmethod
    def addmunkas(cls):
        munkas = {}
        try:
            munkas["nev"]=input("kérlek add meg az új munkatárs nevét: ")
            munkas["beosztas"]=input("kérlek add meg az új munkatárs beosztasat: ")
            munkas["tel"]=input("kérlek add meg az új munkatárs telefonszámát: ")
            munkas["email"]=input("kérlek add meg az új munkatárs emailcímét: ")
        except Exception:
            print("kérlek figyelj jobban")
            munkas = cls.addmunkas()
        cls.munkaslista.append(Munkatars(munkas["nev"],munkas["beosztas"],munkas["tel"],munkas["email"]))

    @classmethod
    def delete(cls):
        try:
            x = int(input(f"kérlek add meg a munkatars sorszámát (0-{len(cls.munkaslista) - 1}): "))
            if 0> x > len(cls.munkaslista):
                raise Exception()
            cls.munkaslista.pop(__index=(x))

        except Exception:
            print(f"ilyen sorszámú munkatárs nincs, kérlek figyelj oda jobban!")
            cls.deleter()