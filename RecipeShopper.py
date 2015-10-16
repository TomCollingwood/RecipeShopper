class ingredient:
	def __init__(self, name, amount, gram):
	 self.name = name
	 self.amount = amount
	 self.gram = gram
	 
class recipe:
	def __init__(self, title, recipe, ingredients):
		self.title = title
		self.recipe = recipe
		if type(ingredients) is list and all(isinstance(x, ingredient) for x in ingredients):
			self.ingredients = ingredients
		else:
			raise ValueError
		
beef = ingredient("beef", 200, True)
beefstrog = recipe("beef strog", "put beef in stew", [beef])

# print beefstrog.recipe
# print beefstrog.ingredients[0].name

def writerecipe(filename, recipe1):
	if type(recipe1) is recipe == False:
		print("That, sir, is not a recipe!")
		return

	fh = open(filename, "w+")
 
	fh.write(recipe1.title+", "+recipe1.recipe+", ")
	for index in range(len(recipe1.ingredients)):
		fh.write(recipe1.ingredients[index].name+ " : "+str(recipe1.ingredients[index].amount)+" : "+str(recipe1.ingredients[index].gram) + " | ")
	fh.write("\n")
	fh.close()
	
def writerecipes(filename, recipes):
	if type(recipes) is list == False:
		print "I need a LIST of recipes"
		return
	for rec in range(len(recipes)):
		writerecipe(filename, recipes)
		
writerecipe("recipes.txt",beefstrog)

# def importrecipes(filename):
# do stuff here to import recipes using structure used for writing
