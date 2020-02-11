from colorama import init,Fore,Back
import os


class Bullets:
	def __init__(self,x,y):
		self._x=x
		self._y=y
		self._shape = ["O"]
		self._allowed_collision = [" ",Fore.RED+'N'+'\x1b[0m',Back.WHITE+':'+'\x1b[0m',Fore.BLUE+'S'+'\x1b[0m',"|"]

	def get_x(self):
		return self._x
	def get_y(self):
		return self._y
	def set_y(self,y):
		self._y = y	

	def disappear_bullets(self,grid):
		if grid[self._x][self._y] == Fore.YELLOW+'$'+'\x1b[0m':
			pass
		else:
			grid[self._x][self._y] = " "

	def get_allowed_collision(self):
		return self._allowed_collision

	def increment_bullets(self,grid):
		grid[self._x][self._y] = Fore.RED+self._shape[0][0]+'\x1b[0m'