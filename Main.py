from Class.Population import Population
from Class.Window import Window

import time

win = Window(750, 750)

win.createGoal()
pop = Population(100)

win.showPopulation(pop)

# TODO: how to get no errors on close
while True:
	time.sleep(0.01)
	pop.update(win)

	if(pop.areAllDead() == True):
		numReached = pop.howManyReached()
		genTotalFitness = pop.updateTotalFitness(win)
		generation = pop.generation

		pop.naturalSelection(win)
		pop.mutateBabies()
		win.showPopulation(pop)
		print("Generation %s. NumReached = %s. TotalFitness = %s." %(generation, numReached, genTotalFitness))

	win.updateDotsUi(pop)
	win.update()
