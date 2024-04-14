from any_handler import MyType, add, delete, get, select, show, uj_eladas, uj_jarmu, uj_munkas
from filehendler import FileHandler
import menü
import datetime
from munkatars import Munkatars
from gepjarmu import Gepjarmu
from eladasok import Ertekesites
import sys

dolgozok:list = []
gepjarmuvek:list = []
ertekesitesek:list = []

def loader():
    global dolgozok
    global gepjarmuvek
    global ertekesitesek
    try:
        dolgozok = FileHandler.load_any(FileHandler.MUNKATARSAK)
    except:pass
    try:
        gepjarmuvek = FileHandler.load_any(FileHandler.GEPJARMUVEK)
    except:pass
    try:
        ertekesitesek = FileHandler.load_any(FileHandler.ELADASOK)
    except:pass
    

def munkatars_kezelo():
    global dolgozok
    global gepjarmuvek
    global ertekesitesek
    sel = menü.munkatars_menu(dolgozok)
    if sel==1:
        add(this=uj_munkas(),to=dolgozok)
        FileHandler.save_any(path=FileHandler.MUNKATARSAK,data=dolgozok)
    elif sel == 2:
        delete(select(_from=dolgozok,tipe=MyType.EMP),dolgozok)
        FileHandler.save_any(path=FileHandler.MUNKATARSAK,data=dolgozok)
    elif sel==3:
        pass


def gepjarmu_kezelo():
    global dolgozok
    global gepjarmuvek
    global ertekesitesek
    sel = menü.gepjarmu_menu(gepjarmuvek)
    if sel == 1:
        add(this=uj_jarmu(),to=gepjarmuvek)
        FileHandler.save_any(path=FileHandler.GEPJARMUVEK,data=gepjarmuvek)
    elif sel == 2:
        delete(select(_from=gepjarmuvek,tipe=MyType.VEH),gepjarmuvek)
        FileHandler.save_any(path=FileHandler.GEPJARMUVEK,data=gepjarmuvek)
    elif sel == 3:
        pass

def ertekesites_kezelo():
    global dolgozok
    global gepjarmuvek
    global ertekesitesek
    sel = menü.ertekesites_menu(ertekesitesek)
    if sel == 1:
        add(this=uj_eladas(dolgozok=dolgozok,jarmuvek=gepjarmuvek),to=ertekesitesek)
        FileHandler.save_any(path=FileHandler.ELADASOK,data=ertekesitesek)
    elif sel == 2:
        delete(select(_from=ertekesitesek,tipe=MyType.SEL),ertekesitesek)
        FileHandler.save_any(path=FileHandler.ELADASOK,data=ertekesitesek)
    elif sel == 3:
        pass


def datumszuro():
    global dolgozok
    global gepjarmuvek
    global ertekesitesek
    eredmeny:list = []
    datum = menü.idopontbekero("keresett")
    for i in ertekesitesek:
        d = i["eladas_datuma"].strip().split(sep="-")
        d = datetime.date(year=int(d[0]),
                            month=int(d[1]),
                            day=int(d[2]))
        if d == datum:
            eredmeny.append(i)
    namilegyen(eredmeny)


def intervallumszuro(returnable = False)-> list|None:
    global ertekesitesek
    eredmeny:list = []
    datum = menü.intervall()
    for i in ertekesitesek:
        d = i["eladas_datuma"].strip().split(sep="-")
        d = datetime.date(year=int(d[0]),
                            month=int(d[1]),
                            day=int(d[2]))
        if datum["start"] <= d <= datum["stop"]:
            eredmeny.append(i)
    if returnable:
        return eredmeny
    namilegyen(eredmeny)

def namilegyen(szurt):
    match input("fileba(1) vagy kiiratva(2) szeretnéd megtekinteni? "):
        case '2':
            show(szurt)
        case '1':
            path = input("mi legyen a file neve (*.json)")
            FileHandler.save_any(path + ".json", szurt)

def munkasraszuro():
    global dolgozok
    global gepjarmuvek
    global ertekesitesek
    szurt = []
    emp = get(_from=dolgozok,selected=select(_from = dolgozok,tipe=MyType.EMP))
    for i in ertekesitesek:
        if i["dolgozo"] == emp:
            i.pop("dolgozo")
            print(f"popitemutan: {i}")
            szurt.append(i)
    
    namilegyen(szurt)

def legkeresettebb_kocsi():
    jeloltek = intervallumszuro(returnable = True)
    koztes = {"gepjarmuvek":[],"db":[]}
    for d in jeloltek:
        if d["gepjarmu"] in koztes["gepjarmuvek"]:
            koztes["db"][list.index(d["gepjarmu"])] +=1
        else:
            koztes["gepjarmuvek"].append(d["gepjarmu"])
            koztes["db"].append(1)
    nyertes={}
    max = 0
    for k,i in enumerate(koztes["db"]):
        if i>max:
            nyertes=koztes["gepjarmuvek"][k]
    namilegyen([nyertes])


def legsikeresebb_munkas():
    jeloltek = intervallumszuro(returnable = True)
    koztes = {"dolgozok":[],"db":[]}
    for d in jeloltek:
        if d["gepjarmu"] in koztes["dolgozok"]:
            koztes["db"][list.index(d["dolgozo"])] +=1
        else:
            koztes["dolgozok"].append(d["dolgozo"])
            koztes["db"].append(1)
    nyertes={}
    max = 0
    for k,i in enumerate(koztes["db"]):
        if i>max:
            nyertes=koztes["dolgozok"][k]
    namilegyen([nyertes])

def idoszaknyereseg():
    jeloltek = intervallumszuro(returnable = True)
    nyereseg =0
    for i in jeloltek:
        nyereseg = nyereseg + i['tenyleges_eladasi_ar'] - i['gepjarmu']['onkoltsegi_ar']

    namilegyen([{"nyereseg":nyereseg}])

def main():
    loader()

    while True:
        x=menü.main_menu()
        if x == 1:
            munkatars_kezelo()
        elif x==2:
            gepjarmu_kezelo()
        elif x==3:
            ertekesites_kezelo()
        elif x==4:
            datumszuro()
        elif x==5:
            intervallumszuro()
        elif x==6:
            munkasraszuro()
        elif x==7:
            legkeresettebb_kocsi()
        elif x==8:
            legsikeresebb_munkas()
        elif x==9:
            idoszaknyereseg()
        elif x==10:
            sys.exit()






if __name__ == "__main__":
    main()