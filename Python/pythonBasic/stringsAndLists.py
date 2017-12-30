#Find and Replace
my_str = "Its thanksgiving day its my birthday too"
print (my_str.replace("day", "month"))

#Printing min and max
x = [2,54,-2,7,12,98]
print (max(x))
print (min(x))

#Finding the first and last in the list
x = ["hello", 2,54,-2,7,12,98,"world"]
print(x[0:1])
print(x[len(x)-1:])

#Creating a new List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
y = x[0:int(len(x)/2)]
z = x[int(len(x)/2):]
z.insert(0, y)
print (z)
