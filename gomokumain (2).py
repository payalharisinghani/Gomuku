import turtle
#imports all constants except STONETURT
import const
#ast used in the loadfile function
import ast
import random
import time
turtle.tracer(0)

#create turtle to place moves
STONETURT = turtle.Turtle()
STONETURT.ht()
STONETURT.speed(const.turtspeed)
STONETURT.up()



def aimove(x,y,Z,list,otherlist,window):
	x = centerx(x)
	y = centery(y)
	initialx = x
	initialy = y
	
	#For when the x,y coordinates passed are those from when you hit the new game button
	if x > 275 or x <= 25 or y > 275 or y <= 25:
		x = random.randint(26,275)
		y = random.randint(26,275)
		x = centerx(x)
		y = centery(y)

	#Finds win conditions for ai and plays at the appropriate coordinate
	###make it work for diagonol and xxx-x x-xxx and xx-xx and make it avoid accidental lines > 5
	for q in otherlist:
		if check_hor(q[0],q[1],Z,otherlist) == 4 and (q[0]+4*Z,q[1]) not in list and q[0]+4*Z <= 262.5:
			x = q[0]+4*Z
			y = q[1]
			break
		if check_hor(q[0],q[1],Z,otherlist) == 4 and (q[0]-Z,q[1]) not in list and q[0]-Z >= 37.5 :
			x = q[0]-Z
			y = q[1]
			break
		if check_vert(q[0],q[1],Z,otherlist) == 4 and (q[0],q[1]+4*Z) not in list and q[1]+4*Z <= 262.5:
			x = q[0]
			y = q[1]+4*Z
			break
		if check_vert(q[0],q[1],Z,otherlist) == 4 and (q[0],q[1]-Z) not in list and q[1]-Z >=37.5:
			x = q[0]
			y = q[1]-Z
			break
		if check_lrdiag(q[0],q[1],Z,otherlist) == 4 and (q[0]-Z,q[1]+Z) not in list and q[0]-Z>=37.5 and q[1]+Z <=262.5:
			x = q[0]-Z
			y = q[1]+Z
			break
		if check_lrdiag(q[0],q[1],Z,otherlist) == 4 and (q[0]+4*Z,q[1]-4*Z) not in list and q[0]+4*Z <=262.5 and q[1]-4*Z >= 37.5:
			x = q[0]+4*Z
			y = q[1]-4*Z
			break
		if check_rldiag(q[0],q[1],Z,otherlist) == 4 and (q[0]-Z,q[1]-Z) not in list and q[0]-Z >= 37.5 and q[1]-Z >= 37.5:
			x = q[0]-Z
			y = q[1]-Z
			break
		if check_rldiag(q[0],q[1],Z,otherlist) == 4 and (q[0]+4*Z,q[1]+4*Z) not in list and q[0]+4*Z <= 262.5 and q[1]+4*Z <= 262.5:
			x = q[0]+4*Z
			y = q[1]+4*Z
			break
			

	while ((x,y) in blackmoveslist or (x,y) in whitemoveslist):
		####Make sure to update the two blocks below to include diagonol cases
		####Include cases in the 3-1 for when the final stone is in the 3 and not the 1

	
		#makes sure to fill spaces of xx-xx setups because the x-x checker has lower priority than -xxx-
		#setups which might cause it to miss blocking this type of win condition
		if check_vert(x,y,Z,list) == 2 and (x,y+Z) not in otherlist and (check_vert(x,y+2*Z,Z,list) == 2 or check_vert(x,y+3*Z,Z,list) == 2):
			y += Z
		elif check_hor(x,y,Z,list) == 2 and (x+Z,y) not in otherlist and (check_hor(x+2*Z,y,Z,list) == 2 or check_hor(x+3*Z,y,Z,list) == 2):
			x += Z
		elif check_vert(x,y,Z,list) == 2 and (x,y-Z) not in list and (x,y-Z) not in otherlist and (check_vert(x,y-2*Z,Z,list) == 2 or check_vert(x,y-3*Z,Z,list) == 2):
			y -= Z
		elif check_hor(x,y,Z,list) == 2 and (x-Z,y) not in list and (x-Z,y) not in otherlist and (check_hor(x-2*Z,y,Z,list) == 2 or check_hor(x-3*Z,y,Z,list) == 2):
			x -= Z
		
		#Fills x-xxx or xxx-x spaces for same reason as above lines
		elif check_vert(x,y,Z,list) == 1 and  (x,y+Z) not in otherlist and check_vert(x,y+2*Z,Z,list) == 3:
			y+= Z
		elif check_vert(x,y,Z,list) == 1 and  (x,y-Z) not in otherlist and check_vert(x,y-2*Z,Z,list) == 3:
			y-= Z
		elif check_hor(x,y,Z,list) == 1 and  (x+Z,y) not in otherlist and check_hor(x+2*Z,y,Z,list) == 3:
			x+= Z
		elif check_hor(x,y,Z,list) == 1 and  (x-Z,y) not in otherlist and check_hor(x-2*Z,y,Z,list) == 3:
			x-= Z
			
		elif check_vert(x,y,Z,list) == 3 and  (x,y+Z) not in otherlist and (x,y+Z) not in list and (check_vert(x,y+2*Z,Z,list) == 1 or check_vert(x,y+3*Z,Z,list) == 1 or check_vert(x,y+4*Z,Z,list) == 1):
			y+= Z
		elif check_vert(x,y,Z,list) == 3 and  (x,y-Z) not in otherlist and (x,y-Z) not in list and (check_vert(x,y-2*Z,Z,list) == 1 or check_vert(x,y-3*Z,Z,list) == 1 or check_vert(x,y-4*Z,Z,list) == 1):
			y-= Z
		elif check_hor(x,y,Z,list) == 3 and  (x+Z,y) not in otherlist and  (x+Z,y) not in list and (check_vert(x+2*Z,y,Z,list) == 1 or check_vert(x+3*Z,y,Z,list) == 1 or check_vert(x+4*Z,y,Z,list) == 1):
			x+= Z
		elif check_hor(x,y,Z,list) == 3 and  (x-Z,y) not in otherlist and  (x-Z,y) not in list and (check_vert(x-2*Z,y,Z,list) == 1 or check_vert(x-3*Z,y,Z,list) == 1 or check_vert(x-4*Z,y,Z,list) == 1):
			x-= Z
		
		#Blocks stone sets of -xxxx- on the side that the -xxx- blocker is least likely to block
		elif check_hor(x,y,Z,list) == 4:
			switchdirections = False
			while ((x,y) in list or (x,y) in otherlist) and x >37.5 and switchdirections == False:
				x -= Z
				if (x,y) in otherlist:
					switchdirections = True
			while ((x,y) in list or (x,y) in otherlist) and x < 262.5:
				x += Z
			while ((x,y) in list or (x,y) in otherlist): 
				x = centerx(random.randint(26,275))
				y = centery(random.randint(26,275))
				
		elif check_vert(x,y,Z,list) == 4:
			switchdirections = False
			while ((x,y) in list or (x,y) in otherlist) and y > 37.5 and switchdirections == False:
				y -= Z
				if (x,y) in otherlist:
					switchdirections = True
			while ((x,y) in list or (x,y) in otherlist) and y < 262.5:
				y += Z
			while ((x,y) in list or (x,y) in otherlist):
				x = centerx(random.randint(26,275))
				y = centery(random.randint(26,275))
		
		elif check_lrdiag(x,y,Z,list) == 4:
			switchdirections = False
			while ((x,y) in list or (x,y) in otherlist) and x > 37.5 and y < 262.5 and switchdirections == False:
				x -= Z
				y += Z
				if (x,y) in otherlist:
					switchdirections = True
			while ((x,y) in list or (x,y) in otherlist) and x < 262.5 and y > 37.5:
				x += Z
				y -= Z
			while ((x,y) in list or (x,y) in otherlist):
				x = centerx(random.randint(26,275))
				y = centery(random.randint(26,275))
			
		elif check_rldiag(x,y,Z,list) == 4:
			switchdirections = False
			while ((x,y) in list or (x,y) in otherlist) and x > 37.5 and y > 37.5 and switchdirections == False:
				x -= Z
				y -= Z
				if (x,y) in otherlist:
					switchdirections = True
			while ((x,y) in list or (x,y) in otherlist) and x < 262.5 and y < 262.5:
				x += Z
				y += Z
			while ((x,y) in list or (x,y) in otherlist):
				x = centerx(random.randint(26,275))
				y = centery(random.randint(26,275))
			
		#Caps stone sets of -xxx- in all directions
		elif check_hor(x,y,Z,list) == 3:
			switchdirections = False
			while ((x,y) in list or (x,y) in otherlist) and x < 262.5 and switchdirections == False:
				x += Z
				if (x,y) in otherlist:
					switchdirections = True
			while ((x,y) in list or (x,y) in otherlist) and x > 37.5:
				x -= Z
			while ((x,y) in list or (x,y) in otherlist):
				x = centerx(random.randint(26,275))
				y = centery(random.randint(26,275))
		
		elif check_vert(x,y,Z,list) == 3:
			switchdirections = False
			while ((x,y) in list or (x,y) in otherlist)  and y < 262.5 and switchdirections == False:
				y += Z
				if (x,y) in otherlist:
					switchdirections = True
			while ((x,y) in list or (x,y) in otherlist)  and y > 37.5:
				y -= Z
			while ((x,y) in list or (x,y) in otherlist):
				x = centerx(random.randint(26,275))
				y = centery(random.randint(26,275))			
			
		elif check_lrdiag(x,y,Z,list) == 3:
			switchdirections = False
			while ((x,y) in otherlist or (x,y) in list) and x > 37.5 and y < 262.5 and switchdirections == False:
				x -= Z
				y += Z
				if (x,y) in otherlist:
					switchdirections = True
			while ((x,y) in list or (x,y) in otherlist) and x < 262.5 and y > 37.5:
				x += Z
				y -= Z
			while ((x,y) in list or (x,y) in otherlist):
				x = centerx(random.randint(26,275))
				y = centery(random.randint(26,275))			
			
		
		elif check_rldiag(x,y,Z,list) == 3:
			switchdirections = False
			while ((x,y) in list or (x,y) in otherlist) and x < 262.5 and y < 262.5 and switchdirections == False:
				x += Z
				y += Z
				if (x,y) in otherlist:
					switchdirections = True
			while (x,y) in list and x > 37.5 and y > 37.5:
				x -= Z
				y -= Z
			while ((x,y) in list or (x,y) in otherlist):
				x = centerx(random.randint(26,275))
				y = centery(random.randint(26,275))
		
		
		#Checks for cases x-x in all directions and blocks in the center
		elif (x,y) in list and (x+2*Z,y) in list and (x+Z,y) not in list and (x+Z,y) not in otherlist:
			x = x+Z
		elif (x,y) in list and (x-2*Z,y) in list and (x-Z,y) not in list and (x-Z,y) not in otherlist:
			x = x-Z
		elif (x,y) in list and (x,y-2*Z) in list and (x,y-Z) not in list and (x,y-Z) not in otherlist:
			y = y-Z
		elif (x,y) in list and (x,y+2*Z) in list and (x,y+Z) not in list and (x,y+Z) not in otherlist:
			y = y+Z
		elif (x,y) in list and (x+2*Z,y+2*Z) in list and (x+Z,y+Z) not in list and (x+Z,y+Z) not in otherlist:
			x = x+Z
			y = y+Z
		elif (x,y) in list and (x+2*Z,y-2*Z) in list and (x+Z,y-Z) not in list and (x+Z,y-Z) not in otherlist:
			x = x+Z
			y = y-Z
		elif (x,y) in list and (x-2*Z,y+2*Z) in  list and (x-Z,y+Z) not in list and (x-Z,y+Z) not in otherlist:
			x = x-Z
			y = y+Z
		elif (x,y) in list and (x-2*Z,y-2*Z) in list and (x-Z,y-Z) not in list and (x-Z,y-Z) not in otherlist:
			x = x-Z
			y = y-Z
		
		#Caps stone sets of -xx- in all directions
		elif check_hor(x,y,Z,list) == 2:
			switchdirections = False
			while ((x,y) in list or (x,y) in otherlist) and x < 262.5 and switchdirections == False:
				x += Z
				if (x,y) in otherlist:
					switchdirections = True
			while ((x,y) in list or (x,y) in otherlist) and x > 37.5:
				x -= Z
			while ((x,y) in list or (x,y) in otherlist):
				x = centerx(random.randint(26,275))
				y = centery(random.randint(26,275))
		
		elif check_vert(x,y,Z,list) == 2:
			switchdirections = False
			while ((x,y) in list or (x,y) in otherlist) and y < 262.5 and switchdirections == False:
				y += Z
				if (x,y) in otherlist:
					switchdirections = True
			while ((x,y) in list or (x,y) in otherlist) and y > 37.5:
				y -= Z
			while ((x,y) in list or (x,y) in otherlist):
				x = centerx(random.randint(26,275))
				y = centery(random.randint(26,275))			
			
		elif check_lrdiag(x,y,Z,list) == 2:
			switchdirections = False
			while ((x,y) in list or (x,y) in otherlist) and x > 37.5 and y < 37.5 and switchdirections == False:
				x -= Z
				y += Z
				if (x,y) in otherlist:
					switchdirections = True
			while ((x,y) in list or (x,y) in otherlist) and x < 262.5 and y > 37.5:
				x += Z
				y -= Z
			while ((x,y) in list or (x,y) in otherlist):
				x = centerx(random.randint(26,275))
				y = centery(random.randint(26,275))			
			
		
		elif check_rldiag(x,y,Z,list) == 2:
			switchdirections = False
			while ((x,y) in list or (x,y) in otherlist) and x < 262.5 and y < 262.5 and switchdirections == False:
				x += Z
				y += Z
				if (x,y) in otherlist:
					switchdirections = True
			while ((x,y) in list or (x,y) in otherlist) and x > 37.5 and y > 37.5:
				x -= Z
				y -= Z
			while ((x,y) in list or (x,y) in otherlist):
				x = centerx(random.randint(26,275))
				y = centery(random.randint(26,275))			
			

				
		else:
			x = random.randint(26,275)
			y = random.randint(26,275)
			x = centerx(x)
			y = centery(y)
	return placestone(x,y,window)

