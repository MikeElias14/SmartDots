from Class.Population import Population
from Class.Window import Window

import time

def __main__():
	win = Window(750, 750)

	win.createGoal()
	pop = Population(100)

	win.showPopulation(pop)

	# Create Walls
	win.createWall(0, 300, 0, 300)
	win.createWall(450, 750, 0, 300)
	win.createWall(0,500,500, 520)

	# TODO: Refactor tkinter to exit gracefully
	while win:
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


if __name__ == "__main__":
	__main__()
