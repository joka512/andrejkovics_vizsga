import filehendler
import menü
import datetime
from munkatars import Munkatars
from gepjarmu import Gepjarmu
from eladasok import Ertekesites
import sys



def loader():
    Gepjarmu.loadfromfile()
    Munkatars.loadfromfile()
    Ertekesites.loadfromfile()

def main():
    loader()

    while True:
        almenu={}
        x=menü.main_menu()
        if x == 1:
            almenu["ertek"] = menü.munkatars_menu()
            almenu["lepes"] = ""
        elif x==2:
            almenu["ertek"]=menü.gepjarmu_menu()
            almenu["lepes"]=""
        elif x==3:
            almenu["ertek"] = menü.ertekesites_menu()
            almenu["lepes"] = ""
        elif x==4:
            pass
        elif x==5:
            pass
        elif x==6:
            pass
        elif x==7:
            pass
        elif x==8:
            pass
        elif x==9:
            pass
        elif x==10:
            sys.exit()






if __name__ == "__main__":
    main()