def describe_pet(animal_type, pet_name):
    '''Display information about a pet.'''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

describe_pet('harry', 'hamster')

describe_pet(animal_type='cat', pet_name='Luna')
describe_pet(pet_name='lookout', animal_type='cat')


print('NEXT')


def describe_pet(pet_name, animal_type='dog'):
    '''Display information about a pet.'''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry')