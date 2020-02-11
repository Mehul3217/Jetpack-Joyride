import random
import os
from enemy import Person
from colorama import init, Fore,Back

class Mandalorian(Person):

	def __init__(self,x,y):
		Person.__init__(self,x,y)
		self.__shape = [ ["|", "$", "|"], [" ",  "|" ," "], ["^"," ","^"] ]
		self.__shape2 = [ ["|", " ", "|"], ["|",  "$" ,"|"], ["|"," ","|"] ]
		self._life = 4
		self._allowed_collision = ["O"," ",Fore.YELLOW+'$'+'\x1b[0m']
		self._collision_magnet = ["O"," ",Fore.RED+'N'+'\x1b[0m',Back.WHITE+':'+'\x1b[0m',Fore.BLUE+'S'+'\x1b[0m',Fore.YELLOW+'$'+'\x1b[0m']
		self._coins = 0
		self._kills = 0

	def get_x(self):
		return self._x
	def set_x(self,x):
		self._x = x
	def get_y(self):
		return self._y
	def get_kills(self):
		return self._kills
	def get_coins(self):
		return self._coins
	def get_life(self):
		return self._life
	def set_y(self,y):
		self._y = y
	def set_life(self):
		self._life-=1
	def get_collision(self):
		return self._allowed_collision
	def get_magnet(self):
		return self._collision_magnet
	def set_coins(self):
		self._coins+=1
	def set_kills(self):
		self._kills+=1

	def start_pos(self,grid):
		for i in range(45,48,1):
			for j in range(0,3,1):
				grid[i][j] = self.__shape[i-45][j]

	def increment_position(self,grid,c,pos):
		self._y+=pos
		if c == 0:
			for i in range(self._x,self._x+3,1):
				for j in range(self._y,self._y+3,1):
					grid[i][j] = self.__shape[i-self._x][j-self._y]
		else:
			for i in range(self._x,self._x+3,1):
				for j in range(self._y,self._y+3,1):
					grid[i][j] = self.__shape2[i-self._x][j-self._y]

	def disappear_mandalorian(self,grid,c):
		if c == 0:
			for i in range(self._x,self._x+3,1):
				for j in range(self._y,self._y+3,1):
					grid[i][j] = " "
		else:
			for i in range(self._x,self._x+3,1):
				for j in range(self._y,self._y+3,1):
					grid[i][j] = " "

	def reappear_mandalorian(self,grid,c):
		if c == 0:
			for i in range(self._x,self._x+3,1):
				for j in range(self._y,self._y+3,1):
					grid[i][j] = self.__shape[i-self._x][j-self._y]
		else:
			for i in range(self._x,self._x+3,1):
				for j in range(self._y,self._y+3,1):
					grid[i][j] = self.__shape2[i-self._x][j-self._y]