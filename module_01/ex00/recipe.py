class Recipe:
    
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        #TODO -> Verif des valeurs
        self.name = name
        self.cooking_lvl = cooking_lvl      #int 1 to 5
        self.cooking_time = cooking_time    #int in minutes
        self.ingredients = ingredients      #list
        self.description = description      #str, can be empty
        self.recipe_type = recipe_type      #str -> starter, lunch or dessert


#implement __str__
    # tourte = Recipe(...)
    # to_print = str(tourte)
    # print(to_print)
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "------\n"
        txt += "{name} - Level {lvl}\nIt's a {type} who takes {time}mn to cook\n".format(name=self.name, type=self.recipe_type, lvl=self.cooking_lvl, time=self.cooking_time)
        txt += "Ingredients: {ingredients}\n{desc}\n".format(ingredients=self.ingredients, desc=self.description)
        return txt