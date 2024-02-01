



class Gepjarmu():
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
