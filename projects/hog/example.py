from hog import *
dice = make_test_dice(1,2)
sum = 0
a = 1000
while a > 0:
    sum += roll_dice(2,dice)
    a -= 1