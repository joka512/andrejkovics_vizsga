import filehendler
import menü
import datetime
from munkatars import Munkatars
from gepjarmu import Gepjarmu
from eladasok import Ertekesites
import sys



def loader():
    try:
        Gepjarmu.loadfromfile()
    except Exception:
        pass
    try:
        Munkatars.loadfromfile()
    except Exception:
        pass
    try:
        Ertekesites.loadfromfile()
    except Exception:
        pass

def munkatars_kezelo():
    select = menü.munkatars_menu()
    if select==1:
        Munkatars.addmunkas()
    elif select == 2:
        Munkatars.delete()
    elif select==3:
        pass


def gepjarmu_kezelo():
    select = menü.gepjarmu_menu()
    if select == 1:
        Gepjarmu.addjarmu()
    elif select == 2:
        Gepjarmu.delete()
    elif select == 3:
        pass

def ertekesites_kezelo():
    select = menü.ertekesites_menu()
    if select == 1:
        Ertekesites.addnew()
    elif select == 2:
        Ertekesites.delete()
    elif select == 3:
        pass


def datumszuro():
    szurt = []
    idopont=menü.idopontbekero()
    for data in Ertekesites.eladasok:
        datum = data.eladas_datuma
        datum = datum.split(sep="-")
        datum = datetime.date(year=int(datum[0]),
                              month=int(datum[1]),
                              day=int(datum[2]))
        if idopont == datum:
            szurt.append(data)
    mode = input("fileba(1) vagy kiiratva(2) szeretnéd megtekinteni? " )
    if mode == 2:
        for x in szurt:
            print(x)
    elif mode == 1:
        path= input("mi legyen a file neve (*.txt)")
        menteni =[]
        for x in szurt:
            menteni.append(str(x))
        filehendler.save_any(path+".txt",menteni)

def intervallumszuro(generate=False):
    szurt = []
    intervall = menü.intervall()
    for data in Ertekesites.eladasok:
        datum = data.eladas_datuma
        datum = datum.split(sep="-")
        datum = datetime.date(year=int(datum[0]),
                              month=int(datum[1]),
                              day=int(datum[2]))
        if intervall["start"] < datum < intervall["stop"]:
            szurt.append(data)
    if not generate:
        namilegyen(szurt)
    else:return szurt

def namilegyen(szurt):
    mode = input("fileba(1) vagy kiiratva(2) szeretnéd megtekinteni? ")
    if mode == 2:
        for x in szurt:
            print(x)
    elif mode == 1:
        path = input("mi legyen a file neve (*.txt)")
        menteni = []
        for x in szurt:
            menteni.append(str(x))
        filehendler.save_any(path + ".txt", menteni)

def munkasraszuro():
    szurt = []
    Munkatars.showall()

    def belso():
        try:
            x = int(input(f"kérlek add meg a munkatárs sorszámát (0-{len(Munkatars.munkaslista) - 1})"))
            if 0 > x > len(Munkatars.munkaslista) - 1:
                raise ValueError
            munkas=Munkatars.munkaslista[x]
        except Exception:
            print("valmi nek ok, figyelj jobban")
            munkas=belso()
        return munkas
    munkas=belso()
    munkas=str(munkas)
    for data in Ertekesites.eladasok:
        if data[0]== munkas:
            szurt.append(data)
    namilegyen(szurt)

def legkeresettebb_kocsi():
    szurt = intervallumszuro(True)
    köztes = {}
    for x in Gepjarmu.jarmulista:
        köztes[str(x)]=0
    for data in szurt:
        köztes[data.gepjarmu] += 1
    eredmeny=""
    max =0
    for k,v in köztes.items():
        if v>max:
            max=v
            eredmeny = k
    namilegyen([eredmeny])

def legsikeresebb_munkas():
    szurt = intervallumszuro(True)
    köztes = {}
    for x in Munkatars.munkaslista:
        köztes[str(x)] = 0
    for data in szurt:
        köztes[data.munkatars] += 1
    eredmeny = ""
    max = 0
    for k, v in köztes.items():
        if v > max:
            max = v
            eredmeny = k
    namilegyen([eredmeny])

def idoszaknyereseg():
    szurt=intervallumszuro(True)
    print("a nyereség: ")
    nyereseg=0
    for data in szurt:
        költség = int(data.gepjarmu.split(sep="\t")[3])
        nyereseg = nyereseg + data.tenyleges_eladasi_ar - költség
    namilegyen([nyereseg])
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