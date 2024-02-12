from mcpi_e.minecraft import *
from mcpi_e.block import *
import collections
collections.Iterable=collections.abc.Iterable
import collections.abc
from _collections_abc import Iterable
from random import *

serverAddress = "Pycraft.yasan.ac"
pythonPort = 29035
PlayerName = "t_vahedi"

def village (filename,start_x,start_y,start_z) :
    file = open(filename)
    for line in file :
        nums = line.strip().split(" ")
        print(nums)
        x = int(nums[0]) + start_x
        y = int(nums[1]) + start_y
        z = int(nums[2]) + start_z
        b = int(nums[3])
        mc.setBlock(x, y, z, b)
xp , zp, yp = mc.player.getPos()

for i in range (2) :
    for j in range (4) :
        for k in range (randint(1,5)) :
            village ("house.txt",xp+10*i ,yp+5*k ,zp+10*j)