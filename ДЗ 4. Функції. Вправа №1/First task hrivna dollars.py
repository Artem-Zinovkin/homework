# конвертація гривні в доллар та навпаки

while True:
    kurs = 40


    def hrivna_dollar(a):
        try:
            a = float(a)
            return round(float(a) / kurs, 2)
        except:
            print("некоректне введення")


    def dollar_hrivna(a):
        try:
            a = float(a)
            return round(kurs * float(a), 2)
        except:
            print("некоректне введення")


    def choice():
        d = (input('''
з доллара в гривню натисніть (1)   
з гривні в доллар натисніть (2) 
бажаєте  вийти натисніть (0) 
    \n зробіть свій вибір  '''))
        return d


    d = choice()
    if d == "1":
        b = dollar_hrivna(a=input("скільки у вас доларів "))
        print(f"це буде {b} гривень")
    elif d == "2":
        b = hrivna_dollar(a=input("скільки у вас гривень "))
        print(f"це буде {b} доларів")
    elif d == "0":
        print("До побачення")
        break
    else:
        print('некоректне введення, введить (1) або (2) або (0)')
