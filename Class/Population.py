from .Dot import Dot

import random
import math

class Population:
	def __init__ (self, size):
		self.size = size
		self.dots = []
		self.generation = 1
		self.minSteps = 400 #this should be var. number of max steps in brain
		self.mutationRate = 1 #start with 100% mutation

		for i in range(self.size):
			self.dots.append(Dot())
		return


	def update(self, win):
		for i in range(self.size):
			self.dots[i].update(win)
		return


	def areAllDead(self):
		for i in range(self.size):
			if (self.dots[i].dead == False):
				return False
		return True


	def naturalSelection(self, win):
		newDots = []

		# self.sortPopOnFitness()
		self.totalFitness = self.updateTotalFitness(win)

		for i in range(self.size):
			#makeNewDots
			newDots.append(Dot())

			#GetAParent
			parentDot = self.selectParent()

			#makeBaby
			newDots[i].makeBaby(parentDot)

		#make sure the best dot does not get lost
		newDots[0].makeBaby(self.getChamp())
		self.dots = newDots
		self.generation += 1

		return


	def updateTotalFitness(self, win):
		totalFitness = 0

		for i in range(self.size):
			totalFitness += self.dots[i].findFitness(win)
		return totalFitness


	def selectParent(self):
		rand = random.uniform(0.0, self.totalFitness)

		runningSum = 0.0

		for i in range(self.size):
			runningSum += self.dots[i].fitness #maybe findFitness again.. but already updated so dont have to. may be best practice though
			if runningSum > rand:
				return self.dots[i]
		#should never get here
		return


	def mutateBabies(self):
		self.mutationRate = 0.01
		for i in range(1, self.size): #Start at 1 to not mutate champ
	 		self.dots[i].mutateBrain(self.mutationRate)
		return


	def getChamp(self):
	 	maxFitness = 0
	 	for i in range(self.size):
	 		if self.dots[i].fitness > maxFitness:
	 			maxFitness = self.dots[i].fitness
	 			self.bestDot = self.dots[i]

	 			# if self.dots[bestDot].goalReached == True:
	 			# 	self.minSteps = self.dots[bestDot].brain.step

	 	return self.bestDot


	def howManyReached(self):
		numReached = 0
		for i in range(self.size):
	 		if self.dots[i].goalReached == True:
	 			numReached += 1
		return numReached
