def while_loop(rb, step):
	i = 0
	numbers = []

	while i < rb:
		print "At the top i is %d" %i
		numbers.append(i)

		i = i+step
		print "Numbers now: ", numbers
		print "At the bottom i is %d" %i

	print "The numbers: "

	for num in numbers:
		print num

while_loop(7, 2)
