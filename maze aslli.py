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

xp , zp, yp = mc.player.getPos()

def createMaze(blocktype) :
    my_file = open("maze-map.txt")
    for line in my_file :
        z +=1
        items = line.strip().split(" ")
        x = 0
        for i in items :
            x += 1
            b = AIR if i == "p" else blocktype
            mc.setBlock(xp+x ,yp, zp+z,b)

while True :
    for chat in mc.pollChatPosts() :
        chatparts = chat.message.split(" ")
        if chatparts[0]+" "+ chatparts[1] == "create maze" :
            b = int(chatparts[2])
            createMaze(b)
        
    sleep(0.5)


