import random

h = [9,7,11]
d = [3,5,7]
days = 300
m1=days//3

def exploreOnly():
        happy=0
        for num in range(m1):
                happy = happy + random.normalvariate(h[0],d[0])
        for num in range(m1):
                happy = happy + random.normalvariate(h[1],d[1])
        for num in range(m1):
                happy = happy + random.normalvariate(h[2],d[2])
        return happy
