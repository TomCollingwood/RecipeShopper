recipes = []

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
		
# beef = ingredient("beef", 200, True)
# beefstrog = recipe("beef strog", "put beef in stew", [beef])
# print beefstrog.recipe
# print beefstrog.ingredients[0].name

def writerecipe(filename, recipe1):
	if type(recipe1) is recipe == False:
		print("That, sir, is not a recipe!")
		return

	fh = open(filename, "a")
 
	fh.write(recipe1.title+", "+recipe1.recipe+", ")
	for index in range(len(recipe1.ingredients)):
		fh.write(recipe1.ingredients[index].name+ " : "+str(recipe1.ingredients[index].amount)+" : "+str(recipe1.ingredients[index].gram))
		if index != (len(recipe1.ingredients) - 1):
			fh.write(" | ")
	fh.write("\n")
	fh.close()
	
def writerecipes(filename, recipes):
	if type(recipes) is list == False:
		print "I need a LIST of recipes"
		return
	for rec in range(len(recipes)):
		writerecipe(filename, recipes[rec])
		
def importrecipes(filename):
	try:
		fh = open(filename, "r")
	except IOError:
		print "No such file exists"
		return
	
	num_lines = sum(1 for line in open(filename))
	
	content = fh.readlines()
	lineedit = ""	
	linelist = []
	linenumber = 0 
	for line in content:
		linenumber += 1
		line = line.split(", ")
		if len(line) != 3:
			print "Invalid format on line"+str(linenumber)
			return
		line[2] = line[2].split(" | ")
		for index in range(len(line[2])):
			line[2][index] = line[2][index].split(" : ")
			line[2][index] = ingredient(line[2][index][0], int(line[2][index][1]), bool(line[2][index][2]))
		recipes.append(recipe(line[0],line[1],line[2]))
	print "Recipes imported"
	return

def printrecipes():
	for index in range(len(recipes)):
		

beefstrogonoff = recipe("Beef Strog", "put beef in stew", [ingredient("beef",200,True), ingredient("water",400,True)])
noodles = recipe("noodles", "boil noodles and fry onions", [ingredient("noodles",300, True),ingredient("onion",2,False)])

recipes = [beefstrogonoff,noodles]

writerecipes("fatshit.txt", recipes)

recipes = []

importrecipes("fatshit.txt")

print recipes[0].title + recipes[1].title

			
		
		
	
	
	
		

#do stuff here to import recipes using structure used for writing
