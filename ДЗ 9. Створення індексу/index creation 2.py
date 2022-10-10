import json
from uuid import uuid4

def choice() -> str:
    """
    запрашивает у пользователя по какому индексу он бы хотел сортировать
    :return: результат ввода пользователя
    """
    d = (input('''
выберите по какому индексу вы хотите сортировать
    "first name"  -  введите - first name
    "last name"   -  введите - last name
    "gender"      -  введите - gender
    "category"    -  введите - category
    "rating"      -  введите - rating
    "EXIT"        -  введите - exit    
     '''))
    return d

def continue_or_not()->str:
    """
    запрашивает у пользователя желает ли он продолжить
    :return: результат ввода пользователя
    """
    while True:
        s = (input('''
        Вы желаете продолжить?
         ДА введите -  yes
         НЕТ введите -  no 
             '''))
        if s.lower() == "yes":
            return "yes"
        elif s.lower() == "no":
            return "no"
        else:
            print(" введите предложенное значение! ")
            continue

def display_people_data(d: dict) -> str:
    """
    Читабельно и репрезентативно формирует строку для вывода полных данных об одном человеке
    :param d: полные данные об одном человеке
    :return: возвращает сформированную строку о человеке
    """
    return f'  {d["first name"]}  {d["last name"]}  {d["gender"]} category #{d["category"]} rating {d["rating"]}'


def view_index(index_name: str, index_to_view: dict, source_uid_data: dict):
    """
    Функция выводит на экран в читабельном репрезентативном виде
    людей, разделенных по признаку index_name (в index_to_view)
    :param index_name: название нашего индекса для вывода
    :param index_to_view: сам индекс, словарь списком.
        Ключи словаря - уникальные значения в индексе
        значения словаря - списки уникальных айди людей (ссылки на полные данные)
    :param source_uid_data: полные данные людей промаркированные своим уникальным айди
    :return: ничего
    """
    print(f' \n PEOPLE BY {index_name.upper()}')
    for key, values in index_to_view.items():
        print(f'\nDisplaying people of {index_name} - {key}:\n')
        for uid in values:
            print(f'    {display_people_data(source_uid_data[uid])}')


def index (d:str):
    """
присваивает уникальный айди каждому человеку.
создает индекс категории
формирует и выводит на экран информацию сортированную по индексам
    :param d: индекс по которому необходимо отсортировать, вводится пользователем
    :return: ничего
    """
    index_uid = dict()
    index = dict()
    for people_data in data["people"]:
        people_data["uid"] = str(uuid4())
        index_uid[people_data["uid"]] = people_data
        # для каждого индекса делаем проверку если необходимый индекс уже есть в словаре
        # добавляем айди человека в список значений
        if people_data[d] in index:
            index[people_data[d]].append(people_data["uid"])
        # если индекса нет создаем пустой список под значения айди
        else:
            index[people_data[d]] = list()
            index[people_data[d]].append(people_data["uid"])
    view_index(d, index, index_uid)


if __name__ == '__main__':

    data = json.load(open('database.json', mode='r'))
    while True:
        d = choice()
        if d.lower() == "exit":
            print("всего хорошего!")
            break
        try:
            index(d.lower())
        except:
            print(" введите предложенное значение! ")
            continue
        s = continue_or_not()
        if s == "yes":
            continue
        elif s == "no":
            print("всего хорошего!")
            break

