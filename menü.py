import datetime
import any_handler


def munkatars_menu(dolgozok):
    print("\n\nmunkatárs kezelő")
    #munkatársak kilistázása:
    any_handler.show(dolgozok)
    #menüpontok
    print("1 munkatárs hozzáadása")
    print("2 munkatárs törlése")
    print("3 vissza a főmenübe")
    return menupontvalasztó(3)

def gepjarmu_menu(jarmuvek):
    print("\n\nGépjármű kezelő")
    # Gépjárművek kilistázása:
    any_handler.show(jarmuvek)
    # menüpontok
    print("1 Gépjármű hozzáadása")
    print("2 Gépjármű törlése")
    print("3 vissza a főmenübe")
    return menupontvalasztó(3)

def ertekesites_menu(ertekesites):
    print("\n\nÉrtékesítés kezelő")
    #munkatársak kilistázása:
    any_handler.show(ertekesites)
    #menüpontok
    print("1 Értékesítés hozzáadása")
    print("2 Értékesítés törlése")
    print("3 vissza a főmenübe")
    return menupontvalasztó(3)

def main_menu():
    print("\n\nFő kezelő \n")
    print("1 teljeskörű információk a cég alkalmazottairól")
    print("2 teljeskörű információ a gépjárművekről")
    print("3 teljeskörű információ a értékesítésekröl")
    print("4 egy bizonyos dátum össszes értékesítése")
    print("5 összes értékesítés egy bizonyos időszakban")
    print("6 egy bizonyos alkalmazott összes értékesítése")
    print("7 a legkeresettebb autó neve egy bizonyos időszakban")
    print("8 információ a legsikeresebb kereskedőről az adott időszakban")
    print("9 teljes nyereség az adott időszakban")
    print("10 kilépés")
    return menupontvalasztó(10)

def menupontvalasztó(max=1):
    try:
        selected = int(input(f"kérlek válassz egy menüpontot 1-töl {max}-ig: "))
        if 0 > selected > max:
            raise Exception()
    except Exception:
        print("ilyen menüpont nincs kérlek figyelj oda jobban!")
        selected = menupontvalasztó(max)
    return selected

def intervall():
    print("időintervallum megadása:")
    start = idopontbekero("intervallum kezdeti")
    stop= idopontbekero("intervallum végi")
    return {"start":start,"stop":stop}

def idopontbekero(s=""):
    try:
        datum = input(f"kérlek add meg a(z ){s} dátumot (yyyy-mm-dd): ")
        datum = datum.strip().split(sep="-")
        if len(datum[0])<4:
            raise ValueError("végig írd ki az évet")
        datum = datetime.date(year=int(datum[0]),
                              month=int(datum[1]),
                              day=int(datum[2]))
    except Exception as e:
        print(e)
        print("kérlek figyelj a formátumra.")
        datum = idopontbekero(s)
    return datum


