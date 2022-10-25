class Triangle:
    def __init__(self, name: str, side_a: float, side_b: float, side_c: float):
        self.name = name
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def exists(self) -> bool:
        """
        Перевіряє чи може існувати трикутник в Евклідовому просторі
        :return: Якщо може повертає True, якщо не може існувати повідомляє про це користувача та повертає False
        """
        if self.side_a + self.side_b > self.side_c and self.side_a + self.side_c > self.side_b \
                and self.side_c + self.side_b > self.side_a:
            return True
        else:
            print(f"Tрикутник {self.name} не для Евклідового простору")
            return False

    def perimeter(self) -> float:
        """
        Рахує периметр трикутника
        :return: повертає вирахований периметр
        """
        return self.side_a + self.side_b + self.side_c

    def area(self) -> float:
        """
        Рахує площу трикутника
        :return: повертає вираховану площу
        """
        a = (self.perimeter()) / 2
        return (a * (a - self.side_a) * (a - self.side_b) * (a - self.side_c)) ** 0.5

    def abc(self):
        """
        перевіряє якщо трикутник існує, вираховує його периметр та площу та виводить дані на екран
        :return: нічого
        """
        if self.exists():
            perimetr = self.perimeter()
            area = self.area()
            print(f'Периметр трикутника {self.name}  = {perimetr}, площа = {round(area, 4)}')


if __name__ == '__main__':
    triangle = Triangle('A', 3, 4, 5)
    triangle.abc()

    triangle = Triangle('B', 7, 8, 9)
    triangle.abc()

    triangle = Triangle('C', 2, 12, 9)
    triangle.abc()

    triangle = Triangle('D', 8, 15, 9)
    triangle.abc()
