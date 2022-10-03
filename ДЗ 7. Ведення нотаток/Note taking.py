note_journal = []  # журнал заметок в него дополняются все заметки


def choice() -> str:
    """
    выводит на экран варианты ввода для работы с журналом
    :return: возвращает переменную d в которой храниться текст помогаюший сделать выбор
    """
    d = (input('''
    add -  додати нотатку 
    earliest - виводить збережені нотатки у хронологічному порядку  - від найранішої до найпізнішої
    latest - виводить збережені нотатки у хронологічному порядку - від найпізнішої до найранішої
    longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
    shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшої до найдовшої 
    end - якщо бажаєте вийти
    \n'''))
    return d


def choice_how(note_journal: list) -> int:
    """
    выводим на экран количество заметок,
    после чего считывает ввод пользователя сколько заметок он хочет вывести на экран
    :param note_journal: журнал, с веденным количеством заметок
    :return: возвращает введеное пользователем целое число, если отрицательное делает его положительным
    """
    while True:
        print(f"у вас {len(note_journal)} нотатків")
        how = input('скільки нотатків ви бажаєте вивести на екран?  ')
        # проверка  что введено целое число
        try:
            how = int(how)

            return abs(how)
        except:
            print("Необхідно ввести ціле число!")


def func_add(note_journal: list) -> list:
    """
    считывает введеную пользователем заметку, если она не пустая добавляет ее в журнал заметок
    :param note_journal: журнал, с введенным количеством заметок
    :return: возвращает журнал с добавленой заметкой
    """
    note = input("введіть нотатку ")
    # проверка на то что заметка не пустая
    if note.isspace():
        pass
    elif len(note) == 0:
        pass
    else:
        note_journal.append(note)
    return note_journal


def func_earliest(note_journal: list, how: int):
    """
    выводит на экран заметки от самой ранней до самой поздней
    :param note_journal: журнал, с введенным количеством заметок
    :param how: количество заметок которое необходимо вывести на экран (введеное пользователем)
    :return: ничего не возвращает
    """
    for i in note_journal[:how]:
        print(i)


def func_latest(note_journal: list, how: int):
    """
    выводит на экран заметки от самой поздней до самой ранней
    :param note_journal: журнал, с введенным количеством заметок
    :param how: количество заметок которое необходимо вывести на экран (введеное пользователем)
    :return: ничего не возвращает
    """
    for i in note_journal[:-how - 1:-1]:
        print(i)


def func_longest(note_journal: list, how: int):
    """
    выводит на экран заметки в порядке их длины от самой длинной до самой короткой
    сначала сортирует потом выводит необходимое количество
    :param note_journal: журнал, с введенным количеством заметок
    :param how: журнал, с веденным количеством заметок
    :return: ничего не возвращает
    """
    a = sorted(note_journal, reverse=True, key=len)
    for i in a[:how]:
        print(i)


def func_shortest(note_journal: list, how: int):
    """
    выводит на экран заметки в порядке их длины от самой короткой до самой длинной
    сначала сортирует потом выводит необходимое количество
    :param note_journal: журнал, с введенным количеством заметок
    :param how: журнал, с введенным количеством заметок
    :return: ничего не возвращает
    """
    a = sorted(note_journal, key=len)
    for i in a[:how]:
        print(i)


if __name__ == '__main__':
    while True:
        d = choice()
        if d.lower() == "add":
            func_add(note_journal)
        elif d.lower() == "earliest":
            how = choice_how(note_journal)
            func_earliest(note_journal, how)
        elif d.lower() == "latest":
            how = choice_how(note_journal)
            func_latest(note_journal, how)
        elif d.lower() == "longest":
            how = choice_how(note_journal)
            func_longest(note_journal, how)
        elif d.lower() == "shortest":
            how = choice_how(note_journal)
            func_shortest(note_journal, how)
        elif d.lower() == "end":
            print("До побачення")
            break
        else:
            print('Введіть запропоноване значення')


