from colorama import init, Fore,Back
init()
import os
from mandalorian import Mandalorian
import time

class Shield:
	def __init__(self):
		self.__available = 1
		self.__b = 0

	def get(self):
		return self.__available

	def get2(self):
		return self.__b
		
	def activate(self,grid,obj_mandalorian):
		self.__available = 0
		obj_mandalorian.disappear_mandalorian(grid,0)
		obj_mandalorian.reappear_mandalorian(grid,1)

	def deactivate(self,grid,obj_mandalorian):
		obj_mandalorian.disappear_mandalorian(grid,1)
		obj_mandalorian.reappear_mandalorian(grid,0)
		self.__b = 1
	
	def refill(self):
		self.__b = 0
		self.__available = 1
