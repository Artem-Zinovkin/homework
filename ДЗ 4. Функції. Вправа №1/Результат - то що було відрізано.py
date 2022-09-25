# Відрізання останніх цифр від числа, результат - то що було відрізано

def choice():
    a = int(input("введите целое число "))
    b = int(input("на сколько цифр отрезать число? "))
    return a, b


def namber(a, b):
    d = "0"
    if b != 0:
        c = int("1" + d * b)
        return (a % c)
    else:
        pass


a, b = choice()
print(namber(a, b))
