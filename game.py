from sys import exit

prompt = "> "

def dark_forest():
	print "You have entered the dark forest."

print "Welcome to the dark forest."
print "Do you want to enter the dark forest?"

response = raw_input(prompt)

if response.lower() == "yes":
	print "Great! let's get started..."
	dark_forest()
elif response.lower() == "no":
	print "Good bye."
else:
	while True:
		if response.lower() == "yes":
			dark_forest()
		elif response.lower() == "no":
			print "good bye".capitalize()
			exit(1)
		else:
			print "Enter yes or no"
			response = raw_input(prompt)


