import random
import os
from colorama import init, Fore,Back
init()

class Background:
    def __init__(self):
        self.__sky=Fore.CYAN + "X" + '\x1b[0m'
        self.__ground=Fore.RED + "G" + '\x1b[0m'

    def create_ground(self,grid):
        for i in range(1000):
            grid[49][i] = self.__ground
            grid[48][i] = "_"

    def create_sky(self,grid):
        for i in range(1000):
            grid[0][i]=self.__sky