#Creates two turtles to draw the gameboard
def drawboard():
	turtle.tracer(0)
	#change the background colour into burlywood
	turtle.bgcolor("burlywood2")
	
	#create/set up the turtles
	boardmaker = turtle.Turtle()
	boardmaker.ht()
	boardmaker.up()
	boardmaker.goto(const.turtlestart)
	boardmaker.down()
	boardmaker.speed(const.turtspeed)
	boardmaker.pensize(5)

	#draw the perimeter of the gameboard draws an L shape twice to make a square
	for i in range(4):
			boardmaker.forward(const.boardlength)
			boardmaker.left(const.ninety)

	#draw the lines in the gameboard
	boardmaker.pensize(3)
	for i in range(const.cellsperrow):
			boardmaker.forward(const.cellsize)
			boardmaker.left(const.ninety)
			boardmaker.forward(const.boardlength)
			boardmaker.backward(const.boardlength)
			boardmaker.right(const.ninety)
	boardmaker.backward(const.boardlength)
	boardmaker.left(const.ninety)
	for i in range(const.cellspercolumn):
			boardmaker.forward(const.cellsize)
			boardmaker.right(const.ninety)
			boardmaker.forward(const.boardlength)
			boardmaker.backward(const.boardlength)
			boardmaker.left(const.ninety)
	boardmaker.up()
	#name the columns
	columnname=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	for writecolumnname in range(const.cellspercolumn):
			boardmaker.goto(const.cellsize*(writecolumnname+1)+const.cellsize/2  ,  const.boardlength+const.cellsize+const.buffer)
			boardmaker.write( columnname[writecolumnname], align="center", font=("Arial",16,"bold"))

	#name the rows
	for writerowname in range(const.cellsperrow):
			boardmaker.goto(const.cellsize/2  ,  const.boardlength-const.cellsize*(writerowname))
			boardmaker.write( 1+writerowname, align="center", font=("Arial",16,"bold"))
	boardmaker.goto(100,4)
	boardmaker.write("Save Game", font=('Arial',16,'bold'))
	boardmaker.goto(170,4)
	boardmaker.write("Load Game", font=('Arial',16,'bold'))
	boardmaker.goto(240,4)
	boardmaker.write("New Game", font=('Arial',16,'bold'))
	turtle.update()

