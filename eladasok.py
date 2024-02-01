from munkatars import Munkatars
from gepjarmu import Gepjarmu


class Ertekesites():
    def __init__(self,munkatars:Munkatars,gepjarmu:Gepjarmu,
                 eladas_datuma, tenyleges_eladasi_ar):
        self.munkatars = munkatars
        self.gepjarmu = gepjarmu
        self.eladas_datuma = eladas_datuma
        self.tenyleges_eladasi_ar = tenyleges_eladasi_ar


    def __str__(self):
        return f"{self.munkatars}\t{self.gepjarmu}\t{self.eladas_datuma}\t{self.tenyleges_eladasi_ar}"