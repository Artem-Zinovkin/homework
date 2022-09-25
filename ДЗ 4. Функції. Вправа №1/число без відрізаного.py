# Відрізання останніх цифр від числа, результат - число без відрізаного
def choice():
    a = int(input("введите целое число "))
    b = int(input("на сколько цифр отрезать число? "))
    return a, b


def namber(a, b):
    d = "0"
    c = int("1" + d * b)
    if c > a:
        pass
    else:
        return (a // c)


a, b = choice()
print(namber(a, b))
