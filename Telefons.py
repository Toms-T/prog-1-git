class Telefons:
    def __init__(self,tips,modelis,marka,raz_gads,cena) :
        self.modelis=modelis
        self.marka=marka
        self.raz_gads=raz_gads
        self.cena=cena
    def info(self):
        print(f"{self.modelis} {self.marka} ir ražots {self.raz_gads}. gadā. viņa aptvenā cena ir{self.cena}")

    def mainitCenu(self, jaunaCena):
        print(f"{self.modelis} {self.marka} tika mainīta cena {self.cena} ")
        self.cena = jaunaCena
        