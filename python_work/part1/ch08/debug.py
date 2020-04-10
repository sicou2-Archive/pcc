def make_car(manuf, model, **info):
    """making a car without knowing the number of info"""
    infos = {}
    infos['marque'] = manuf
    infos['model'] = model
    for key, value in info.items():
        infos[key] = value
    print("\nHere are the specifications of your car: ")
    return infos


car = make_car('porshe', 911, color='blue', motor='V12')
print(car)




