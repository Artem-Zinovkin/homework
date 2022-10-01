def choice():
    a = input("введите сторону в см а = ")
    b = input("введите сторону в см b = ")
    c = input("введите сторону в см c = ")
    d = input("введите сторону в см d = ")
    return a, b, c, d


def acreage(a, b):
    return a * b


def checking_rectangle(a, b, c):
    diag1 = (a ** 2 + b ** 2) ** 0.5
    diag2 = (c ** 2 + b ** 2) ** 0.5
    if diag1 == diag2:
        print("площадь прямоугольника = ", acreage(a, b), "кв. см.")
    else:
        print("у вас не прямоугольник")


def square(a, b, c, d):
    if a == b == c == d:
        print("у вас квадрат")


if __name__ == '__main__':
    a, b, c, d = choice()
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)

        checking_rectangle(a, b, c)
        square(a, b, c, d)

    except:
        print("стороны должны быть цифрой")