#Can call load/save/new game/placestone and aimove depending on where user clicks
def onclick(x,y):	
	#Prevents any clicks outside of the board from placing a stone (currently the positioning for save, load, and newboard)
	if x > 100 and x < 150 and y < 17 and y > 2:
		return savefile()
	if x > 170 and x < 220 and y < 17 and y > 2:
		STONETURT.clear()
		clearmovelists()
		return loadfile()
	if x > 240 and x < 290 and y < 17 and y > 2:
		return main(x,y)
		
	if y > const.cellsize + const.boardlength:
		return
	if y < const.cellsize:
		return
	if x < const.cellsize:
		return
	if x > const.cellsize + const.boardlength:
		return
		
	#Checks x,y click coordinates and centers them for stone placement (range 10 in order to check each of 10 rows/columns)
	x = centerx(x)
	y = centery(y)
	
	#Does nothing if a move has already been played so stones can't be played on top of stones
	if ((x,y)) in blackmoveslist or ((x,y)) in whitemoveslist:
		return
	

	list = whitemoveslist
	otherlist = blackmoveslist
	if movecounter()%2 == 0:
		list = blackmoveslist
		otherlist = whitemoveslist
	window = turtle.Screen()
	
	if placestone(x,y,window):
		return
	else:
		aimove(x,y,const.cellsize,list,otherlist,window)

