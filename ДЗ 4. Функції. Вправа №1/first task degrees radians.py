# конвертация градусов в радианы и наоборот
import math


def degrees(a):
    try:
        a = float(a)
        return round((float(a) * math.pi) / 180, 5)
    except:
        print("некорректный ввод")



def radians(a):
    try:
        a = float(a)
        return round((float(a) * 180) / math.pi, 5)
    except:
        print("некорректный ввод")

def choice():
    d = (input('''
из градусов в радианы нажмите (1)   
из радиан в градусы нажмите (2) 
хотите выйти нажмите (0) 
\n сделайте свой выбор  '''))
    return d


while True:
    d = choice()

    if d == "1":
        b = degrees(a=input("Введите число в градусах "))
        print(F"число в радианах = {b} ")
    elif d == "2":
        с = radians(a=input("Введите число в радианах "))
        print(F"число в градусах = {с} ")
    elif d == "0":
        print("до новых встреч!")
        break
    else:
        print('некорректный ввод, введите (1) или (2) или (0)')
