#Magician
import math


dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200,0)
dType.SetPTPCoordinateParams(api,200,200,200,200,0)
dType.SetPTPJumpParams(api, 10, 200,0)
dType.SetPTPCommonParams(api, 100, 100,0)
x = 117
y = 22
z = -5
rHead = 11
stredX = 247
stredY = -7
stredZ = -53
dType.SetPTPCmd(api, 2, x, y, z, rHead, 1)
dType.SetPTPCmd(api, 2, stredX, stredY, stredZ, rHead, 1)
dType.SetPTPCmd(api, 2, stredX, stredY, stredZ+30, rHead, 1)
for uhelStup in range(360):
	uhelRad = math.radians(uhelStup)
	velikost = 15
	X=stredX + velikost * math.cos(uhelRad)
	Y=stredY + velikost * math.sin(uhelRad)
	dType.SetPTPCmd(api, 2, X, Y, stredZ, rHead, 1)
dType.SetPTPCmd(api, 2, x, y, z, rHead, 1)
