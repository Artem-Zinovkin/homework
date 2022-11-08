from Merchandise import Merchandise


class Refrigerators(Merchandise):
    def __init__(self, brand: str, name: str, price: str, year_of_admission: str,
                 guarantee: str, quantity: str, height: str, no_frost: str):
        super().__init__(category="Refrigerators", brand=brand, name=name, price=price,
                         year_of_admission=int(year_of_admission),
                         guarantee=guarantee, quantity=quantity)
        self.height = int(height)
        self.no_frost = no_frost

    def __str__(self):
        s = super(Refrigerators, self).__str__()
        s += f'Height cm - {self.height},\nNo Frost (Frost Free) -  {self.no_frost}\n\n'
        return s
