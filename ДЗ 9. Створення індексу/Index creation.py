import json
from uuid import uuid4



def display_people_data(d: dict) -> str:
    """
    Читабельно и репрезентативно формирует строку для вывода полных данных об одном человеке
    :param d: полные данные об одном человеке
    :return: возвращает сформированную строку о человеке
    """
    return f'  {d["first name"]}  {d["last name"]}  {d["gender"]} category #{d["category"]} rating {d["rating"]}'


def view_index(index_name: str, index_to_view: dict, source_uid_data: dict):
    """
    Функция выводит на экран в читaбельном репрезентативном виде
    студентов, разделенных по признаку index_name (в index_to_view)
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


if __name__ == '__main__':

    data = json.load(open('database.json', mode='r'))
    # индекс всех людей, каждому человеку будет присвоен уникальный айди
    index_uid = dict()
    # создаем индексы по категориям, рейтингу и полу
    index_category = dict()
    index_rating = dict()
    index_gender = dict()
    # проходясь циклом по каждому значению списка словарей присваиваем каждому человеку уникальный айди
    for people_data in data["people"]:
        people_data["uid"] = str(uuid4())
        index_uid[people_data["uid"]] = people_data
        # формируем индексы
        # для каждого индекса делаем проверку если необходимый индекс уже есть в словаре
        # добавляем айди человека в список значений
        if people_data["category"] in index_category:
            index_category[people_data["category"]].append(people_data["uid"])
        # если индекса нет создаем пустой список под значения айди
        else:
            index_category[people_data["category"]] = list()
            index_category[people_data["category"]].append(people_data["uid"])
        # также для других индексов
        if people_data["rating"] in index_rating:
            index_rating[people_data["rating"]].append(people_data["uid"])
        else:
            index_rating[people_data["rating"]] = list()
            index_rating[people_data["rating"]].append(people_data["uid"])
        if people_data["gender"] in index_gender:
            index_gender[people_data["gender"]].append(people_data["uid"])
        else:
            index_gender[people_data["gender"]] = list()
            index_gender[people_data["gender"]].append(people_data["uid"])



    view_index("gender", index_gender, index_uid)
    print("_" * 60)
    view_index("rating", index_rating, index_uid)
    print("_" * 60)
    view_index("category", index_category, index_uid)
