import os
from mandalorian import Mandalorian
from colorama import Fore,Back

class Board:
    def __init__(self,rows,cols):
        self._rows = rows
        self._cols = cols
        self._mat = []
    def create(self):
    	for i in range(self._rows):
    		self.n = []
    		for j in range(self._cols):
    			self.n.append(" ")
    		self._mat.append(self.n)

    def get_mat(self):
    	return self._mat

    def set_mat(self,c,d,val):
    	self._mat[c][d] = val

    def printi(self,a):
    	if a==0:
    		for i in range(self._rows):
    			for j in range(a,a+203):
    				print(self._mat[i][j],end="")
    			print()
    	else:
    		for i in range(self._rows):
    			for j in range(a,a+204):
    				print(self._mat[i][j],end="")
    			print()

    def spawn_mandalorian(self,obj_mandalorian,left):
    	obj_mandalorian.set_x(45)
    	obj_mandalorian.set_y(left)
    	obj_mandalorian.reappear_mandalorian(self._mat,0)