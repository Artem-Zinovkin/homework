from Merchandise import Merchandise


class WashingMachines(Merchandise):
    def __init__(self, brand: str, name: str, price: str, year_of_admission: int,
                 guarantee: str, quantity: str, spin_speed: str, load_type: str):
        super().__init__("WashingMachines", brand, name, price, year_of_admission,
                         guarantee, quantity)
        self.spin_speed = int(spin_speed)
        self.load_type = load_type

    def __str__(self):
        s = super(WashingMachines, self).__str__()
        s += f'Spin speed - {self.spin_speed},\nLoad type - {self.load_type}\n\n'
        return s
