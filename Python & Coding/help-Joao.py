#This game was inspired by the old knights of middle Ages.
print('You are a captain and are in charge of a troop of 10 thousand men\nmarching with your troops towards war against the army that wants to enslave you to steal your gold.')

print('One of your warriors presents you with a plan to surprise the enemy army.')
print('The plan is either to take the SHORTEST path and face them head-on or the LONGEST path and take them by surprise.')

# set choices = to string outputs to be used later
shortest = 'your enemies are not there. They went to your camp to kidnap your children and women.'
longest = "the path shown on the map is wrong and you are lost on a beach. It's late at night."

# set variable name = to input.
distance = input('As a captain, what do you decide? go the SHORTEST way or the LONGEST?  ')

# check to see what the input was

if distance.lower() == "shortest":
    # First choice
    print('Upon arriving at the place, '  + str(shortest))
elif distance.lower() == "longest":
    # Second choice
    print("Upon arriving at the place, "  +  str(longest))
else:
    # something other than "shortest" or "longest"
    print('As a captain, it is necessary to make a decision. lives are at risk!')