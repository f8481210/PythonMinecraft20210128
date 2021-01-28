#4-3
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange

for i in range(10):
    x,y,z = mc.player.getTilePos()
    z = z+i
    for j in range(10):
        color = randrange(0,16)
        x = x+1
        mc.setBlock(x,y,z,35,color)
#生成平面
        
ans = randrange(0,16) #問題
while True:
    hits = mc.events.pollBlockHits()
    if len(hits)>0:
        h = hits[0]
        block = mc.getBlockWithData(h.pos)
        data = block.data #data = 我的答案
        
        if data == ans :
            mc.postToChat("恭喜你找到啦!")
            mc.setBlock(h.pos,57)
            break
        
        elif data < ans:
            mc.postToChat("找錯囉~~~ 找大一點的吧!")
        
        elif data > ans:
            mc.postToChat("找錯囉~~~ 找小一點的吧!")