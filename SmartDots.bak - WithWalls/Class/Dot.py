from .Brain import Brain
import math

class Dot:
	def __init__(self):
		self.brain = Brain(400)
		self.pos = (750/2, 750-50) #TODO: GLOBAL VARS
		self.startPos = self.pos
		self.acc = (0,0)
		self.vel = (0,0)
		self.dead = False
		self.goalReached = False
		self.parent = None
		return


	def __move__(self):

		#for each step in brain, move the dot
		if (len(self.brain.directions) > self.brain.step):
			self.acc = self.brain.directions[self.brain.step]
			self.brain.step += 1
		else: #If no more steps, die
			self.dead = True

		self.vel = [(x + y) for x, y in zip(self.vel, self.acc)]
		self.pos = [(x + y) for x, y in zip(self.pos, self.vel)]

		#There is a better way to do this( settting max on vel)
		if self.vel[0] > 5:
			self.vel[0] = 5

		if self.vel[1] > 5:
			self.vel[1] = 5
		return


	def update(self, win):

		if(self.dead == False):
			self.__move__()

		#if the dot hits the edge of the screen, kill it
		if (self.pos[0] > win.width-5 or self.pos[0] < 5 or self.pos[1] > win.height-5 or self.pos[1] < 5): #is there a way to simplify this ##TODO: UPDATE GLOBAL VARRS
			self.dead = True

		#if the dot hits a wall, kill it
		for i in range(len(win.walls)):
			if (self.pos[0] >= win.walls[i].x1-3 and self.pos[0] <= win.walls[i].x2+3 and self.pos[1] >= win.walls[i].y1-3 and self.pos[1] <= win.walls[i].y2+3):
				self.dead = True


		#if it reahces the goal then yay!! and its dead...
		if (self.pos[0] >= win.goal.pos[0]-5 and self.pos[0] <= win.goal.pos[0]+5 and self.pos[1] >= win.goal.pos[1]-5 and self.pos[1] <= win.goal.pos[1]+5): #is there a way to simplify this 
			self.goalReached = True
			self.dead = True


		return

	#Fitnessis the inverse of how lose to the goal the dot is/was. This is squared to make the smallest step more impactful
	def findFitness(self, win): 
		self.fitness = 1.0/(math.hypot(self.pos[0] - win.goal.pos[0], self.pos[1] - win.goal.pos[1]))**2
		if(self.goalReached == True):
			self.fitness += (6.0 + 1200.0/(self.brain.step)) #goal bonus plus less steps
		return self.fitness

	def getDistToGoal(self,win):
		distToGoal  = math.hypot(self.pos[0] - win.goal.pos[0], self.pos[1] - win.goal.pos[1])
		return distToGoal

	def makeBaby(self, parentDot):
		self.brain.clone(parentDot)
		return


	def mutateBrain(self, mutationRate):
		self.brain.mutate(mutationRate)
		return
