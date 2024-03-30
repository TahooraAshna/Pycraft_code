from mcpi_e.minecraft import *
from mcpi_e.block import *
import collections
collections.Iterable=collections.abc.Iterable
import collections.abc
from _collections_abc import Iterable

serverAddress = "Pycraft.yasan.ac"
pythonPort = 29035
PlayerName = "t_vahedi"

def feroon (fillname,start_x,start_y,start_z) :
    fill = open(fillname)
    for line in fill :
        nums = line.strip().split(" ")
        print(nums)
        x = int(nums[0]) + start_x
        y = int(nums[1]) + start_y
        z = int(nums[2]) + start_z
        b = int(nums[3])
        mc.setBlock(x, y, z, b)
xp , zp, yp = mc.player.getPos()
for i in range (5) :
    feroon("unknown.txt",xp,yp,zp+10*i)