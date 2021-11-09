def simulation(e, t):
    avghappy1 = 0
    avghappy2 = 0
    avghappy3 = 0
    for i in range(t):
        avghappy1 = avghappy1 + explore()
        avghappy2 = avghappy2 + exploit()
        avghappy3 = avghappy3 + e_greedy(e)
    avghappy1 = avghappy1 / t
    avghappy2 = avghappy2 / t
    avghappy3 = avghappy3 / t
    exploitexphappy = 9 + 7 + 11 + (11 * 297)
    exploreexphappy = (9 * 100) + (7 * 100) + (11 * 100)
    egreedyexphappy = (7 * 12) + (9 * 12) + (11 * 12) + (11 * 264)

    print("Optimum Happiness: 3300 \n")

    print("Exploit Only Expected Happiness: " + str(exploitexphappy))
    print("Exploit Only Average Happiness: " + str(avghappy2))
    print("Exploit Only Expected Regret: " + str(3300 - exploitexphappy))
    print("Exploit Only Average Regret: " + str(3300 - avghappy2) + "\n")

    print("Explore Only Expected Happiness: " + str(exploreexphappy))
    print("Explore Only Average Happiness: " + str(avghappy1))
    print("Explore Only Expected Regret: " + str(3300 - exploreexphappy))
    print("Explore Only Average Regret: " + str(3300 - avghappy1) + "\n")

    print("eGreedy Only Expected Happiness: " + str(egreedyexphappy))
    print("eGreedy Only Average Happiness: " + str(avghappy3))
    print("eGreedy Only Expected Regret: " + str(3300 - egreedyexphappy))
    print("eGreedy Only Average Regret: " + str(3300 - avghappy3) + "\n")

