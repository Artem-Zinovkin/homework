import json
from Washingmachines import WashingMachines
from TV import TV
from Refrigerators import Refrigerators
import User_input as Df

if __name__ == '__main__':
    f = json.load(open('Merchandise.json', mode='r'))
    while True:
        # Какие фильтры не нужно предлагать
        do_not_offer = ["Name", "Guarantee"]
        choice_category = Df.view_category(f)
        a = list()
        if choice_category == "TV":
            for i in f[choice_category]:
                obj = TV(brand=i["Brand"], name=i["Name"], price=i["Price"], year_of_admission=i["Year of admission"],
                         guarantee=i["Guarantee"],
                         quantity=i["Quantity"], diagonal=i["Diagonal, inches"], smart_tv=i["Smart_tv"])
                a.append(obj)
        elif choice_category == "WashingMachines":
            for i in f[choice_category]:
                obj = WashingMachines(brand=i["Brand"], name=i["Name"], price=i["Price"],
                                      year_of_admission=i["Year of admission"],
                                      guarantee=i["Guarantee"],
                                      quantity=i["Quantity"], spin_speed=i["Spin speed"], load_type=i["Load type"])
                a.append(obj)
        elif choice_category == "Refrigerators":
            for i in f[choice_category]:
                obj = Refrigerators(brand=i["Brand"], name=i["Name"], price=i["Price"],
                                    year_of_admission=i["Year of admission"],
                                    guarantee=i["Guarantee"],
                                    quantity=i["Quantity"], height=i["Height cm"], no_frost=i["No frost"])
                a.append(obj)
        category = a[0].category
        Df.for_i_in_a(a)
        while True:
            filter_or_reset = Df.filter_or_reset(a)
            if filter_or_reset == "1":
                filters_1 = Df.filters(f, choice_category, do_not_offer)
                w = Df.filter_selection(filters_1, a, category)
                do_not_offer.append(filters_1.capitalize())
                if category == "TV":
                    a = Df.filter_last_tv(a, w)
                elif category == "Refrigerators":
                    a = Df.filter_last_refrigerators(a, w)
                elif category == "WashingMachines":
                    a = Df.filter_last_washingmachines(a, w)
                Df.for_i_in_a(a)
            elif filter_or_reset == "2":
                break
