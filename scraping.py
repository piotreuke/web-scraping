class Kwadrat:

    def __init__(self, bok):
        self.bok = bok
        self.kolor = None
    
    def __str__(self):
        return f'Kwadrat o boku {self.bok}'

    def __repr__(self):
        return f'Kwadrat o boku {self.bok}'
            
    def pokaz_bok(self):
        print(self.bok)

    def policz_pole(self):
        return self.bok * self.bok

    def ustaw_bok(self, nowy_bok):
        self.bok = nowy_bok

    def nowy_atrybut(self, kolor):
        self.kolor = kolor


k = Kwadrat(bok=6.0)
k.ustaw_bok(2.0)
k.pokaz_bok()
k.nowy_atrybut(kolor="red")
print(k.kolor)

l = Kwadrat(bok=4.0)

lista = [k, l]
print(lista)





