import filehendler



class Gepjarmu():
    jarmulista = []
    def __init__(self,gyarto,gyartas_eve,modell,
                 onkoltsegi_ar,potencialis_eladasi_ar):
        self.gyarto_neve = gyarto
        self.gyartas_eve = gyartas_eve
        self.modell = modell
        self.onkoltsegi_ar = onkoltsegi_ar
        self.potencialis_eladasi_ar = potencialis_eladasi_ar

    def __str__(self):
        return (f"{self.gyarto_neve}\t"
                f"{self.gyartas_eve}\t"
                f"{self.modell}\t"
                f"{self.onkoltsegi_ar}\t"
                f"{self.potencialis_eladasi_ar}")

    @classmethod
    def addjarmu(cls):
        jarmu = {}
        try:
            jarmu["gyartó"] = input("kérlek add meg a gépjármű gyártóját: ")
            jarmu["gyartas_eve"] = input("kérlek add meg a gépjármű gyártási évét: ")
            jarmu["modell"] = input("kérlek add meg a gépjármű modellt: ")
            jarmu["besz"] = int(input("kérlek add meg a gépjármű önköltségi árát: "))
            jarmu["eladasi_ar"] = int(input("kérlek add meg a gépjármű potenciális eladási árát: "))
        except Exception:
            print("kérlek figyelj jobban")
            jarmu = cls.addjarmu()
        cls.jarmulista.append(Gepjarmu(jarmu["gyartó"],jarmu["gyartas_eve"],jarmu["modell"],jarmu["besz"],jarmu["eladasi_ar"]))

    @classmethod
    def delete(cls):
        try:
            x = int(input(f"kérlek add meg a munkatars sorszámát (0-{len(cls.jarmulista) - 1}): "))
            if 0> x > len(cls.jarmulista):
                raise Exception()
            cls.jarmulista.pop(__index=(x))

        except Exception:
            print(f"ilyen sorszámú munkatárs nincs, kérlek figyelj oda jobban!")
            cls.delete()

    @classmethod
    def showall(cls):
        if len(cls.jarmulista) == 0:
            print("még nincsenek értékelhető adatok")
        else:
            for x in range(len(cls.jarmulista) - 1):
                print(f"{x}\t{cls.jarmulista[x]}")

    @classmethod
    def loadfromfile(cls):
        cls.jarmulista.clear()
        datalist = filehendler.load_any(filehendler.paths["gepjarmuvek"])
        for data in datalist:
            data = data.split(sep="\t")
            cls.jarmulista.append(Gepjarmu(data[0], data[1], data[2], int(data[3]),int(data[4])))

    @classmethod
    def save(cls):
        list = []
        for x in cls.jarmulista:
            list = str(x)
        filehendler.save_any(filehendler.paths["gepjarmuvek"], list)