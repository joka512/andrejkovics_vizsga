import filehendler


class Munkatars():
    munkaslista = []
    fejlec = "nev\tbeosztas\ttelefon\temail"
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
    def save(cls):
        list = []
        for x in cls.munkaslista:
            list = str(x)
        filehendler.save_any(filehendler.paths["munkatarsak"], list)


    @classmethod
    def loadfromfile(cls):
        cls.munkaslista.clear()
        munkasok = filehendler.load_any("munkatarsak")
        for munkas in munkasok:
            munkas=munkas.split(sep="\t")
            cls.munkaslista.append(Munkatars(munkas[0],munkas[1],munkas[2],munkas[3]))


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
        cls.save()

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
        cls.save()

    @classmethod
    def showall(cls):
        print(cls.fejlec)
        if len(cls.munkaslista) == 0:
            print("még nincsenek értékelhető adatok")
        else:
            i=0
            for x in cls.munkaslista:
                print(f"{i}\t{str(x)}")
                i+=1
