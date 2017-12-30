#Odd/Even
number = 0 
counter = 0
while number <= 2000:
	print "Number is", counter 
	number = number + 1
	counter = counter + 1
	if number%2 == 0:
		print "This is an even number"
	else:
		print "This is an odd number"

#"Dry Code"		
for x in range(1,2001):
    if x%2 != 0:
        print ("Number is "+str(x)+". This is an odd number.")
    else:
        print ("Number is "+str(x)+". This is an even number.")