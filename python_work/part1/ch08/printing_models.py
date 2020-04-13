import printing_functions

# Start with sone designs that need to be printed. 
unprinted_designs = ['phone case', 'robot pendant', 'dodecaheron']
completed_models = []

# Simulate printing each design, until none are left. 
#  Move each design to completed_models after printing. 
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}.")
    completed_models.append(current_design)

# Display all completed models. 
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


to_be_printed_designs = ['phone case', 'robot pendant', 'dodecaheron']
completed_models = []

printing_functions.print_models(to_be_printed_designs[:], completed_models) # Not sure if I am 
                                                        #ever going to see this 
                                                    # again but, what we are 
                                                # doing here is setting the 
                                            # unprinted_designs that is 
                                        #occuring in the def of print models = 
                                    # to a slice of the unprinted_designs in 
                                # the calling of the  function of print_models;
                            # therefore it would kind of like like:
                        # unprinted_designs = to_be_printed_designs[:] as if we
                    # were creating a slice anywhere else. 
printing_functions.show_completed_models(completed_models)
print(unprinted_designs)

