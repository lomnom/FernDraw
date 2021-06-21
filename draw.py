# importing necessary modules
from random import randint
import FUNC as f
from TERMINALFUNC import FramerateLimiter
import pyautogui as pag
import datetime
  
def biggest(theList):
	biggestThing=theList.pop()
	for thing in theList:
		if thing>biggestThing:
			biggestThing=thing
	return biggestThing

def smallest(theList):
	smallestThing=theList.pop()
	for thing in theList:
		if thing<smallestThing:
			smallestThing=thing
	return smallestThing

input("top left edge")
topLeftEdge=pag.position()

input("bottom right edge")
bottomRightEdge=pag.position()

# initializing the list
x = []
y = []
  
# setting first element to 0
x.append(0)
y.append(0)
  
current = 0

f.log("getting points")

for i in range(1, 50000):
	# generates a random integer between 1 and 100
	z = randint(1, 100)
  
	# the x and y coordinates of the equations
	# are appended in the lists respectively.
	  
	# for the probability 0.01
	if z == 1:
		x.append(0)
		y.append(0.16*(y[current]))
	  
	# for the probability 0.85  
	if z>= 2 and z<= 86:
		x.append(0.85*(x[current]) + 0.04*(y[current]))
		y.append(-0.04*(x[current]) + 0.85*(y[current])+1.6)
	  
	# for the probability 0.07  
	if z>= 87 and z<= 93:
		x.append(0.2*(x[current]) - 0.26*(y[current]))
		y.append(0.23*(x[current]) + 0.22*(y[current])+1.6)
	  
	# for the probability 0.07  
	if z>= 94 and z<= 100:
		x.append(-0.15*(x[current]) + 0.28*(y[current]))
		y.append(0.26*(x[current]) + 0.24*(y[current])+0.44)
		  
	current = current + 1

f.log("done!")

f.log("getting values")
biggestX=biggest(x)
biggestY=biggest(y)

smallestX=smallest(x)
smallestY=smallest(y)

middleXOfCanvas=topLeftEdge.x+abs((topLeftEdge.x-bottomRightEdge.x)/2)

fractalSizeX=biggestX-smallestX
fractalSizeY=biggestY-smallestY

canvasSizeX=abs(topLeftEdge.x-bottomRightEdge.x)
canvasSizeY=abs(topLeftEdge.y-bottomRightEdge.y)

transform=canvasSizeY/fractalSizeY
f.log("done!")

print("fractalSizeY: {}, fractalSizeX: {}".format(fractalSizeY,fractalSizeX))
print("canvasSizeX: {}, canvasSizeY: {}".format(canvasSizeX,canvasSizeY))
print("transform: {}".format(transform))

rateLimiter=FramerateLimiter(2)

f.log("starting to draw!")
for n in f.everyIndexInList(x):
	rateLimiter.startFrame()

	theX=middleXOfCanvas+(x[n]*transform)
	theY=bottomRightEdge.y-(y[n]*transform)
	print("")
	f.log("x: {}, y: {}".format(x[n],y[n]))
	f.log("transformedX: {}, transformedY: {}".format(theX,theY))
	f.log(("clickX: {}, clickY: {}".format(theX,theY)))
	f.log("progress: {}/{}".format(n,len(x)-1))
	f.log("time left: {}".format(str(datetime.timedelta(seconds=(len(x)-(n+1))*0.5))))

	pag.moveTo(theX,theY)
	pag.click()

	rateLimiter.endFrame()
	rateLimiter.delayTillNextFrame()
f.log("finished")