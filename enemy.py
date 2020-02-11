from colorama import init, Fore,Back
init()
import os
import time

class Person:
    def __init__(self,x,y):
        self._x=x
        self._y=y

class Ball:
	def __init__(self,x,y):
		self._x=x
		self._y=y
		self.__shape = [[" ","*"," "],["*","*","*"],[" ","*"," "]]

	def increment(self,grid):
	 	for i in range(3):
	 		for j in range(3):
	 			grid[self._x+i][self._y-j] = Back.WHITE+self.__shape[i][j]+'\x1b[0m'

	def disappear_bullets(self,grid):
	 	for i in range(3):
	 		for j in range(3):
	 			grid[self._x+i][self._y-j] = " "
	def get_x(self):
		return self._x
	def get_y(self):
		return self._y
	def set_x(self,x):
		self._x = x
	def set_y(self,y):
		self._y = y

class Enemy(Person):
	def __init__(self,x,y):
		self._life = 3
		self._boss = []
		self._last = time.time()
		Person.__init__(self,x,y)

	def set_life(self):
		self._life -= 1
	def get_life(self):
		return self._life
	def get_last(self):
		return self._last
	def set_last(self,t):
		self._last = t
	def get_x(self):
		return self._x
	def get_y(self):
		return self._y

	def put_boss(self,c,d,grid):
		with open("./boss.txt") as obj:
			for line in obj:
				self._boss.append(line.strip('\n'))

		e=d
		for i in range(26):
			for j in range(61):
				if self._boss[i][j] == " ":
					grid[c][d] = " "
				else:
					grid[c][d] = Fore.GREEN+self._boss[i][j]+'\x1b[0m'
				d+=1
			d=e
			c+=1

	def change_position_up(self,grid):
		for i in range(self._x,self._x+26,1):
			for j in range(self._y,self._y+61,1):
				grid[i][j] = " "
		
		if self._x>3:
			self._x-=3
		else:
			self._x=1
		for i in range(self._x,self._x+26,1):
			for j in range(self._y,self._y+61,1):
				if self._boss[i-self._x][j-self._y] == " ":
					grid[i][j] = " "
				else:
					grid[i][j] = Fore.GREEN+self._boss[i-self._x][j-self._y]+'\x1b[0m'

	def change_position_down(self,grid):
		for i in range(self._x,self._x+26,1):
			for j in range(self._y,self._y+61,1):
				grid[i][j] = " "
		
		if self._x+25 <= 45:
			self._x+=3
		else:
			self._x = 23
		for i in range(self._x,self._x+26,1):
			for j in range(self._y,self._y+61,1):
				if self._boss[i-self._x][j-self._y] == " ":
					grid[i][j] = " "
				else:
					grid[i][j] = Fore.GREEN+self._boss[i-self._x][j-self._y]+'\x1b[0m'