def view_category(file: dict):
    """
    Выводит на экран категории товаров.
    :param file: файл с товаром.
    :return: значение категории
    """
    while True:
        print("Internet-shop Tech-stop welcomes you!\nCategories to search in:")
        n = 1
        for i in file:
            print(f"Category {i} click {n}")
            n += 1
        choice = input()
        if choice == '1':
            return "TV"
        elif choice == '2':
            return "Refrigerators"
        elif choice == '3':
            return "WashingMachines"
        else:
            print("Enter the suggested value!\n")


def for_i_in_a(a_1: list):
    """
    Читабельно выводит товары на экран.
    :param a_1: Список объектов класса

    """
    for i in a_1:
        print(i)


def filter_or_reset(len_a: list) -> str:
    """
    Спрашивает у пользователя хочет он фильтровать или выйти.
    :param len_a: Список объектов класса (в данной функции необходим только для определения длины списка)
    :return: значение выбранное пользователем
    """
    while True:
        c = input(f"Found  {len(len_a)}, Would you like to filter or reset?\n"
                  "filter click 1"
                  " reset click 2\n")
        if c == "1" or c == "2":
            return c
        else:
            print("\nEnter the suggested value!!!\n")
            continue


def filters(file: dict, ch: str, dno: list) -> str:
    """
    Выводит на экран по каким полям можно отфильтровать выбранную категорию.
    :param file: json файл в котором содержится информация о товарах.
    :param ch: категория товаров выбранная пользователем.
    :param dno: список полей которые не нужно выводить на экран.
    :return:
    """
    while True:
        fl = []
        print(f'\nCategory  {ch}, you can filter by:\n')
        for g in file[ch][0]:
            if g not in dno:
                print(g.upper())
                fl.append(g)
        chh = input('Choose one:\n')
        for i in fl:
            if chh.capitalize() in i:
                return chh.capitalize()
        else:
            print("\nEnter the suggested value!!!\n")
            continue


def filter_selection(chh_1: str, a_1: list, category_1: str) -> str:
    """
    Выводит на экран какие значения полей, если выбрана цена то какие суммы есть, если бренд какие бренды.
    :param chh_1: поле категории выбранное пользователем.
    :param a_1: Список объектов класса.
    :param category_1: выбранная пользователем категория.
    :return: значения выбранного поля
    """

    print(f'Category  {category_1}, filter {chh_1} you can choose:')
    a = set()
    while True:
        if "Brand" == chh_1:
            for i in a_1:
                a.add(i.brand)
        elif chh_1 == "Diagonal, inches":
            for i in a_1:
                a.add(i.diagonal)
        elif chh_1 == "Smart_tv":
            for i in a_1:
                a.add(i.smart_tv)
        elif chh_1 == "Price":
            for i in a_1:
                a.add(i.price)
        elif chh_1 == "Year of admission":
            for i in a_1:
                a.add(i.year_of_admission)
        elif chh_1 == "Quantity":
            for i in a_1:
                a.add(i.quantity)
        elif chh_1 == "Height cm":
            for i in a_1:
                a.add(i.height)
        elif chh_1 == "No frost":
            for i in a_1:
                a.add(i.no_frost)
        elif chh_1 == "Load type":
            for i in a_1:
                a.add(i.load_type)
        elif chh_1 == "Spin speed":
            for i in a_1:
                a.add(i.spin_speed)
        for_i_in_a(list(a))
        inp = input('Choose one:\n')
        if inp.upper() in str(a):
            return inp.upper()
        else:
            print("\nEnter the suggested value!!!\n")
            continue


def filter_last_tv(a_1: list, inp: str) -> list:
    """
    Если категория TV
    возвращает список объектов класса отфильтрованных по всем заданным пользователем
     в одном цикле полям и их значениям.
    :param a_1: список объектов класса.
    :param inp: значение выбранного поля.
    :return: список объектов класса
    """
    a = []
    for i in a_1:
        if i.brand == inp:
            a.append(i)
        elif str(i.price) == inp:
            a.append(i)
        elif str(i.year_of_admission) == inp:
            a.append(i)
        elif i.quantity == inp:
            a.append(i)
        elif i.smart_tv == inp:
            a.append(i)
        elif str(i.diagonal) == inp:
            a.append(i)
    return a


def filter_last_refrigerators(a_1, inp):
    """
        Если категория Refrigerators
        возвращает список объектов класса отфильтрованных по всем заданным пользователем
         в одном цикле полям и их значениям.
        :param a_1: список объектов класса.
        :param inp: значение выбранного поля.
        :return: список объектов класса
        """
    a = []
    for i in a_1:
        if i.brand == inp:
            a.append(i)
        elif str(i.price) == inp:
            a.append(i)
        elif str(i.year_of_admission) == inp:
            a.append(i)
        elif i.quantity == inp:
            a.append(i)
        elif i.no_frost == inp:
            a.append(i)
        elif str(i.height) == inp:
            a.append(i)
    return a


def filter_last_washingmachines(a_1, inp):
    """
           Если категория WashingMachines
           возвращает список объектов класса отфильтрованных по всем заданным пользователем
            в одном цикле полям и их значениям.
           :param a_1: список объектов класса.
           :param inp: значение выбранного поля.
           :return: список объектов класса
           """
    a = []
    for i in a_1:
        if i.brand == inp:
            a.append(i)
        elif str(i.price) == inp:
            a.append(i)
        elif str(i.year_of_admission) == inp:
            a.append(i)
        elif i.quantity == inp:
            a.append(i)
        elif i.load_type == inp:
            a.append(i)
        elif str(i.spin_speed) == inp:
            a.append(i)
    return a
