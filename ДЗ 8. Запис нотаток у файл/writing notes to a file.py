import os
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
    save - зберегти нотатки у файл
    load - завантаження збережених нотатків
    clear - видалити всі збережені нотатки та видалити файл зберігання нотаток
    exit - якщо бажаєте вийти
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
        # не запрашивать количество заметок если их 0
        if len(note_journal) == 0:
            break
        else:
            how = input('скільки нотатків ви бажаєте вивести на екран?  ')
        # проверка  что введено целое число

        try:
            how = int(how)
            if how >= 0:
                return how
            else:
                print("введіть не від'ємне значення!")
        except:
            print("Необхідно ввести ціле число!")

def save_del() -> str:
    """
    запрашивает у пользователя хочет ли он сохранить не сохраненые заметки
    :return: результат выбора пользователя
    """
    s = input(''' 
    якщо у вас є не збережені нотатки вони будуть видалені
             proceed - продовжити без збереження
             save - зберегти
            ''')
    return s

def w_or_a()-> str:
    """
    считывает ввод пользователя как он хочет сохранить заметки
    :return: результат выбора пользователя
    """
    while True:
        q = input(''' 
            a - додати до існуючих нотатків  
            W - перезаписати нотатки
                    ''')
        if q.lower() == "a" or q.lower() == "w":
            return q
        else:
            print("Введіть запропановане значення")
            continue

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
    try:
        for i in note_journal[:-how - 1:-1]:
            print(i)
    except:
        pass

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

def func_save(note_jornal_new: list, mode:str)-> list:
    """
   сохраняет журнал с заметками в служебный файл
    :param note_jornal_new: журнал, с введенным количеством заметок
    :param mode: режим в котором производиться запись в файл
    :return: очищеный журнал заметок
    """
    for i in note_jornal_new:
        i = "\n" + i
        with open ('test_file.txt', mode = mode) as fp:
            fp.writelines(i)
    note_journal = []
    return note_journal


def func_load(new_file) -> list:
    """
    выгружает из служебного файла заметки
    :param new_file: служебный файл
    :return: возвращает список с удаленными \n и игнорирует пустые строки
    """
    with open(new_file, mode = 'r') as fp:
        a = []
        file = fp.readlines()
        for i in file:
            if i.isspace():
                pass
            elif len(i) == 0:
                pass
            else:
                a.append(i.replace("\n", ""))
        return a

def func_clear(file):
    """
    удаляет все сохраненные заметки вместе со служебным файлом
    :param file: служебный файл
    :return: ничего не возвращает
    """
    os.remove(file)

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
        elif d.lower() == "save":
            q = w_or_a()
            s = func_save(note_journal, q)
            note_journal = s
        elif d.lower() == "load":
            while True:
                s = save_del()
                if s.lower() == "proceed":
                    try:
                        note_journal = func_load('test_file.txt')
                        break
                    except:
                        print("Файл не знайдено")
                        break
                elif s.lower() == "save":
                    q = w_or_a()
                    try:
                        func_save(note_journal, q)
                        note_journal = func_load('test_file.txt')
                        break
                    except:
                        print("Файл не знайдено")
                else:
                    print ("Введіть запропановане знечення")
        elif d.lower() == "clear":
            try:
                func_clear('test_file.txt')
            except:
                print("Файл не знайдено")
        elif d.lower() == "exit":
            print("До побачення")
            break

        else:
            print('Введіть запропоноване значення')