#Takes an x coordinate and centers it to a board cell space
def centerx(x):
	x = const.stoneplacement+(x//const.cellsize)*const.cellsize
	return x

#Takes a y coordinate and center it to a board cell space	
def centery(y):
	y = const.stoneplacement+(y//const.cellsize)*const.cellsize
	return y

#Takes given coordinate and places a stone there, updating the gamestate list
def placestone(x,y,window):
	turtle.tracer(0)
	move = movecounter()
	if move%2 == 0:
		#Places a black stone and updates movelists
		STONETURT.goto(x,y)
		STONETURT.dot(const.stonesize,"black")
		movelist[0].append((x,y))
		blackmoveslist.sort()
		STONETURT.up()
		
	else:
		#Places a white stone and updates movelists
		STONETURT.goto(x,y)
		STONETURT.dot(const.stonesize, "white")
		movelist[1].append((x,y))
		whitemoveslist.sort()
		STONETURT.up()
	turtle.update()
	time.sleep(0.15)
	if wincondition(x,y,const.cellsize,blackmoveslist,window) or wincondition(x,y,const.cellsize,whitemoveslist,window):
		return True
	else:
		return False
		

#Counts the total length of each moves list together to determine how many turns have passed
def movecounter():
	return len(blackmoveslist)+len(whitemoveslist)

#Saves the gamestate list to a text file
def savefile():
	#Writes the current black and white moves lists to their respective save files
	savefile = open("C:/Users/Hayden/Downloads/GomokuSaveFiles/gomokusave.txt", 'w')
	savefile.write(str(movelist))
	savefile.close()
	return

	
#Opens the saved gamestate file and sets up the board/gamestate list to reflect the save file
def loadfile():
	savefile = open("C:/Users/Hayden/Downloads/GomokuSaveFiles/gomokusave.txt", 'r')
	savefile = savefile.read()
	#find explanation for ast.literal_eval
	savefile = ast.literal_eval(savefile)
	

	#Prints each of the moves read from the save file and updates the current move lists
	for x,y in savefile[0]:
		STONETURT.goto(x,y)
		STONETURT.dot(const.stonesize,"black")
		blackmoveslist.insert (0,(x,y))
	#whitemoves
	for x,y in savefile[1]:
		STONETURT.goto(x,y)
		STONETURT.dot(const.stonesize,"white")
		whitemoveslist.insert (0,(x,y))

	return
		

def main(x,y):
	clearmovelists()
	STONETURT.clear()
	STONETURT.down()
	
	#creates a fresh turtle graphics window in which a new game will be played
	window = turtle.Screen()
	window.clear()
	window.setworldcoordinates(const.windowstartxy, const.windowstartxy, const.windowendxy, const.windowendxy)

	drawboard()
	
	whofirst = random.randint(0,1)
	if whofirst == 0:
		aimove(x,y,const.cellsize,blackmoveslist,whitemoveslist,window)
	
	
	#Sets up the ability of the user to click on the board and place stones
	window.onclick(onclick)
	
	window.mainloop()

#Z is the constant const.cellsize. Used for the sake of reducing line length
def wincondition(x,y,Z,list,window):
	if movecounter() % 2 == 0:
		winner = 'White'
	else:
		winner = "Black"
	winstate = False
	if check_hor(x,y,Z,list) == 5:
		print(winner,"wins. Click anywhere to start a new game")
		winstate = True
		window.onclick(main)
	if check_vert(x,y,Z,list) == 5:
		print(winner,"wins. Click anywhere to start a new game")
		winstate = True
		window.onclick(main)
	if check_lrdiag(x,y,Z,list) == 5:
		print(winner,"wins. Click anywhere to start a new game")
		winstate = True
		window.onclick(main)
	if check_rldiag(x,y,Z,list) == 5:
		print(winner,"wins. Click anywhere to start a new game")
		winstate = True
		window.onclick(main)
	if movecounter() == 100:
		print("The game ends in a tie. Click anywhere to start a new game")
		winstate = True
		window.onclick(main)
	return winstate
	

def check_hor(x,y,Z,list):
	counter = 0
	while (x,y) in list:
		x -= Z
	x = x + Z
	while (x,y) in list:
		counter += 1
		x += Z
	return counter

def check_vert(x,y,Z,list):
	counter = 0
	while (x,y) in list:
		y -= Z
	y = y + Z
	while (x,y) in list:
		counter += 1
		y += Z
	return counter
		
def check_lrdiag(x,y,Z,list):
	counter = 0
	while (x,y) in list:
		y -= Z
		x += Z
	y += Z
	x -= Z
	while (x,y) in list:
		counter += 1
		y += Z
		x -= Z
	return counter
		
def check_rldiag(x,y,Z,list):
	counter = 0
	while (x,y) in list:
		y -= Z
		x -= Z
	y += Z
	x += Z
	while (x,y) in list:
		counter += 1
		y += Z
		x += Z
	return counter



def clearmovelists():
	global blackmoveslist
	global whitemoveslist
	global movelist
	blackmoveslist = []
	whitemoveslist = []
	movelist = []
	movelist.append(blackmoveslist)
	movelist.append(whitemoveslist)

main(137.5,137.5)
