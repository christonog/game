from sys import exit
import prompts

class Player(object):

	def __init__(self):
		self.health = 100
	
	def swing_sword(self):
		print "you swung your sword"

	def punch(self):
		print "you punched the dragon!"

class Dragon(object):
	
	def __init__(self):
		self.health = 100

	def swing_tail(self):
		print "The dragon swung its tail."
	
	def breath_fire():
		print "The dragon breathed fire."

class Battle(object):
	
	def __init__(self):
		self.player = Player()
		self.dragon = Dragon()

	def start_battle(self):
		print "The battle has begun!"
		prompts.battle_prompt(self.player.health, self.dragon.health)
		self.battle()
	
	def battle(self):

		while self.player.health != 0 and self.dragon.health != 0:
			action = raw_input("> ")

			if action == "punch":
				self.player.punch
			elif action == "avoid":
				print "You avoided it!"

			if self.player.health == 0:
				print "You lost"
			elif self.dragon.health == 0:
				print "You won!"


class Game(object):

	def __init__(self, response):
		self.response = response

		if self.response.lower() == "play":
			battle = Battle()
			battle.start_battle()

		else:
			while True:
				if self.response.lower() == "yes":
					battle = Battle()
					battle.start_battle()
					
				elif self.response.lower() == "no":
					print "good bye.".title()
					exit(1)
				else:
					print "Type \"play\" to start. Or \"No\" to exit."
					self.response = raw_input(prompt)

prompts.start_game()

prompt = "> "

game = Game(raw_input(prompt))