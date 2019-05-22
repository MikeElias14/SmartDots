import math
import random

class Brain:
	def __init__(self, numSteps):
		self.numSteps = numSteps #num of directions
		self.step = 0
		self.directions = []
		self.__randomize__()
		return

	#create random directions/velocities for all steps
	def __randomize__(self):
		for i in range(self.numSteps):
			randomAngle = math.radians(random.randint(0, 360))
			
			x = math.cos(randomAngle)
			y = math.sin(randomAngle)

			self.directions.append([x,y])
		return

	#Copy the brain of the parent dot
	def clone(self, parentDot):
		for i in range(self.numSteps):
			self.directions[i] = parentDot.brain.directions[i]
		return

	#Randomly change {mutationRate} percent of Steps
	def mutate(self, mutationRate):
		for i in range(self.numSteps):
			rand = random.uniform(0.0, 1.0)

			if rand < mutationRate:
				randomAngle = math.radians(random.randint(0, 360))
			
				x = math.cos(randomAngle)
				y = math.sin(randomAngle)

				self.directions[i] = ([x,y])
		return
