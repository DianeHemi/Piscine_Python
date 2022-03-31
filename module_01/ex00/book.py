from datetime import datetime
from recipe import Recipe


class Book:
	
	def __init__(self, name):
		self.name = name
		self.last_update = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		self.creation_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		self.recipes_list = {"starter":[], "lunch":[], "dessert": []}

	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name \texttt{name} and returns the instance"""
		found = False
		for element in self.recipes_list:
			for recipe in self.recipes_list[element]:
				if recipe.name is name:
					found = True
					print(str(recipe))
		if found is False:
			print("Recipe {name} not found".format(name=name))	

	def get_recipe_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe type"""
		assert recipe_type in self.recipes_list, "Invalid recipe type"
		for element in self.recipes_list[recipe_type]:
			print(element.name)

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		try:
			isinstance(recipe, Recipe)
		except ValueError:
			print("Error : Not a recipe instance")
		self.recipes_list[recipe.recipe_type].append(recipe)
		self.last_update = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
