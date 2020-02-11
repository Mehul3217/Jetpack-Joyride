import random
import os
from colorama import init, Fore,Back
init()

class Obstacle():
	def __init__(self,x,y):
		self._x=x
		self._y=y

	def place_obstacle(self,grid,c,d):
		for i in range(5):
			grid[c][d] = Back.RED+"-"+'\x1b[0m'
			c+=1

class Obstacle_0(Obstacle):
	def __init__(self,x,y):
		Obstacle.__init__(self,x,y)


class Obstacle_1(Obstacle):
	def __init__(self,x,y):
		Obstacle.__init__(self,x,y)

	def place_obstacle(self,grid,c,d):
		for i in range(5):
				grid[c][d] = Back.RED+"-"+'\x1b[0m'
				d+=1

class Obstacle_2(Obstacle):
	def __init__(self,x,y):
		Obstacle.__init__(self,x,y)

	def place_obstacle(self,grid,c,d):
		for i in range(5):
				d=d+4-i
				c=c+i
				grid[c][d] = Back.RED+"-"+'\x1b[0m'

class Obstacle_3(Obstacle):
	def __init__(self,x,y):
		Obstacle.__init__(self,x,y)

	def place_obstacle(self,grid,c,d):
		for i in range(5):
				grid[c][d] = Back.RED+"-"+'\x1b[0m'
				c+=1
				d+=1

class Obstacle_4(Obstacle):
	def __init__(self,x,y):
		Obstacle.__init__(self,x,y)

	def place_obstacle(self,grid,c,d):
		for j in range(8):
				grid[c][d] = Fore.YELLOW+"$"+'\x1b[0m'
				d+=1

class Obstacle_5(Obstacle):
	def __init__(self,x,y):
		Obstacle.__init__(self,x,y)

	def place_obstacle(self,grid,c,d):
		e=d
		for i in range(3):
			for j in range(8):
				grid[c][d] = Fore.YELLOW+"$"+'\x1b[0m'
				d+=1
			d=e
			c+=1
