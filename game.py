from sys import exit
from random import randint
from time import sleep
import prompts

DEATH = 0 # player and dragon death
TIME_TIL_DRAGON_ATTACK = 5 # in seconds


class Player(object):

	""" sets the player's health at 100 hit points """
	def __init__(self):
		self.health = 100
	
	""" this occurs when the player swings their sword in battle """

	def swing_sword(self):
		prompts.swing_sword_attack_prompt()

	""" this occurs when the player selects punch in battle """

	def punch(self, damage_inflicted, enemy_health):
		prompts.punch_attack_prompt(damage_inflicted, enemy_health, DEATH)

	""" you can use this to attempt to avoid the dragon attack. Randomness will
	eventually be built in (you can only avoid the dragon x percentage
	off the time) but works 100 percent for now
	
	"""

	def avoid_dragon_attack(self):
		print "You avoided it!"

""" the dragon and its attributes and actions """

class Dragon(object):

	""" sets the dragons's health at 100 hit points. Might change this later. """
	
	def __init__(self):
		self.health = 100

	""" one of the ferocious dragon's attacks. """

	def swing_tail(self):
		print "The dragon swung its tail."

	""" Dragon fire breathe attack. Can deliver a fatal blow (to come soon). """
	
	def breath_fire():
		print "The dragon breathed fire."

""" The battle engine for the game """

class Battle(object):

	""" the player and dragon are set up to battle. """
	
	def __init__(self):
		self.player = Player()
		self.dragon = Dragon()

	""" starts the battle and provides the player with initial health and information """

	def start_battle(self):
		print "The battle has begun!"
		prompts.start_battle_prompt(self.player.health, self.dragon.health)
		self.battle()

	""" the actual battle itself. the player is prompted to perform various attacks before
	the dragon attacks (to come soon). 

	"""
	
	def battle(self):

		while self.player.health > DEATH and self.dragon.health > DEATH:

			action = raw_input("> ")
			# sleep(TIME_TIL_DRAGON_ATTACK)
			if action == "punch":
				damage_inflicted = randint(20, 100)
				self.dragon.health -= damage_inflicted
				self.player.punch(damage_inflicted, self.dragon.health)
				self.did_player_win()

			elif action == "avoid":
				self.player.avoid_dragon_attack()

			elif action == "swing sword":
				self.player.swing_sword()
				self.dragon.health -= 100
				self.did_player_win()

			else:
				print "please select an action"
				action = raw_input("> ")

	""" function that indicates whether the player has won. """

	def did_player_win(self):
		if self.player.health <= DEATH:
			print "You lost"
		elif self.dragon.health <= DEATH:
			print "You won!"

""" class that sets up and starts the game """

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