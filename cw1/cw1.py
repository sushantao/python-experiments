# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps.
# Please write a program to compute the distance from current position after a sequence
# of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2
import math

while True:

    up = int(input("Up:"))
    a = input("Do you want up again?")
    if a is "Y":
        secondUp = int(input("Up:"))
        up = up + secondUp
    else:
        pass

    down = int(input("Down:"))
    left = int(input("Left:"))
    right = int(input("Right:"))

    break

l1 = [up - down, left - right]
origin = [0, 0]

distance = ((l1[0] - origin[0]) ** 2 + (l1[1] - origin[1]) ** 2) ** 0.5
print(int(distance))