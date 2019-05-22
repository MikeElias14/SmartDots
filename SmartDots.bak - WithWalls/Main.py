from Class.Population import Population
from Class.Window import Window

import time

win = Window(750, 750)

win.createGoal()
pop = Population(100)

win.showPopulation(pop)
# win.createWall(0, 300, 0, 300)
# win.createWall(450, 750, 0, 300)
# win.createWall(100, 650, 400, 450)
# win.createWall(0,500,500, 520)
# win.createWall(250,750,300,320)

while True: ##how to get no errors on close
	time.sleep(0.01)
	pop.update(win)

	if(pop.areAllDead() == True):
		numReached = pop.howManyReached()
		genTotalFitness = pop.updateTotalFitness(win)
		pop.naturalSelection(win)
		pop.mutateBabies(win)
		win.showPopulation(pop)
		print("Generation %s. NumReached = %s. TotalFitness = %s. Mutation Rate = %s." %(pop.generation, numReached, genTotalFitness, pop.mutationRate))

	win.updateDotsUi(pop)
	win.update()
