#4-1
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange

x,y,z = mc.player.getTilePos()

for i in range(20):
    r = randrange(1,7)
    if r == 1: #前
        mc.setBlocks(x,y,z,x,y,z+4,46)
        z = z+4
    elif r == 2: #後
        mc.setBlocks(x,y,z,x,y,z-4,41)
        z =z-4
    elif r == 3:#右
        mc.setBlocks(x,y,z,x+4,y,z,35)
        x = x+4
    elif r == 4: #左
        mc.setBlocks(x,y,z,x-4,y,z,29)
        x =x-4
    elif r == 5: #上
        mc.setBlocks(x,y,z,x,y+4,z,57)
        y =y+4
    elif r == 6: #下
        mc.setBlocks(x,y,z,x,y-4,z,88)
        y =y-4
    
 #挑戰題：上下 4-2