from book import Book
from recipe import Recipe


b1 = Book("MyCookbook")
print(b1.name, " | Creation : ", b1.creation_date, " | Last update : ", b1.last_update)
print("")

r1 = Recipe("Salted water", 2, 12, ["Salt", "Water"], "Perfect for weight loss", "starter")
r2 = Recipe("Cake", 2, 12, ["Floor", "Sugar", "Chocolate"], "A delicious chocolate cake", "dessert")
r3 = Recipe("Tuna salad", 2, 12, ["Salad", "Tuna", "Olive oil"], "Perfect for weight loss", "starter")
b1.add_recipe(r1)
b1.add_recipe(r2)
b1.add_recipe(r3)

b1.get_recipe_by_name("Cake")
b1.get_recipe_by_name("salad")
b1.get_recipe_by_types("starter")