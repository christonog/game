def start_game():
	print """Welcome to The Small Island Adventure RPG game. You are Sam,
	a young peasant looking for some food and supplies for your family.
	Though the island you live on is small, it has many environments and
	areas; one could easily get lost.
	""" 

	print "Type \"play\" to start."

def start_battle_prompt(player, dragon):
	print "You have %d health, while the dragon has %d health." % (player, dragon)
	print "You can do one of three actions:"
	print "You can punch, enter 'punch'"
	print "You can swing your sword, enter 'swing sword'"
	print "What do you do?"

def punch_attack_prompt(damage_inflicted, enemy_health, death):
	print "you punched the dragon!"
	print "You inflicted %d damage" % damage_inflicted
	print "The dragon has %d health left" % (enemy_health if enemy_health >= 0 else death)

def swing_sword_attack_prompt():
	print "you swung your sword!"
	print "It ended up being a critical hit and killed the dragon."