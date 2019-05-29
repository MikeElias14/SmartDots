from .Goal import Goal
from .Wall import Wall

import tkinter as tk

class Window:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.walls = []
		self.win = tk.Tk()
		self.win.title('SmartDots')
		self.win.geometry("%dx%d" % (width, height))
		self.canvas = tk.Canvas(self.win, height=width, width=height)
		self.canvas.grid(row=0, column=0, sticky='w')
		

	def showPopulation(self, pop):
		for i in range(pop.size):
			dot = pop.dots[i]
			dot.coords = (dot.pos[0], dot.pos[1], dot.pos[0]+3, dot.pos[1]+3)
			if i == 0:
				dot.body = self.canvas.create_oval(dot.coords, outline = "red", fill = "red")
			else:
				dot.body = self.canvas.create_oval(dot.coords, outline = "black", fill = "black")
		return


	def __showGoal__(self):
		self.goal._coords = (self.goal.pos[0], self.goal.pos[1], self.goal.pos[0]+5, self.goal.pos[1]+5)
		self.goal._body = self.canvas.create_oval(self.goal._coords, outline = "red", fill = "red")
		return


	def updateDotsUi(self,pop):
		for i in range(pop.size):
			dot = pop.dots[i]

			if dot.dead == False:
				# Do the actual updating of the dot UI
				self.canvas.move(dot.body, dot.vel[0], dot.vel[1])
		return


	def update(self):
		self.win.update()
		return


	def createWall(self, x1, x2, y1, y2):
		self.walls.append(Wall(x1,x2,y1,y2))
		self.canvas.create_rectangle(x1, y1, x2, y2, outline = "blue", fill = "blue")
		return


	def createGoal(self):
		self.goal = Goal(self.width/2,50)
		self.__showGoal__()
		return		
