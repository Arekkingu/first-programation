allergies = {
    "gluten" : ("bread", "brownie"),
    "crustacean" : ("crab"),
    "fish" : ("Tilapia")
}
Menu = [
    ("bread", 1),
    ("brownie", 3),
    ("crab", 6),
    ("Tilapia", 1),
]
allergy = str(input('What are allergic to? :')).strip().lower()
def eliminate_allergies(allergies, Menu, allergy):
    allergy_list = allergy.split()
    for allergies_index in allergy_list:
        plate_list = allergies[allergies_index]
        if type(plate_list) is not str:
            for plates in plate_list:
                for menu_plates in Menu:
                    if plates in menu_plates:
                        Menu.remove(menu_plates)
        else:
            for menu_plates in Menu:
                    if plate_list in menu_plates:
                        Menu.remove(menu_plates)
    return Menu
for plate_name, price in eliminate_allergies(allergies, Menu, allergy):
    print(f"{plate_name} - {price:.2f}€")