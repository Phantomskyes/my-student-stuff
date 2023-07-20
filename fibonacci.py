
selection = input("Pick a number from the fibonacci spiral (0, 1, 1, 2, 3, 5, 8, etc): ")


spiral = [0, 1]
complete = False

while not complete:
    if spiral[-1] == int(selection):
        complete = True
        print(spiral)
    spiral.append(spiral[-2] + spiral[-1])
