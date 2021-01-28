from mcpi.minecraft import Minecraft
mc = Minecraft.create()

list2 = [[12,41,14],[35,73,86]]

myID = mc.getPlayerEntityId("CHUNNN812") #你的ID
x,y,z = mc.entity.getTilePos(myID)

startX = x

for i in list2: #看大清單裡有幾個小清單
    for j in i: #小清單裡面有幾個數值
        
        mc.setBlock(x,y,z,j)
        x = x+1
    x = startX
    z = z-1
    
    