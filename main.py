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


def do_iteratively(endStep):
    l = [0]
    while len(l) > 0:
        fr = l[-1]
        del l[-1]

        if fr == endStep:
            turtle.forward(50)
            continue
        elif fr == -2:
            turtle.right(60)
            continue
        elif fr == -1:
            turtle.left(60)
            continue

        l.append(fr + 1)
        l.append(-2) #turtle.right(60)
        l.append(fr + 1)
        l.append(-1) #turtle.left(60)
        l.append(-1)
        l.append(fr + 1)
        l.append(-2)
        l.append(fr + 1)


endStep = input("To what depth?")
# do_recursively(0, endStep)
do_iteratively(endStep)

while True:
    pass