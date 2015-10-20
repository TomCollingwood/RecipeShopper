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

def exportrecipe(filename, recipe1):
	# We can safely assume recipe1 is a recipe. As write recipe is only called by writerecipes.
	# And user can only edit recipes list with defined commands at terminal

	fh = open(filename, "a")

	fh.write(recipe1.title+", "+recipe1.recipe+", ")
	for index in range(len(recipe1.ingredients)):
		fh.write(recipe1.ingredients[index].name+ " : "+str(recipe1.ingredients[index].amount)+" : "+str(recipe1.ingredients[index].gram))
		if index != (len(recipe1.ingredients) - 1):
			fh.write(" | ")
	fh.write("\n")
	fh.close()
	
def exportrecipes(filename):
	if not recipes:
		print "Recipes list is empty."
		return
	for rec in recipes:
		exportrecipe(filename, rec)
		
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
			fh.close()
			print "Invalid format on line"+str(linenumber)
			return
		line[2] = line[2].split(" | ")
		for index in range(len(line[2])):
			line[2][index] = line[2][index].split(" : ")
			line[2][index] = ingredient(line[2][index][0], int(line[2][index][1]), bool(line[2][index][2]))
		recipes.append(recipe(line[0],line[1],line[2]))
	print "Recipes imported"
	fh.close()
	return

def printrecipes():
	for item in recipes:
		print "Name: "+item.name+"\n"
		print "Recipe: "+item.recipe+"\n"
		print "Ingredients: \n"
		for ingredient in item.ingredients:
			if(ingredient.gram):
				print ingredient.amount+"g of "+ingredient.name+"\n"
			else:
				if (ingredient.amount>1):
					print ingredient.amount+ingredient.name+"s \n"
		print "\n"
		
quit = False
correct = False
confirm = ""

while not quit:
	user_input = raw_input("What do you want to do? (type help for a list of commands)\n")
	if (user_input == "add"):

		while True: 
			input_title = raw_input("What is the name of your new recipe?\n")
			confirm = raw_input("Is "+input_title+" the name of your new recipe? (y/n)\n")
			if confirm == "y":
				break

		while True:
			input_recipe = raw_input("What is the recipe (excluding ingredients)? \n")
			confirm = raw_input("Here is your recipe: \n \n"+input_recipe+"\n \n Is this correct? (y/n)\n")
			if (confirm == "y"):
				break

		input_ingredients = []

		while True:

			# Inputting ingredient's name
			while True: 
				input_ingr_name = raw_input("What is the name of your ingredient?\n")
				confirm = raw_input("Is "+input_ingr_name+" the name of your ingredient? (y/n)\n")
				if (confirm == "y"):
					break
				
			# Inputting ingredient's amount
			while True:

				input_ingr_amount = raw_input("What is the amount of "+input_ingr_name+" ?\n")

				if input_ingr_amount.endswith("g"):
					input_ingr_gram = True
					input_ingr_amount_fixed = input_ingr_amount[:-1]
				elif input_ingr_amount.endswith("kg"):
					input_ingr_gram = True
					input_ingr_amount_fixed = input_ingr_amount[:-1] * 1000
				elif input_ingr_amount.endswith("mg"):
					input_ingr_gram = True
					input_ingr_amount_fixed = input_ingr_amount[:-1] / 1000
				else:
					input_ingr_gram = False
					input_ingr_amount_fixed = input_ingr_amount

				confirm = raw_input(input_ingr_amount+"\nIs this amount correct? (y/n)")
				while(confirm != "y" and confirm != "n"):
					confirm = raw_input(input_ingr_amount+"\nIs this amount correct?  (y/n) \n")
				if (confirm == "y"):
					break

			input_ingredients.append(ingredient(input_ingr_name, input_ingr_amount_fixed,input_ingr_gram))
			confirm = raw_input("Add more ingredients? (y/n) \n")
			while(confirm != y or confirm != n):
				confirm = raw_input("Add more ingredients? (y/n) \n")
			if (confirm == "n"):
				break
			else:
				return

		recipes.append(recipe(input_title,input_recipe,input_ingredients))
		print "Recipe Added!"
	if (user_input == "quit"):
		quit = True


# beefstrogonoff = recipe("Beef Strog", "put beef in stew", [ingredient("beef",200,True), ingredient("water",400,True)])
# noodles = recipe("noodles", "boil noodles and fry onions", [ingredient("noodles",300, True),ingredient("onion",2,False)])

# recipes = [beefstrogonoff,noodles]

# writerecipes("fatshit.txt", recipes)

# recipes = []

# importrecipes("fatshit.txt")

# print recipes[0].title + recipes[1].title

			
		
		
	
	
	
		

#do stuff here to import recipes using structure used for writing
