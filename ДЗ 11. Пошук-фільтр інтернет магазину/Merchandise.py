class Merchandise:
    def __init__(self, category: str, name: str, brand: str, price: str, year_of_admission: int,
                 guarantee: str, quantity: str):
        self.category = category
        self.name = name
        self.brand = brand
        self.price = int(price)
        self.year_of_admission = int(year_of_admission)
        self.guarantee = int(guarantee)
        self.quantity = int(quantity)
        if self.quantity > 0:
            self.quantity = "IN STOCK"
        else:
            self.quantity = "MISSING"

    def __str__(self):
        return f"{self.category} {self.name}, \nPrice - {self.price} UAH, \nGuarantee - {self.guarantee}  mon," \
               f"\nYear of admission - {self.year_of_admission}, \nQuantity - {self.quantity},\n"
