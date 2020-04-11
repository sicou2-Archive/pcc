def make_pizza(size, *toppings):
    '''
    # Print the list of toppings that have been requested.
    Summarize the pizza we are about to make.
    '''
    #print(toppings)

    print(f'\nMaking a {size}" pizza with the following toppings: ')
    for topping in toppings:
        print(f"- {topping}")

make_pizza(12, 'pepperoni')
make_pizza(18, 'olives', 'tuna', 'garlic')