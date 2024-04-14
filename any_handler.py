

from dataclasses import dataclass
import datetime
import enum

from filehendler import FileHandler
from menü import idopontbekero

class MyType(enum.Enum):
    EMP = 0
    VEH = 1
    SEL = 2


@dataclass
class Munkas():
    nev :str
    beosztas :str
    telefon :str
    email :str
@dataclass
class Gepjarmu():
    gyarto_neve :str
    gyartas_eve :int
    modell :str
    onkoltsegi_ar :int
    potencialis_eladasi_ar :int

@dataclass
class Eladas():
    dolgozo :dict 
    gepjarmu:dict
    eladas_datuma:str
    tenyleges_eladasi_ar :int

def fejlecprinter(d):
    ezeladas= False
    print(f"{"Nr.":<4}",end="|")
    for i,j in d.items():
        #print(type(j))
        ezeladas = type(j)==dict
        if ezeladas and i=="dolgozo" :
            print(f"{i:^63}",end="|")
        elif ezeladas and i=="gepjarmu":
            print(f"{i:^79}",end="|")
        else:
            print(f"{i:^15}",end="|")
    print("")
    if "dolgozo" in d:
        print(f"{"":<4}",end="|")
        for i,j in d.items():
            if i=="dolgozo" or i=="gepjarmu":
                for x,y in j.items():
                    print(f"{x:^15}",end="|")   
            else:
                print(f"{"":^15}",end="|")
        print("")



def add(this,to):
    to.append(vars(this))
    

def delete(this,_from):
    _from.pop(this)

def select(_from:list | None = None,tipe=MyType.EMP) -> int:
    if _from != None:
        if not show(_from):
            print("ellőbb hozd létre! tessék a lehetőség adott!")
            match tipe:
                case MyType.EMP:
                    add(this=uj_munkas(),to=_from)
                    FileHandler.save_any(path=FileHandler.MUNKATARSAK,data=_from)
                case MyType.VEH:
                    add(this=uj_jarmu(),to=_from)
                    FileHandler.save_any(path=FileHandler.GEPJARMUVEK,data=_from)
                case MyType.SEL:
                    add(this=uj_eladas(),to=_from)
                    FileHandler.save_any(path=FileHandler.ELADASOK,data=_from)
            show(_from)

    try:
        r =  int(input("kérlek add meg az elem sorszámát: "))
    except:
        print("számot adj meg kérlek!")
        r = select()
    return r

def get(_from,selected):
    return _from[selected]

def show(this):
    if len(this)==0:
        print("még nincsenek értékelhető adatok")
        return False
    else:
        for i,d in enumerate(this):
            if i==0:fejlecprinter(d)
            print(f"{i:^4}",end="|")

            for x,y in d.items():
                if type(y)==dict:
                    for a,b in y.items():
                        print(f"{b:^15}",end="|")
                else:
                    print(f"{y:^15}",end="|")
            print("")
        return True

def uj_munkas():
    
    try:
        munkas = Munkas(
        nev=input("kérlek add meg az új munkatárs nevét: "),
        beosztas=input("kérlek add meg az új munkatárs beosztasat: "),
        telefon=input("kérlek add meg az új munkatárs telefonszámát: "),
        email=input("kérlek add meg az új munkatárs emailcímét: "))
    except Exception as e:
        print(f"kérlek figyelj jobban, itt a baki {e}")
        munkas = uj_munkas()
    return munkas

def uj_jarmu():
        
        try:
            jarmu= Gepjarmu(
                gyarto_neve= input("kérlek add meg a gépjármű gyártóját: "),
                gyartas_eve= int(input("kérlek add meg a gépjármű gyártási évét: ")),
                modell =input("kérlek add meg a gépjármű modellt: "),
                onkoltsegi_ar = int(input("kérlek add meg a gépjármű önköltségi árát: ")),
                potencialis_eladasi_ar = int(input("kérlek add meg a gépjármű potenciális eladási árát: ")))
        except Exception:
            print("kérlek figyelj jobban")
            jarmu = uj_jarmu()
        return jarmu

def mennyiazannyi(gepjarmu)->int:
    try:
        ar =  int(input("kérlek add meg az eladási árat (-1 ha listaáron kelt el)"))
        if ar == -1:
            ar = gepjarmu["potencialis_eladasi_ar"]
        return ar
    except:
        print("P.L.S... egy ár csak számokbol áll!")
        ar = mennyiazannyi(gepjarmu)
    return ar

def uj_eladas(dolgozok,jarmuvek):
    dolgozo=get(dolgozok,selected=select(dolgozok))
    gepjarmu=get(jarmuvek,selected=select(jarmuvek))
    datum = idopontbekero("értékesítési")
    tenyleges_eladasi_ar=mennyiazannyi(gepjarmu=gepjarmu)

    eladas = Eladas(dolgozo=dolgozo,
                    gepjarmu=gepjarmu,
                    eladas_datuma= str(datum),
                    tenyleges_eladasi_ar=tenyleges_eladasi_ar)
    return eladas


    