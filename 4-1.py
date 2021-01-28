#4-1
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

x,y,z = mc.player.getTilePos()

for i in range(20):
    r = random.randrange(1,5)
    if r == 1: #前
        mc.setBlocks(x,y,z,x,y,z+4,41)
        z = z+4
    if r == 2: #後
        mc.setBlocks(x,y,z,x,y,z-4,41)
        z =z-4
    if r == 3:#右
        mc.setBlocks(x,y,z,x+4,y,z,41)
        x = x+4
    if r == 4: #左
        mc.setBlocks(x,y,z,x-4,y,z,41)
        x =x-4