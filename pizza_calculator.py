'''

these algorithms calcutate the number of pizza needed 
to feed a group of people
#
''' 



number_of_people = input('enter the number of people: ')
slices_per_pizza = input('enter the number of slices per pizza: ')
slices_per_person = input('How many slices each person need person? ')
number_of_pizzas = int(number_of_people) * int(slices_per_person) // int(slices_per_pizza)

# Using the str() function to convert a number into a string.
print("We will need around " + str(number_of_pizzas) + " pizzas for " + str(number_of_people) + " people.")

# Using the int() function to convert a float to an integer.
cheese = int(.25 * number_of_pizzas)
vegetarian = int(.25 * number_of_pizzas)
meat = int(.5 * number_of_pizzas)

print("Get:")
print(str(cheese) + " cheese pizzas.")
print(str(vegetarian) + " vegetarian pizzas.")
print(str(meat) + " meat-lovers pizzas.")
