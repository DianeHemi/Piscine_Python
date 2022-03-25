cookbook = {
    "sandwich": {"ingredients": ["ham", "bread", "cheese", "tomatoes"], "meal": "lunch", "prep_time": 10},
    "cake": {"ingredients": ["floor", "sugar", "eggs"], "meal": "dessert", "prep_time": 60},
    "salad": {"ingredients": ["avocado", "arugula", "tomatoes", "spinach"], "meal": "lunch", "prep_time": 15}
    }


def print_options():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe\n"
          "2: Delete a recipe\n"
          "3: Print a recipe\n"
          "4: Print the cookbook\n"
          "5: Quit")
    option = input(">> ")
    print()
    if option.isdigit():
        option = int(option)
    else:
        option = 0
    return option


def add_recipe():
    recipe = input("Enter the recipe's name :\n>> ")
    if recipe in cookbook:
        print("This recipe already exist")
        return
    elif len(recipe) < 1:
        print("Error : You have to enter a name\n")
        return
    ingredients = input("Enter the ingredients, separated by spaces:\n>> ").split(' ')
    if len(ingredients) < 1:
        print("Error : Ingredients list cannot be empty\n")
        return
    meal = input("What type of meal is it ?\n>> ")
    if len(meal) < 1:
        print("Error : Type of meal cannot be empty\n")
        return
    time = input("How long does it take to cook in minutes ?\n>> ")
    if len(time) < 1 or time.isdigit() is False:
        print("Error : Incorrect time value\n")
        return
    cookbook[recipe] = {'ingredients': ingredients, 'meal': meal, 'prep_time': time}
    print("{recipe} was added to the cookbook !\n".format(recipe=recipe))


def del_recipe():
    to_del = input("Please enter the recipe you want to delete:\n>> ")
    if to_del in cookbook:
        del cookbook[to_del]
        print("The recipe of {to_del} was deleted.\n".format(to_del=to_del))
    else:
        print("This recipe doesn't exist\n")


def print_recipe():
    recipe = input("Please enter the recipe's name to get its details:\n>> ")
    if recipe in cookbook:
        print_one_recipe(recipe)
    else:
        print("This recipe doesn't exist\n")


def print_one_recipe(recipe):
    print("Recipe for {recipe}:".format(recipe=recipe))
    print("\tIngredients list: {ingredients}".format(ingredients=cookbook[recipe]['ingredients']))
    print("\tTo be eaten for {meal}.".format(meal=cookbook[recipe]['meal']))
    print("\tTakes {time} minutes of cooking.".format(time=cookbook[recipe]['prep_time']))
    print()


def print_cookbook():
    for element in cookbook:
        print_one_recipe(element)


def main():
    while 1:
        opt = print_options()
        if opt == 1:
            add_recipe()
        elif opt == 2:
            del_recipe()
        elif opt == 3:
            print_recipe()
        elif opt == 4:
            print_cookbook()
        elif opt == 5:
            print("Cookbook closed.")
            quit()
        else:
            print("This option does not exist, please type the corresponding number.\n"
                  "To exit, enter 5.\n")


if __name__ == '__main__':
    main()

