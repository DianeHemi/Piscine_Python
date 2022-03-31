class Recipe:
    
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "------\n"
        txt += "{name} - Level {lvl}\nIt's a {type} who takes {time}mn to cook\n".format(name=self.name,
                                                                                         type=self.recipe_type,
                                                                                         lvl=self.cooking_lvl,
                                                                                         time=self.cooking_time)
        txt += "Ingredients: {ingredients}\n{desc}\n".format(ingredients=self.ingredients, desc=self.description)
        return txt
