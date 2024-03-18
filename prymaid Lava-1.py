from mcpi_e.minecraft import *
from mcpi_e.block import *
import collections
collections.Iterable=collections.abc.Iterable
import collections.abc
from _collections_abc import Iterable

serverAddress = "Pycraft.yasan.ac"
pythonPort = 29035
PlayerName = "t_vahedi"

xp , zp, yp = mc.player.getPos()

for y in range (10) :
    for z in range (y , 19-y) :
        for x in range (y , 19-y) :
            mc.setBlock(x+xp , y+yp , z+zp ,STONE)
mc.setBlock(x+xp ,y+yp , z+zp ,LAVA)