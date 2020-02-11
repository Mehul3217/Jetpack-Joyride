from colorama import init,Fore,Back
from mandalorian import Mandalorian
import os


class Magnet():
	def __init__(self,x,y):
		self.__shape = ["N",":",":","S"]
		self.__x=x
		self.__y=y


	def place_magnet(self,grid):
		for i in range(4):
			if i==0:
				grid[self.__x][self.__y+i] = Fore.RED+self.__shape[i]+'\x1b[0m'
			elif i==1 or i==2:
				grid[self.__x][self.__y+i] = Back.WHITE+self.__shape[i]+'\x1b[0m'
			else:
				grid[self.__x][self.__y+i] = Fore.BLUE+self.__shape[i]+'\x1b[0m'


	def check_range(self,grid,listm,left,right,obj_mandalorian):
		for i in range(len(listm)):
			a=max(listm[i].__x-10,1)
			b=max(listm[i].__y-10,left)
			c=min(listm[i].__x+10,47)
			d=min(listm[i].__y+10,right-1)
			if obj_mandalorian.get_x()+2-a>=1 and listm[i].__x-obj_mandalorian.get_x()+2>=1:
				if obj_mandalorian.get_y()+2-b>=1 and listm[i].__y-obj_mandalorian.get_y()+2>=1:
					obj_mandalorian.disappear_mandalorian(grid,0)
					obj_mandalorian.set_y(min(obj_mandalorian.get_y()+2,right-1))
					obj_mandalorian.set_x(min(obj_mandalorian.get_x()+2,45))
					obj_mandalorian.reappear_mandalorian(grid,0)
				elif obj_mandalorian.get_y()-listm[i].__y>=1 and d-obj_mandalorian.get_y()>=1:
					obj_mandalorian.disappear_mandalorian(grid,0)
					obj_mandalorian.set_y(max(obj_mandalorian.get_y()-2,left))
					obj_mandalorian.set_x(min(obj_mandalorian.get_x()+2,45))
					obj_mandalorian.reappear_mandalorian(grid,0)
			elif obj_mandalorian.get_x()-listm[i].__x>=1 and c-obj_mandalorian.get_x()>=1:
				if obj_mandalorian.get_y()+2-b>=1 and listm[i].__y-obj_mandalorian.get_y()+2>=1:
					obj_mandalorian.disappear_mandalorian(grid,0)
					obj_mandalorian.set_y(min(obj_mandalorian.get_y()+2,right-1))
					obj_mandalorian.set_x(max(obj_mandalorian.get_x()-2,1))
					obj_mandalorian.reappear_mandalorian(grid,0)
				elif obj_mandalorian.get_y()-listm[i].__y>=1 and d-obj_mandalorian.get_y()>=1:
					obj_mandalorian.disappear_mandalorian(grid,0)
					obj_mandalorian.set_y(max(obj_mandalorian.get_y()-2,left))
					obj_mandalorian.set_x(max(obj_mandalorian.get_x()-2,1))
					obj_mandalorian.reappear_mandalorian(grid,0)