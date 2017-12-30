def draw_stars(my_list):
	for element in my_list:
		my_string = ""
		if type(element) is int:
			for count in range(0,element):
				my_string += "*"
		elif type(element) is str:
			for count in range (0, len(element)):
				my_string += element[0]

		print (my_string.lower())

draw_stars([4, 10, 20, 30, 40, 50])