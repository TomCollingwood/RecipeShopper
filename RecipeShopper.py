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

def updaterecipetitle(index, newtitle):
	recipes[index] = recipe(newtitle, recipes[index].recipe, recipes[index].ingredients)

def updatereciperecipe(index,newrecipe):
	recipes[index] = recipe(recipes[index].title, newrecipe, recipes[index].ingredients)

def updaterecipeingredientname(recipesindex,ingrindex,newname):
	try:
		recipes[recipesindex].ingredients[ingrindex] = { ingredient(newname, 
			recipes[recipesindex].ingredients[ingrindex].amount,
			recipes[recipesindex].ingredients[ingrindex].gram) }
	except IndexError:
		print "That ingredient does not exist"

def updaterecipeingredientamount(ingredienttochange,newamount):
	if newamount.endswith("g"):
		ingredienttochange.gram = True
		ingredienttochange.amount = newamount[:-1]
	elif newamount.endswith("kg"):
		ingredienttochange.gram = True
		ingredienttochange.amount = newamount[:-1] * 1000
	elif newamount.endswith("mg"):
		ingredienttochange.gram = True
		ingredienttochange.amount = newamount[:-1] / 1000
	else:
		ingredienttochange.ram = False
		ingredienttochange.amount = newamount

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

def printrecipe(index):
	print "Name: "+recipe[index].name+"\n"
	print "Recipe: "+recipe[index].recipe+"\n"
	print "Ingredients: \n"
	for ingredient in recipe[index].ingredients:
		if(ingredient.gram):
			print ingredient.amount+"g of "+ingredient.name+"\n"
		else:
			if (ingredient.amount>1):
				print ingredient.amount+ingredient.name+"s \n"
	print "\n"

def printrecipes():
	for index in range(len(recipes)):
		printrecipe(index);
		
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
				newingredient = ingredient(input_ingr_name, 0,False)
				
				confirm = raw_input(input_ingr_amount+"\nIs this amount correct? (y/n)")
				while(confirm != "y" and confirm != "n"):
					confirm = raw_input(input_ingr_amount+"\nIs this amount correct?  (y/n) \n")

				if (confirm == "y"):
					updaterecipeingredientamount(newingredient,input_ingr_amount)
					break

			input_ingredients.append(newingredient)
			confirm = raw_input("Add more ingredients? (y/n) \n")
			while(confirm != y and confirm != n):
				confirm = raw_input("Add more ingredients? (y/n) \n")
			if (confirm == "n"):
				break

				
		recipes.append(recipe(input_title,input_recipe,input_ingredients))
		print "Recipe Added!"
	if (user_input == "edit"):
		counter = 1
		for r in recipes:
			print "("+counter+") "+r.title+"\n"
		index = raw_input("Enter the integer of the one you want to edit: \n")
		while type(index) != int:
			index = raw_input("I need the INTEGER of the one you want to edit: \n")
		print "Here is your recipe:\n\n"
		printrecipe(index-1)
		response =  raw_input("What would you like to edit? (name, recipe or ingredient 1, ingredient 2 ...)")
		if(response=="name"):
			newinfo = raw_input("What would you like to change it to?")
			updaterecipetitle(newinfo)
		elif(response=="recipe"):
			newinfo = raw_input("What would you like to change it to?")
			updatereciperecipe(newinfo)
		elif(response.startswith("ingredient")):
			responsesplit = response.split(" ")
			whichone = raw_input("Would you like to edit the name or amount of this ingredient?")
			newinfo = raw_input("What would you like to change it to?")
			if(whichone == "name"):
				updaterecipeingredientname(index-1,int(responsesplit[1]),newinfo)
			elif(whichone == "amount"):
				updaterecipeingredientamount(index-1,int(responsesplit[1]),newinfo)
			else:
				print "You screwed up mate. You have to start again because I'm a lazy coder."

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
