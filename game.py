from sys import exit
from house import *

class Game(object):

	def __init__(self, response):
		self.response = response

		if self.response.lower() == "play":
			house = House()
			house.living_room()

		else:
			while True:
				if self.response.lower() == "yes":
					dark_forest()
				elif self.response.lower() == "no":
					print "good bye.".title()
					exit(1)
				else:
					print "Type \"play\" to start. Or \"No\" to exit."
					self.response = raw_input(prompt)

print """Welcome to The Small Island Adventure RPG game. You are Sam,
a young peasant looking for some food and supplies for your family.
Though the island you live on is small, it has many environments and
areas; one could easily get lost." 

print "Type \"play\" to start."
	"""
prompt = "> "
game = Game(raw_input(prompt))