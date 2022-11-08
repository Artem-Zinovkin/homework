from Merchandise import Merchandise


class TV(Merchandise):
    def __init__(self, brand: str, name: str, price: str, year_of_admission: int,
                 guarantee: str, quantity: str, diagonal: str, smart_tv: str):
        super().__init__(category="TV", brand=brand, name=name, price=price, year_of_admission=year_of_admission,
                         guarantee=guarantee, quantity=quantity)
        self.diagonal = int(diagonal)
        self.smart_tv = smart_tv

    def __str__(self):
        s = super(TV, self).__str__()
        s += f'Diagonal, inches - {int(self.diagonal)},\nsmart TV - {self.smart_tv}\n\n'
        return s
