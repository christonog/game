def start_game():
	print """Welcome to The Small Island Adventure RPG game. You are Sam,
	a young peasant looking for some food and supplies for your family.
	Though the island you live on is small, it has many environments and
	areas; one could easily get lost.
	""" 

	print "Type \"play\" to start."

def battle_prompt(player, dragon):
	print "You have %d health, while the dragon has %d health." % (player, dragon)
	print "You can "
	print "What do you do?"
	