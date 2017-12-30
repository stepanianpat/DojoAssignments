# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A
def scores_grades():
import random
for x in range(0,10):
	g = random.randint(60,101)
	if g >= 60 and g <=69:
		print("Score: "+str(g)+"; Your grade is D")
	elif g >= 70 and g <=79:
		print("Score: " + str(g)+"; Your grade is C")
	elif g >= 80 and g <= 89:
		print("Score: " + str(g)+"; Your grade is B")
	else:
		print("Score: " + str(g)+"; Your grade is A")
	print("End of the program. Bye!")
