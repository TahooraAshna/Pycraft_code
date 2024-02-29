from mcpi_e.minecraft import *
from mcpi_e.block import *
import collections
collections.Iterable=collections.abc.Iterable
import collections.abc
from _collections_abc import Iterable
from time import *

serverAddress = "Pycraft.yasan.ac"
pythonPort = 29035
PlayerName = "t_vahedi"

x , z, y = mc.player.getTilePos()
dir = "e"

  
while True :
    mc.setBlock(x,z,y,AIR )

    if dir == "e" :
        if mc.getBlock(x,z+1,y) == 0 :
            z += 1   
            mc.setBlock(x,z,y,GLOWSTONE_BLOCK)
            dir = "s"
        elif mc.getBlock(x+1 ,z ,y) == 0 :
            x += 1
            mc.setBlock(x,z,y,GLOWSTONE_BLOCK)
            dir = "e"
        elif mc.getBlock(x ,z-1 ,y) == 0 :
            z -= 1
            mc.setBlock(x,z,y,GLOWSTONE_BLOCK)
            dir = "n"
        elif mc.getBlock(x-1 ,z ,y) == 0 :
            x -= 1
            mc.setBlock(x,z,y,GLOWSTONE_BLOCK)
            dir = "w"

    elif dir == "s" :
        if mc.getBlock(x-1 ,z ,y) == 0 :
            x -= 1
            mc.setBlock(x,z,y,GLOWSTONE_BLOCK)
            dir = "w"  
        elif mc.getBlock(x,z+1,y) == 0 :
            z += 1   
            mc.setBlock(x,z,y,GLOWSTONE_BLOCK)
            dir = "s"
        elif mc.getBlock(x+1 ,z ,y) == 0 :
            x += 1
            mc.setBlock(x,z,y,GLOWSTONE_BLOCK)
            dir = "e"
        elif mc.getBlock(x ,z-1 ,y) == 0 :
            z -= 1
            mc.setBlock(x,z,y,GLOWSTONE_BLOCK)
            dir = "n"
            
    elif dir == "w" :
        if mc.getBlock(x ,z-1 ,y) == 0 :
            z -= 1
            mc.setBlock(x,z,y,GLOWSTONE_BLOCK)
            dir = "n"
        elif mc.getBlock(x-1 ,z ,y) == 0 :
            x -= 1
            mc.setBlock(x,z,y,GLOWSTONE_BLOCK)
            dir = "w"  
        elif mc.getBlock(x,z+1,y) == 0 :
            z += 1   
            mc.setBlock(x,z,y,GLOWSTONE_BLOCK)
            dir = "s"
        elif mc.getBlock(x+1 ,z ,y) == 0 :
            x += 1
            mc.setBlock(x,z,y,GLOWSTONE_BLOCK)
            dir = "e"

    elif dir == "n" :
        if mc.getBlock(x+1 ,z ,y) == 0 :
            x += 1
            mc.setBlock(x,z,y,GLOWSTONE_BLOCK)
            dir = "e" 
        elif mc.getBlock(x ,z-1 ,y) == 0 :
            z -= 1
            mc.setBlock(x,z,y,GLOWSTONE_BLOCK)
            dir = "n"
        elif mc.getBlock(x-1 ,z ,y) == 0 :
            x -= 1
            mc.setBlock(x,z,y,GLOWSTONE_BLOCK)
            dir = "w"  
        elif mc.getBlock(x,z+1,y) == 0 :
            z += 1   
            mc.setBlock(x,z,y,GLOWSTONE_BLOCK)
            dir = "s"
    if mc.getBlock(x,y-1,z) == 57 :
        mc.PostToChat ("finish") 
        break

    sleep(0.4)