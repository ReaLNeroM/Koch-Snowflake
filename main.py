import turtle

def do_recursively(step, endStep):
	if step == endStep:
		turtle.forward(50)
		return

	do_recursively(step + 1, endStep)
	turtle.right(60)
	do_recursively(step + 1, endStep)
	turtle.left(60)
	turtle.left(60)
	do_recursively(step + 1, endStep)
	turtle.right(60)
	do_recursively(step + 1, endStep)


def koch(length, order):
	l = [0] #l is an update list
	size = [length]
	while len(l) > 0:
		fr = l[-1]
		del l[-1]

		if fr == endStep:
			frlength = size[-1]
			del size[-1]
			turtle.forward(frlength)
			continue
		elif fr == -2:
			turtle.right(60)
			continue
		elif fr == -1:
			turtle.left(60)
			continue

		
		frlength = size[-1]
		del size[-1]

		l.append(fr + 1)
		size.append(length / 3.0)
		l.append(-2) #turtle.right(60)
		l.append(fr + 1)
		size.append(length / 3.0)
		l.append(-1) #turtle.left(60)
		l.append(-1)
		l.append(fr + 1)
		size.append(length / 3.0)
		l.append(-2)
		l.append(fr + 1)
		size.append(length / 3.0)


endStep = input("To what depth?")
length = 100.0
# do_recursively(0, endStep)
koch(length, endStep)

while True:
	pass