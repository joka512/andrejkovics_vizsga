import filehendler
import menü
from munkatars import Munkatars
from gepjarmu import Gepjarmu


class Ertekesites():
    eladasok = []
    def __init__(self,munkatars:str,gepjarmu:str,
                 eladas_datuma, tenyleges_eladasi_ar):

        self.munkatars = munkatars

        self.gepjarmu = gepjarmu
        self.eladas_datuma = eladas_datuma
        self.tenyleges_eladasi_ar = tenyleges_eladasi_ar


    def __str__(self):
        #munkatars=f"{self.munkatars["nev"]}\t{self.munkatars["beosztas"]}\t{self.munkatars["telefon"]}\t{self.munkatars["email"]}\t"
        #gepjarmu=f"{self.gepjarmu["gyartó"]}\t{self.gepjarmu["gyartas_eve"]}\t{self.gepjarmu["modell"]}\t{self.gepjarmu["beszerzesi_ar"]}\t{self.gepjarmu["eladasi_ar"]}"
        return f"{self.munkatars};{self.gepjarmu};{self.eladas_datuma};{self.tenyleges_eladasi_ar}"

    @classmethod
    def addnew(cls):
        eladas = {}
        try:
            print(Munkatars.showall())
            eladas["munkas"] = cls._select("munkatárs")
            print(Gepjarmu.showall())
            eladas["jarmu"] = cls._select("gepjármű")
            eladas["datum"] = str(menü.idopontbekero("eladási"))
            eladas["ar"] = str(cls.mennyiazannyi(eladas["jarmu"]))

        except Exception:
            print("kérlek figyelj jobban")
            eladas = cls.addnew()
        cls.eladasok.append(
            Ertekesites(str(eladas["munkas"]),str(eladas["jarmu"]),eladas["datum"],eladas["ar"])
            )
        cls.save()

    @classmethod
    def delete(cls):
        try:
            x = int(input(f"kérlek add meg a értékesítés sorszámát (0-{len(cls.eladasok) - 1}): "))
            if 0 > x > len(cls.eladasok):
                raise Exception()
            cls.eladasok.pop(__index=(x))

        except Exception:
            print(f"ilyen sorszámú munkatárs nincs, kérlek figyelj oda jobban!")
            cls.delete()
        cls.save()

    @classmethod
    def showall(cls):
        if len(cls.eladasok) == 0:
            print("még nincsenek értékelhető adatok")
        else:
            i=0
            for x in cls.eladasok:
                print(f"{i}\t{str(x)}")
                i+=1

    @classmethod
    def _select(cls,mit):
        try:
            if mit == "munkatárs":
                x = int(input(f"kérlek add meg a munkatárs sorszámát (0-{len(Munkatars.munkaslista)-1})"))
                if 0> x > len(Munkatars.munkaslista)-1:
                    raise ValueError
                miez = Munkatars.munkaslista[x]
            elif mit == "gepjármű":
                x = int(input(f"kérlek add meg a gépjármű sorszámát (0-{len(Gepjarmu.jarmulista)-1})"))
                if 0> x > len(Gepjarmu.jarmulista)-1:
                    raise ValueError
                miez= Gepjarmu.jarmulista[x]
            else: return -1

        except Exception:
            print(f"nincs ilyen {mit}, kérlek figyelj jobban")
            miez = cls._select(mit)
        return miez

    @classmethod
    def mennyiazannyi(cls,jarmu):
        x = int(input("kérlek add meg az eladási árat (-1 ha listaáron kelt el)"))
        if x == -1:
            x = jarmu.potencialis_eladasi_ar
        return x

    @classmethod
    def loadfromfile(cls):
        cls.eladasok.clear()
        datalist=filehendler.load_any(filehendler.paths["eladasok"])
        for data in datalist:
            data=data.split(sep=";")
            cls.eladasok.append(Ertekesites(data[0],data[1],data[2],data[3]))

    @classmethod
    def save(cls):
        list = []
        for x in cls.eladasok:
            list = str(x)
        filehendler.save_any(filehendler.paths["eladasok"],list)