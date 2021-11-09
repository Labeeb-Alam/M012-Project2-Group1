import random


def e_greedy(e):
    c1 = random.normalvariate(9, 3)
    c2 = random.normalvariate(7, 5)
    c3 = random.normalvariate(11, 7)
    for x in range(297):
        r = random.randint(0,100)
        if e >= r:
            if c1 > c2 and c1 > c3:
                c1 += random.normalvariate(9, 3)
            elif c2 > c1 and c2 > c3:
                c2 += random.normalvariate(7, 5)
            elif c3 > c1 and c3 > c2:
                c3 += random.normalvariate(11, 7)
        else:
            x = random.randint(1, 3)
            if x == 1:
                c1 += random.normalvariate(9, 3)
            elif x == 2:
                c2 += random.normalvariate(7, 5)
            elif x == 3:
                c3 += random.normalvariate(11, 7)

    return c1 + c2 + c3

x = e_greedy(30)
print(x)










