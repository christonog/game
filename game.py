from sys import exit
import prompts

class Player(object):

	def __init__(self):
		self.health = 100
		self.weapons = []
		self.carried_items = []

class House(object):
	player = Player()

	def living_room(self):

		print "You're currently home."
		print "You currently have %d health, %d weapons, %d carried items" % (player.health, len(player.weapons), len(player.carried_items))
		print "There are several items:"
		print "1. A Sword"
		print "2. Healing Potion"
		print "3. A Bow & Arrow"

		while True:
			print "Enter the number next to the item you want to pick up. Press 'x' to exit."
			pick_up = raw_input("> ")

			if pick_up == "1":
				player.weapons.append("sword")
				print "You picked up the sword."
				print "Your Inventory: "
				print "You have %d weapons, %d carried items, and %d health" % (player.health, len(player.weapons), len(player.carried_items))

			elif pick_up == "2":
				player.carried_items.append("Potion")
				print "You picked up the potion."

			elif pick_up == "3":
				player.weapons.append("bow & arrow")
				print "You picked up the bow & arrow."

			elif pick_up == "x":
				break

			else:
				print "enter the number next to the item you want to pick up."
				pick_up = raw_input("> ")


class Game(object):

	def __init__(self, response):
		self.response = response

		if self.response.lower() == "play":
			house = House()
			house.living_room()

		else:
			while True:
				if self.response.lower() == "yes":
					house = House()
					house.living_room()
					
				elif self.response.lower() == "no":
					print "good bye.".title()
					exit(1)
				else:
					print "Type \"play\" to start. Or \"No\" to exit."
					self.response = raw_input(prompt)

prompts.start_game()

prompt = "> "

game = Game(raw_input(prompt))