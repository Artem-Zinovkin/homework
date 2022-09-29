def input_namber():
    namber = input("Введите число или sum: ")
    return namber


a = []

if __name__ == '__main__':
    while True:
        namber = input_namber()
        if namber == "sum":
            print(sum(a))
            break
        try:
            namber = float(namber)
            a.append(namber)
        except:
            print("Вы ввели не число, а нужно число!!!!")
