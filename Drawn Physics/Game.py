from imp import C_EXTENSION
from cmu_112_graphics import *
import tkinter
import sys
import math
import time
import pygame



##################CITATIONS#################
#Overall game inspired by http://www.crayonphysics.com/
#initImages idea from Winston Zha TP images mini lecture
#mouse events from https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#events
#This project relies on cmu112 graphics, ideas within project overall inspired from https://www.cs.cmu.edu/~112/schedule.html
#star image from https://www.mobygames.com/game/android/crayon-physics-deluxe_
#background image and homescreen image from http://www.crayonphysics.com/
#crayon image from http://www.crayonphysics.com/
#line intersection inspired by circles intersect inspired by https://www.kosbie.net/cmu/spring-20/15-112/notes/writing-session1.html
# and  https://www.geeksforgeeks.org/check-line-touches-intersects-circle/ and https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
# and https://doubleroot.in/lessons/circle/intersection-line-circle-1/#:~:text=if%20the%20distance%20is%20less,lie%20completely%20outside%20the%20circle.
#General equation of a line(unused) inspired by https://www.mathsisfun.com/algebra/line-equation-general-form.html
#Modes inspired by https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#usingModes
#Time usage inspired by https://www.cs.cmu.edu/~112/notes/notes-efficiency.html
#Sound directly from https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#playingSoundsWithPygame
#Pygame is used for sound
#Song from https://www.youtube.com/watch?v=acEYrld-9sQ
################## CITATIONS CLOSED##########

############### MAIN APP STARTED #################
def appStarted(app):
    pygame.mixer.init()
    app.sound = Sound("GLullaby.mp3")
    app.sound.start()
    app.mode = "homeScreenMode"
    app.gravity = True
    app.move = False
    app.gameOver = False
    ###Locations###
    app.mouseMovedLocation = ()
    app.mouseDraggedLocation = ()
    app.mousePressedLocation = ()
    app.moved = True
    ###Levels###
    app.level = 1
    initImages(app)
    ###Star###
    app.starPosition = []
    app.starCount = 0
    app.levelLinesColor = "Green"
    app.ballColor = "Red"
    #Ball###
    app.ballR = app.width/65
        
    app.ballStart = [app.width/7.5, app.height/2.57]
    app.starPosition = [app.width/1.3, app.height/2.2]
    app.ball = Ball(app.ballStart[0],app.ballStart[1],.01,0,0)
   
    app.timePassed = 0
    # app.ballR = app.width/65
    #Lines#
    app.lineColor = "blue"
    app.mousePresses = ()
    app.mouseReleases = ()
    # app.linesDrawn = []
    app.levelLines = []
    app.lineList = []
    app.linesTouched = []
    app.allLinesTouched = []
    app.currLinesTouched = []
    app.x, app.y = 0, 0
    app.ballR = app.width/65
   
    # app.timerDelay = 500
    #LEVEL CHANGING#
    app.levelTwo = False
    app.levelThree = False
    app.levelList = []
    app.friction = False
    app.fRepresent = 'On'
    app.timeg1 = 0
    app.timeg2 = 0
    app.gTimeDiff = 0
    app.time1 = 0
    app.time2 = 0

    app.velocity1 = 0 
    app.velocity2 = 0
    app.touching = "Yes"
    app.n = False
    app.timeDiff = 0
    app.pressed = []
    app.endScreen = []
    app.velocity = 0
def updateStarts(app):
    if app.level == 1:
        # app.ballPosition = (app.width/7.5, app.height/2.57)
        app.ballStart = [app.width/7.5, app.height/2.57]
        app.starPosition = [app.width/1.3, app.height/2.2]
    elif app.level == 2:
        app.starPosition = [app.width/1.5, app.height/8.5 - app.ballR - 4]
        app.ball.cx, app.ball.cy = app.width/6.3, app.height/8.5 - app.ballR
##################CLOSED#####################

###############INIT IMAGES###############
def initImages(app):
    crayon = "crayon.png"
    gameStar = "star.png"
    scoreStar = "star.png"
    firstHomeBg = "backbackImage.png"
    homeBackGround = "homeBackGround.png"
    background = "background.png"
    app.backgroundImage = app.loadImage(background)
    app.backgroundImage = ImageTk.PhotoImage(app.scaleImage(app.backgroundImage, 1))
    #star for socre in top left
    app.scoreStarImage = app.loadImage(scoreStar)
    app.scoreStarImage = ImageTk.PhotoImage(app.scaleImage(app.scoreStarImage, 1/10))
    #star for actual game
    app.starImage = app.loadImage(gameStar)
    app.starImage = ImageTk.PhotoImage(app.scaleImage(app.starImage, 1/7))
    # app.starImage2 = app.loadImage(gameStar)
    # app.starImage2 = ImageTk.PhotoImage(app.scaleImage(app.starImage, 1/5))
    #crayon image
    app.crayonImage = app.loadImage(crayon)
    app.crayonImage = ImageTk.PhotoImage(app.scaleImage(app.crayonImage, 1/5))

    app.homeBackGroundImage = app.loadImage(homeBackGround)
    app.homeBackGroundImage = ImageTk.PhotoImage(app.scaleImage(app.homeBackGroundImage, 1.3))
    

##################CLOSED#####################

##########################################
# HOME SCREEN MODE 
##########################################
def homeScreenMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    canvas.create_image(app.width/2, app.height/2, image = app.backgroundImage)
    canvas.create_image(app.width/2, app.height/2, image = app.homeBackGroundImage)
    canvas.create_text(app.width/2, 50, text='Welcome to Drawn Physics!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 100, text='A remake of the game crayon physics!',
                       font='Arial 22 bold', fill='black')
    canvas.create_text(app.width/2, 175, text='Press any key for the game!',
                       font=font, fill='black')

def homeScreenMode_keyPressed(app, event):
    app.mode = 'previewScreenMode'

# ##########################################
# # PREVIEW SCREEN MODE 
# ##########################################
def previewScreenMode_redrawAll(app, canvas):
    font = 'Arial 30'
    font1 = 'Arial 40 bold'
    font2 = 'Arial 16'
    font3 = 'Arial 14'
    font4 = 'Arial 17'
    backGround(app, canvas)
    score(app, canvas)
    scoreStar(app, canvas)
    drawStar(app, canvas)
    drawBall(app, canvas)
    levelOneTerrain(app, canvas)
    # canvas.create_text(app.width/2, 70, text = "Hi, before you get started here are some things to know!",
    #                    font=font, fill='coral2')
    canvas.create_text(app.width/2, app.height/2 - 370 , text = "Preview Mode!",
                       font=font1, fill='black')
    canvas.create_text(app.width/2, app.height/2 - 330 , text = "What you see is a preview of the level you are about to play!",
                       font= "Arial 20 bold", fill='black')
    canvas.create_rectangle(app.width/2- 370, app.height/2 - 315, app.width/2 + 360, app.height/2 -50, outline = "Red")
    canvas.create_text(app.width/2, 130, text = "The objective is to draw a line that the ball can follow into the star. How you may ask? That is to follow!",
                       font=font2, fill='black')
    canvas.create_text(app.width/2, 165 , text = "1.You may press 'f' to turn the balls friction off and press 's' to stop or pause the game.",
                       font=font2, fill='black')
    canvas.create_text(app.width/2-10, 190, text = "2.Pressing 'p' will change the ball's color to Pink, 'y' to yellow, and 'g' to gray.", font=font3, fill='black')
    canvas.create_text(app.width/2-10, 215, text = "3. Only in level 2 will each color alter the balls speed in a different way which is for you to find out!", font=font3, fill='black')
    canvas.create_text(app.width/2-10, 240, text = "4.You may press 'r' at any time to restart!", font=font3, fill='black')
    canvas.create_text(app.width/2-10, 265, text = "5.You may press 'h' at any time to go to a helper screen to understand the keystrokes and line drawing!", font=font3, fill='black')
    canvas.create_text(app.width/2-10, 290, text = "6.Skip to level 2 with 'n'. Each level has helpful instructions you should follow before starting!", font=font3, fill='black')
    canvas.create_text(app.width/2-10, 315, text = "7.More instructions on how to actually play to follow in the actual game!", font=font3, fill='black')
    canvas.create_text(app.width/2, 355, text = "Once you have read everything carefully, please press 'c' to continue!",
                       font=font4, fill='black')
def previewScreenMode_keyPressed(app, event):
    if event.key == "c":
        app.mode = "gameMode"
        

##########################################
# HELPER SCREEN MODE
##########################################
def helperMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    canvas.create_image(app.width/2, app.height/2, image = app.backgroundImage)
    canvas.create_rectangle(app.width/2-200, app.height/2 - 290, app.width/2 + 200, app.height/2 + 300 )
    canvas.create_image(app.width/2, app.height/2-250, image = app.starImage)
    canvas.create_text(app.width/2, 75, text='Helper Mode!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 120, text='(You may press any key to return to the game)',
                       font='Arial 16 bold', fill='black')
    canvas.create_text(app.width/2, 250, text='Level 1 Keystroke features:',
                       font='Arial 15 bold', fill='black')
    canvas.create_text(app.width/2, 270, text="1. 's' freezes the game(press 'm' to move it again)",
                       font='Arial 15 bold', fill='black')
    canvas.create_text(app.width/2, 290, text="2. 'n' skips the level",
                       font='Arial 15 bold', fill='black')
    canvas.create_text(app.width/2, 310, text="3. 'f' turns friction off",
                       font='Arial 15 bold', fill='black')
    canvas.create_text(app.width/2, 330, text="4. 'm' moves the ball",
                       font='Arial 15 bold', fill='black')
    canvas.create_text(app.width/2, 350, text="5. 'p', 'g', and 'y' change balls color",
                       font='Arial 15 bold', fill='black')
    canvas.create_text(app.width/2, 370, text="(Though this will not alter the balls speed for this level.)",
                       font='Arial 14 bold', fill='black')
    canvas.create_text(app.width/2, 410, text="Level 2 Keystroke features:",
                       font='Arial 15 bold', fill='black')
    canvas.create_text(app.width/2, 430, text="1. 'm' moves the ball",
                       font='Arial 15 bold', fill='black')
    canvas.create_text(app.width/2, 450, text="2. 'p', 'g', and 'y' change balls color",
                       font='Arial 15 bold', fill='black')
    canvas.create_text(app.width/2, 470, text="And in this level the balls speed accordingly",
                       font='Arial 14 bold', fill='black')
    canvas.create_text(app.width/2, 510, text="Both levels Mouse Usage:",
                        font='Arial 15 bold', fill='black')
    canvas.create_text(app.width/2, 530, text="1.Click down with your mouse to start a line",
                        font='Arial 14 bold', fill='black')
    canvas.create_text(app.width/2, 550, text="2.Drag to draw the line out",
                        font='Arial 14 bold', fill='black')
    canvas.create_text(app.width/2, 570, text="3.Release to place the line",
                        font='Arial 14 bold', fill='black')
def helperMode_keyPressed(app, event):
    app.mode = "gameMode"
    
    
  

    
   
# ##########################################


##########################################
# END SCREEN MODE 
##########################################
def endScreenMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    message1 = "Great job, you seem to be an expert!"
    message2 = "Not bad, but can you go faster next time?"
    message3 = "Alright, this game is not that hard you can win faster than this!"
    canvas.create_image(app.width/2, app.height/2, image = app.backgroundImage)
    canvas.create_rectangle(app.width/2-200, app.height/2 - 200, app.width/2 + 200, app.height/2 + 200 )
    canvas.create_image(app.width/2, app.height/2-100, image = app.starImage)
    if app.timeDiff <= 20:
        finalMessage = message1
    elif app.timeDiff <= 60:
        finalMessage = message2
    else:
        finalMessage = message3

    canvas.create_text(app.width/2, 150, text=f'{finalMessage} It took you {app.timeDiff} seconds and your final score was {app.starCount}!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 400, text="Please press 'r' to play again!",
                       font=font, fill='black')
    
def endScreenMode_keyPressed(app, event):
    if event.key == "r":
        appStarted(app)

def endScreenMode_timerFired(app):
    if len(app.endScreen) == 0:
        app.time2 = time.time()
        app.timeDiff = round(app.time2-app.time1,2)

    app.endScreen.append(1)

  
##########################################
# GAME MODE 
##########################################
class Sound(object):
    def __init__(self, path):
        self.path = path
        self.loops = -1
        pygame.mixer.music.load(path)

    # Returns True if the sound is currently playing
    def isPlaying(self):
        return bool(pygame.mixer.music.get_busy())

    # Loops = number of times to loop the sound.
    # If loops = 1 or 1, play it once.
    # If loops > 1, play it loops + 1 times.
    # If loops = -1, loop forever.
    def start(self, loops=-1):
        self.loops = loops
        pygame.mixer.music.play(loops=loops)

    # Stops the current sound from playing
    def stop(self):
        pygame.mixer.music.stop()




###############LINE CLASS ###############
class Line(object):
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1= y1
    def generalForm(self):
        slope = (self.y1 - self.y0)/(self.x1-self.x0)
        yInt = self.y0
        yVal = slope + yInt
        if slope % 1 != 0 and slope > 1: 
            roundedSlope = -1 *(round(slope , 5))
            yInt *= -1 
            divisor = roundedSlope * -1
            yVal /= divisor
            roundedSlope /= divisor
            yInt /= divisor
            return (roundedSlope, yVal, yInt)
        elif slope % 1 != 0 and slope < 1:
            roundSlope = -1*(round(slope ,5))
            yInt *= -1
            multiplier = 100000
            yVal *= multiplier
            roundSlope *= multiplier
            yInt *= multiplier
            return(roundSlope, yVal, yInt)
    def slopeInterceptForm(self):
        #1. slope multiply by self.x0
        #2. either add or subtract from y0
        # this is to offset int back to where it should be
        a = self.y1-self.y0
        b = self.x1-self.x0
        if b == 0:
            b = .00001
        # if a == 0: a = .1
        # else: b == 0
        # if self.y1 != self.y0 or self.x0 != self.x1 and a != 0 and b != 0:
        # b = .1
        m = round((a)/(b), 7)
        one = m * self.x0
        two = self.y0 - one
        k = two
        x = 1
        y = m*x + k
        return (m, y, k)
    
##################CLOSED#####################

######LINE  FUNCTIONS######
def slopeInterceptForm2(app, line):
        #1. slope multiply by self.x0
        #2. either add or subtract from y0
        # this is to offset int back to where it should be
        a = line[3]-line[1]
        b = line[2]-line[0]
        if b == 0:
            b = .00001
        # if a == 0: a = .1
        # else: b == 0
        # if self.y1 != self.y0 or self.x0 != self.x1 and a != 0 and b != 0:
        # b = .1
        m = round((a)/(b), 7)
        one = m * line[0]
        two = line[1] - one
        k = two
        x = 1
        y = m*x + k
        return (m, y, k)
def createLines(app):
    line = Line(app.mousePresses[0], app.mousePresses[1], app.mouseReleases[0], app.mouseReleases[1])
    app.lineList.append(line)

def drawCrayonLines(app, canvas):
    if len(app.mouseDraggedLocation) >= 1 and len(app.mousePressedLocation) >= 1: 
        x0 = app.mousePressedLocation[0]
        y0 = app.mousePressedLocation[1]
        x1 = app.mouseDraggedLocation[0]
        y1 = app.mouseDraggedLocation[1]
        canvas.create_line(x0, y0, x1, y1, fill = app.lineColor)
    if len(app.lineList) >= 1:
        for line in app.lineList:
            canvas.create_line(line.x0, line.y0, line.x1, line.y1, fill = app.lineColor)
def updateLines(app):
    if app.gameOver:
        app.lineList = []
        app.levelLines = []
        app.linesTouched = []
        app.allLinesTouched = []
        app.currLinesTouched = []
    pass

################## LINE FUNCTIONS CLOSED#####################
 


###############BALL CLASS ###############
class Ball(object):
    def __init__(self, cx, cy, vx, vy, mass):
        self.cx = cx
        self.cy = cy
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.r = round(23.0769230769, 7)
    #one method tell the abll to move forward

    def isIntersecting(self, app,  line2): #line2 = (-100, -101, -99, -100 )
        extra = 10
        objectExtra = 1.5
        radius = self.r + objectExtra #for my purposes it does not need to exactly touch
        circleBottom = self.cy + self.r
        circleRightSide = self.cx + self.r
        circleLeftSide = self.cx - self.r
        for line in app.levelLines:
            line2 = line
    
            x0, y0, x1, y1 = line2[0], line2[1], line2[2], line2[3]
            if y0 == y1 and y0 + extra >= circleBottom >= y0 - extra and x0<= self.cx <= x1: #check for horizontal lines
                if (x0,  y0, x1, y1) not in app.linesTouched:
                    app.linesTouched.append((x0,  y0, x1, y1))
                if (x0,  y0, x1, y1) not in app.allLinesTouched:
                    app.allLinesTouched.append((x0,  y0, x1, y1))
                return True
            elif x0 == x1 and x0 + extra >= circleRightSide >= x0 - extra and y0 <= self.cy <= y1: #checks if right side touches line
                if (x0,  y0, x1, y1) not in app.linesTouched:
                    app.linesTouched.append((x0,  y0, x1, y1))
                if (x0,  y0, x1, y1) not in app.allLinesTouched:
                    app.allLinesTouched.append((x0,  y0, x1, y1))
                return True
            elif x0 == x1 and x0 - extra <= circleLeftSide <= x0 + extra and y0 <= self.cy <= y1: #checks if left side touches line
                if (x0,  y0, x1, y1) not in app.linesTouched:
                    app.linesTouched.append((x0,  y0, x1, y1))
                if (x0,  y0, x1, y1) not in app.allLinesTouched:
                    app.allLinesTouched.append((x0,  y0, x1, y1))
                return True
        for line in app.lineList:
            line2 = line
            interceptVals = line2.slopeInterceptForm()
            m = interceptVals[0]
            y = interceptVals[1]
            k = interceptVals[2]
            x0 = self.cx
            y0 = self.cy
            distance = abs(k+(m * x0)- y0) / math.sqrt(1 + m**2)
            leftSide = self.cx - self.r
            rightSide = self.cx + self.r
            # top = self.cy - self.r
            # bottom = self.cy + self.r
            if (distance == radius or radius > distance) and (line.x0 <= rightSide <= line.x1 or line.x0 <= leftSide <= line.x1)  or (distance == radius or radius > distance) and line.y0 <= self.cy + self.r <= line.y1:
                if (line.x0, line.y0, line.x1, line.y1) not in app.linesTouched:
                    app.linesTouched.append((line.x0, line.y0, line.x1, line.y1))
                if (line.x0, line.y0, line.x1, line.y1) not in app.allLinesTouched:
                    app.allLinesTouched.append((line.x0, line.y0, line.x1, line.y1))
                return True
        return False
    
    def getDistance(self, app, line2):
        if len(app.linesTouched) >= 1:
            line2 = app.linesTouched[-1]
            interceptVals = slopeInterceptForm2(app, line2)
            m = interceptVals[0]
            y = interceptVals[1]
            k = interceptVals[2]
            x0 = self.cx
            y0 = self.cy
            distance = abs(k+(m * x0)- y0) / math.sqrt(1 + m**2)
            return distance
   
    def updateBallPosition(self, app):
        line = []
        startTime = 0
        if app.level == 2:
            x0, x1 = app.linesTouched[-1][0] , app.linesTouched[-1][2]
            xDiff = x1- x0
            if (xDiff) == 0: #stops divide by zero error
                xDiff = .00000001
            dx = .05 + self.vx
            self.cx += dx 


        elif self.isIntersecting(app, line) and len(app.linesTouched) >= 1:
            y0, y1 = app.linesTouched[-1][1] , app.linesTouched[-1][3]
            x0, x1 = app.linesTouched[-1][0] , app.linesTouched[-1][2]
            xDiff = x1- x0
            yDiff = y1-y0
            if (xDiff) == 0: #stops divide by zero error
                xDiff = .00000001
            slope = (yDiff) / (xDiff)
            dy, dx = (yDiff)/600 + self.vy, .05 + self.vx
            if y1 == y0: #not in app.levelLines: #if it is  horizontal line drawn by user #change this for friction
                # self.cy += y0-self.r-slope
                self.cx += dx 
                if  not app.friction:
                    self.cx += dx
#SWITCH OFFSET TO SLOPE?
            if x0 == x1:
                self.cx = x0 - self.r
                self.cy += 3**2
            elif slope != 0:
                # ("Slanted Line")
                #("dx", dx, "dy", dy)
                self.cx += self.r + slope + dx
                self.cy += dy
            # if (round(y0,2) != round(y1,2)) and self.isIntersecting(app, line) and (x0 >= self.cx + self.r or x1 >= self.r + self.cx): # x0 >= self.cx + self.r or x1 >= self.r + self.cx:
            #     if self.isIntersecting(app, line):
            #         if len(app.allLinesTouched) > 2:
            #             newX0, newX1, newY0, newY1 = app.allLinesTouched[-2][0], app.allLinesTouched[-2][2], app.allLinesTouched[-2][1], app.allLinesTouched[-2][3]
            #             slope2 = (app.allLinesTouched[-2][3] - app.allLinesTouched[-2][1]) - (app.allLinesTouched[-2][2] - app.allLinesTouched[-2][0])
            #             if slope2 != slope and (newX0, newX1, newY0, newY1) not in app.levelLines and app.linesTouched[-1] not in app.levelLines:
                            
            #                 # self.cx += self.vx * -5 + dx * -1
            #     
            #             pass
            if len(app.linesTouched) >= 1:
                line4 = app.linesTouched[-1]
                if (self.getDistance(app, line4) < self.r-1) and line4 not in app.levelLines:
                    app.move = False


        else:
            acceleration = 1
            decreaser = .75
            if app.gTimeDiff > 1:
                acceleration += 1
                acceleration **= 2
                if app.gTimeDiff > 2:
                    acceleration **= 1.2
                    decreaser = 4

            x0, x1 = app.allLinesTouched[-1][0] , app.allLinesTouched[-1][2]
            xDiff = x1- x0
            y0, y1 = app.allLinesTouched[-1][1] , app.allLinesTouched[-1][3]
            yDiff = y1-y0
            if (xDiff) == 0: #stops divide by zero error
                xDiff = .00000001
            slope = (yDiff) / (xDiff)
            dy, dx = (yDiff)/100,  (xDiff)/10000
            self.cx += 5 - decreaser
            self.cy += 3 * acceleration
            if self.isIntersecting(app, line) and app.friction:
                self.cx += self.r + slope + dx
                self.cy += dy
  

     
    def gravtiy(self):
        return 9.8
    def potentialEnergy(self):
        return self.mass * self.cy * self.gravtiy()
    
    
    def checkGameOver(self, app):
        starCx = round(app.starPosition[0], 0)
        starCy = round(app.starPosition[1], 0)
        leftStar = round(app.starPosition[0] - self.r, 0) 
        rightStar = round(app.starPosition[0] + self.r, 0)
        topStar = round(app.starPosition[1] - self.r, 0)
        bottomStar = round(app.starPosition[1] + self.r, 0)
        rightBall = round(self.cx + self.r, 0)
        leftBall = round(self.cx - self.r, 0)
        topBall = round(self.cy - self.r, 0)
        bottomBall = round(self.cy + self.r, 0)
        if rightBall >= leftStar and (starCy <= self.cy <= starCy + 30 or starCy <= self.cy <= starCy -30): # or app.n: #checks if right side of ball is in or touching star
            app.gameOver = True
            if app.level == 1:
                app.lineList = []
                app.levelLines = []
                app.linesTouched = []
                app.allLinesTouched = []
                app.mouseMovedLocation = ()
                app.mouseDraggedLocation = ()
                app.mousePressedLocation = ()
                app.level = 2
                app.starCount = 1
                app.move = False
                app.gameOver = False
            elif app.level == 2:
                app.mode = "endScreenMode"
                app.starCount = 2
            return True 
        else:
            app.gameOver = False
            return False


##################CLOSED#####################

######BALL  FUNCTIONS######
def updateLinesTouched(app):
    if app.level == 1:
        currLinesTouched = []
        for line in app.linesTouched:
            if app.ball.isIntersecting(app, line): #, line2 = line
                currLinesTouched.append(line)
        app.linesTouched = currLinesTouched
    elif app.level == 2:
        if len(app.allLinesTouched) > 1:
            app.linesTouched = [(app.allLinesTouched[-1])]
        # app.linesTouched =
        # currLinesTouched2 = []
        # if app.gameOver: 
        #     currLinesTouched2 = []
        # for line in app.linesTouched:
        #     print("update2", app.linesTouched)
        #     if app.ball.isIntersecting(app, line): #, line2 = line
        #         currLinesTouched2.append(line)
        # app.linesTouched = currLinesTouched2
            
def stopBall(app):
    if len(app.linesTouched) == 2 and app.linesTouched[0] not in app.levelLines and app.linesTouched[1] not in app.levelLines:
            pass
    

def drawBall(app, canvas):
    #Start BALL AT BALL POSITION
    #ball has mass center, radius, balls should have velocitys, 
    #x velocity and y velocity
    # if on horizontal suyrface, verticla velocity is zero, horizontal velovity would be dependent on friction
    #adding constant amount to velocity
    #treat vertical velocity one way and horizontal one way
    #keep velocity and position, velocity modified first 
    #do y dimension and x dimension separately
    canvas.create_oval(app.ball.cx - app.ball.r, app.ball.cy - app.ball.r, app.ball.cx + app.ball.r, app.ball.cy + app.ball.r, fill = app.ballColor)

##################BALL FUNCTIONS CLOSED#####################



##################KEY EVENTS#####################
def gameMode_keyPressed(app, event):
    oldColor = ""
    if event.key == "m": app.move = True
    if event.key == "r":
        appStarted(app)
    if event.key == "y":
        oldColor = app.levelLinesColor
        app.ballColor = "Yellow"
    if event.key == "p":
        oldColor = app.levelLinesColor
        app.ballColor = "Pink"
    if event.key == "g":
        app.ballColor = "Gray"
    if event.key == "u":
        app.levelLinesColor = oldColor
    if event.key == "s":
        app.move = False

    if event.key == "f":
        app.friction = True
    if event.key == "e":
        if len(app.lineList) >=1:
            app.lineList.pop(-1)
        if app.lineList == 1:
            app.lineList = []
    if event.key == "n":
        app.level = 2
        app.lineList = []
        app.levelLines = []
        app.linesTouched = []
        app.allLinesTouched = []
        app.mouseMovedLocation = ()
        app.mouseDraggedLocation = ()
        app.mousePressedLocation = ()
        app.n = True
    if event.key == "h":
        app.mode = "helperMode"
    #if u press i an instruction mannual will come down(ie about all the key presses)
    #enable physics on line for level 2
    #ball that line is on can be highlighted a certain color
            


##################CLOSED########################

##################TIMER FIRED #####################
def gameMode_timerFired(app):
    line2 = None
    if app.level == 1 and app.ball.isIntersecting(app, line2):
        app.timeg1 = time.time()
    else:
        app.timeg2 = time.time()
        app.gTimeDiff = app.timeg2 - app.timeg1

    if app.level == 1 and app.move and app.ball.isIntersecting(app, line2):
        m = 4
        app.velocity = round(abs(app.ball.cx-app.width/7.5/m)/18, 2) 
    elif app.level == 1 and not app.move:
        app.velocity = 0
    elif not app.ball.isIntersecting(app, line2) and app.move:
        app.velocity = 9.8
    if app.level == 1 and len(app.pressed) == 0:
        app.time1 = time.time()
        # print(app.time1)
    if len(app.lineList) == 0 and app.level ==2:
        app.move = False
    if len(app.lineList) == 1 and app.level == 2:
        buffer = 3
        line = app.lineList[0]
        slope = line.slopeInterceptForm()[0]
        if ((line.x0 > app.width/4.5 + buffer) or (line.x1 < app.width/1.6 - buffer)) or ((line.y0 > app.height/8.5 + buffer) or (line.y1 > app.height/8.5 + buffer or line.y1<app.height/8.5 - buffer)):
            app.lineColor = "Red"
            line.y0 += 30
            line.y1 += 30
            app.move = False
            if line.y0 > app.height and line.y1 > app.height:
                app.lineList = []
                app.lineColor = "Blue"
                app.mouseMovedLocation = ()
                app.mouseDraggedLocation = ()
                app.mousePressedLocation = ()

                
           
    #used to be if and not indented
        else: #len(app.lineList) == 1 and app.level == 2:
            slope = app.lineList[0].slopeInterceptForm()[0]
            if -.003 >= slope or slope >= .01:
                app.move = False
                y0, y1 = app.lineList[0].y0, app.lineList[0].y1
                if ((app.height/8.5 + 7 >= y0) or (y0 >= app.height/8.5 - 5)) or ((app.height/8.5 + 5 >= y1) or (y1 >= app.height/8.5 - 5)) :
                    app.move = False
        if app.level == 2 and len(app.lineList) > 1:
            appStarted(app)
    if app.ball.isIntersecting(app, None):
        app.touching = "Yes"
    else:
        app.touching = "No"
    if app.level == 2:
        app.friction = False
    app.timePassed += 1
    if app.level == 2:
        app.fRepresent = "Off(Permanently)"

    if app.friction:
        app.fRepresent = "Off"

    updateLines(app)
    updateStarts(app)
    addLevelLines(app)
    # if app.level == 2 and app.ball.isIntersecting(app, line2):
    #     print("level 2")
       
    
    stopBall(app)
    if app.move:
        if app.ball.isIntersecting(app, line2):
            start = .5
            start *= 1.25
            app.ball.vx += start
            if app.ball.vx > 3:
                a = 1.3  
                if app.ballColor == "Gray":
                    a += a *  2
                elif app.ballColor == "Pink" and app.ballColor == "Pink":
                    a += a * 2.6
                elif app.ballColor == "Yellow" and app.ballColor == "Yellow":
                    a += a *1.05
                app.ball.vx += + 2**a
                app.velocity2 = 0
                if app.move:
                    app.velocity2 = round(a*10, 2)
            # app.ball.vy -=.005
        else:
            app.ball.vx = 0
            app.ball.vy = 0

        app.ball.updateBallPosition(app)
        updateLinesTouched(app)
        app.ball.checkGameOver(app)
        app.timePassed += app.timerDelay
        app.ball.cx += app.timerDelay/25
        if 0 > app.ball.cx + app.ball.r or app.ball.cx - app.ball.r > app.width or app.ball.cy - app.ball.r > app.height or app.ball.cy - app.ball.r <0:
            #if you fall off you restart from the beginning
            appStarted(app)
       
##################CLOSED########################

##################MOUSE EVENTS#####################
def gameMode_mouseMoved(app, event):
    app.x, app.y = event.x, event.y
    # app.mouseMovedLocation.append((event.x, event.y))
    app.mouseMovedLocation = (event.x, event.y)
    
       
def gameMode_mousePressed(app, event):
    # app.mousePressedLocation.append((event.x, event.y))
    app.mousePressedLocation = (event.x, event.y)
    app.mousePresses = (event.x, event.y)
    app.pressed.append((event.x, event.y))
    # app.linesDrawn.append((event.x, event.y))
    
    

def gameMode_mouseDragged(app, event):
    app.x, app.y = event.x, event.y
    # app.mouseDraggedLocation =((event.x, event.y))
    app.mouseDraggedLocation = (event.x, event.y)
   

def gameMode_mouseReleased(app, event):
    app.mouseReleases = (event.x, event.y)
    # app.linesDrawn.append((event.x,event.y))
    createLines(app)

    
##################CLOSED#####################




################IMAGES###################
def backGround(app, canvas):
    canvas.create_image(500, 200, image = app.backgroundImage)

#Star next to score to indicate score of how many stars you have gotten
def scoreStar(app, canvas):
    canvas.create_image(app.width/30, app.height/38, image = app.scoreStarImage)

def drawStar(app, canvas):
    canvas.create_image(app.starPosition[0], app.starPosition[1], image = app.starImage)
    # app.starPosition = (app.width/1.3, app.height/2.2)
##################CLOSED#####################



##################SCORE#####################
#Total number of stars gotten
def score(app, canvas):
    canvas.create_text( app.width/18, app.height/800, text = f" x  {app.starCount}", anchor = "nw", font = "Arial 35",  fill = "white")

##################CLOSED#####################



##################DRAWING#####################

#CRAYON#
    #Draw image at coordinate of the mouse
def drawCrayon(app, canvas):
    #magic numbers to ensure crayon tip is alligned with cursor
    canvas.create_image(app.x + 12, app.y - 15, image = app.crayonImage) 
        
#LINES#

##################CLOSED#####################

###############LEVELS#################     

###General###
def changeLevelOne(app):
    if app.levelTwo:
        app.level = 2
        app.levelTwo = False
        app.gameOver = False
def changeLevelTwo(app):
    if app.levelThree:
       app.level = 3
       app.levelThree = False
       app.gameOver = False
def changeLevelThree(app):
    if app.endScreen:
        app.mode = "endScreen"


###Level 1#####
def levelOneTerrain(app, canvas):
    #Left base line of First Green Rectangle
    canvas.create_line(app.width/15, app.height/2.4, app.width/15, app.height, fill = app.levelLinesColor)
    #Right base line of First Green Rectangle
    canvas.create_line(app.width/5, app.height/2.4, app.width/5, app.height, fill = app.levelLinesColor)
    #top line of first green rectangle
    canvas.create_line(app.width/15, app.height/2.4, app.width/5, app.height/2.4 , fill = app.levelLinesColor)
    #top line of second green rectangle
    canvas.create_line(app.width/5, app.height/2.05, app.width/4, app.height/2.05 , fill = app.levelLinesColor)
    #right base line of second green rectangle
    canvas.create_line(app.width/4, app.height/2.05, app.width/4, app.height , fill = app.levelLinesColor)
    #left base line of third green rectangle
    canvas.create_line(app.width/1.4, app.height/2.05, app.width/1.4, app.height , fill = app.levelLinesColor)
    #top line of third green rectangle
    canvas.create_line(app.width/1.4, app.height/2.05, app.width/1.2, app.height/2.05 , fill = app.levelLinesColor)
    #right base line of third green rectangle
    canvas.create_line(app.width/1.2, app.height/2.05, app.width/1.2, app.height , fill = app.levelLinesColor)
    if app.mode == "gameMode":
        canvas.create_text(app.width/2, 50, font = 'Arial 30 bold', text = "Welcome to level 1!")
        canvas.create_rectangle(app.width/1.6, 2, app.width/1.2, app.height/6, outline ="Green", width = 2 )
        canvas.create_text(app.width/1.38, app.height/13, font = 'Arial 16 bold', text = f"Your current velocity is:{app.velocity}")
        canvas.create_text(app.width/1.38, app.height/9, font = 'Arial 16 bold', text = f"You have friction: {app.fRepresent}")
        canvas.create_text(app.width/1.38, app.height/7, font = 'Arial 16 bold', text = f"Is your ball touching a line? :{app.touching} ")
        canvas.create_text(app.width/1.38, app.height/27, font = 'Arial 20 bold', text = "Your balls status!")
        if len(app.lineList) == 0:
            canvas.create_text(app.width/5, app.height/4.3, font = 'Arial 16 bold', text = "Draw a line with your crayon that you think the ball can follow to the star.")
            canvas.create_text(app.width/5, app.height/3.8, font = 'Arial 16 bold', text = "Once you are satisfied, press 'm' to give the ball a push.")
            canvas.create_text(app.width/5, app.height/3.4, font = 'Arial 14 bold', text = "However, beware! If your ball falls off the screen you restart from the very beginning!")
            canvas.create_text(app.width/5, app.height/5, font = 'Arial 18 bold', text = "Instructions:")

    
def levelTwoTerrain(app, canvas):
    canvas.create_line(app.width/10, app.height/8.5, app.width/10, app.height, fill = "Blue")
    #Left base line of First blue Rectangle
    canvas.create_line(app.width/4.5, app.height/8.5, app.width/4.5, app.height, fill = "Blue")
    #Right base line of third blue rectangle
    canvas.create_line(app.width/10, app.height/8.5, app.width/4.5, app.height/8.5 , fill = "Blue")
    #top line of first blue rectangle
    canvas.create_line(app.width/1.6, app.height/8.5, app.width/1.6, app.height , fill = "Blue")
    #Left line of third blue rectangle
    canvas.create_line(app.width/1.6, app.height/8.5, app.width/1.4, app.height/8.5 , fill = "Blue")
    #Top line of second blue rectangle
    canvas.create_line(app.width/1.4, app.height/8.5, app.width/1.4, app.height , fill = "Blue")
    #Right line of third blue rectangle

    if len(app.lineList) == 0:
        canvas.create_line(app.width/4.5, app.height/8.5, app.width/1.6, app.height/8.5, fill = "white")
        # canvas.create_text(app.width/2 -112, app.height/12, font = 'Arial 14 bold', text = "Fill in the line below!")
        canvas.create_text(app.width/2 -100, app.height/6.2, font = 'Arial 19 bold', text = "As a reward for beating level 1, this will be much easier!")
        canvas.create_text(app.width/2 -115, app.height/5, font = 'Arial 17 bold', text = "However, it will test the accuracy of your line drawing skills much more.")
        canvas.create_text(app.width/2 -115, app.height/3.7, font = 'Arial 17 bold', text = "Instructions:")
        canvas.create_text(app.width/2 -115, app.height/3.3, font = 'Arial 15 bold', text = "Draw with your crayon over the white line, you can't move your ball until you do so!")
        canvas.create_text(app.width/2 -115, app.height/3, font = 'Arial 15 bold', text = "Make sure your line closely resembles the white line or the ball wont move.")
        canvas.create_text(app.width/2 -115, app.height/2.7, font = 'Arial 18 bold', text = "Important!:")
        canvas.create_text(app.width/2 -115, app.height/2.5, font = 'Arial 16 bold', text = "This level is meant to be easy so you are only allowed one line.")
        canvas.create_text(app.width/2 -115, app.height/2.3, font = 'Arial 15 bold', text = "If you cheat and draw more than one line you will be punished and have to restart!")
        canvas.create_text(app.width/2 -100, app.height/25, font = 'Arial 25 bold', text = "Welcome to level 2, bridge in the sky!")
    
    elif len(app.lineList) == 1:
        canvas.create_text(app.width/2 -112, app.height/30, font = 'Arial 14 bold', text = "For obvious reasons(Flat surface) friction is permanently disabled for this level!")
        canvas.create_text(app.width/2 -112, app.height/5, font = 'Arial 14 bold', text = "*Hint* You may want to change the balls color to make this level a bit less painfully slow :)")
    if app.lineColor == "Red":
        canvas.create_text(app.width/2 -115, app.height/2.5, font = 'Arial 22 bold', text = "Oh no, you drew a bad line!")
        canvas.create_text(app.width/2 -115, app.height/2.3, font = 'Arial 20 bold', text = "As you watch it fall I hope you learn your lesson and try again")

   
   
    canvas.create_rectangle(app.width/1.3, 0, app.width, app.height/5, outline = "Green", width = 2)
    canvas.create_text(app.width/1.15, app.height/11, font = 'Arial 16 bold', text = f"Your current velocity is:{app.velocity2}")
    canvas.create_text(app.width/1.15, app.height/8.5, font = 'Arial 16 bold', text = f"You have friction: {app.fRepresent}")
    canvas.create_text(app.width/1.15, app.height/6.5, font = 'Arial 16 bold', text = f"Is your ball touching a line? :{app.touching} ")
    canvas.create_text(app.width/1.15, app.height/25, font = 'Arial 16 bold', text = "Your balls status!")
   
    




  

def addLevelLines(app):
    if app.level == 1:
        #Left base line of First Green Rectangle
        app.levelLines.append((app.width/15, app.height/2.4,  app.width/15, app.height)) #tuple containing two tuples that hold x0 y0 x1 y1
        #Right base line of First Green Rectangle
        app.levelLines.append((app.width/5, app.height/2.4, app.width/5, app.height))
        #top line of first green rectangle
        app.levelLines.append((app.width/15, app.height/2.4,app.width/5, app.height/2.4))
        #top line of second green rectangle
        app.levelLines.append((app.width/5, app.height/2.05,  app.width/4, app.height/2.05))
        #right base line of second green rectangle
        app.levelLines.append((app.width/4, app.height/2.05,  app.width/4, app.height))
        #left base line of third green rectangle
        app.levelLines.append((app.width/1.4, app.height/2.05,  app.width/1.4, app.height))
        #top line of third green rectangle
        app.levelLines.append((app.width/1.4, app.height/2.05,  app.width/1.2, app.height/2.05))
        #right base line of third green rectangle
        app.levelLines.append((app.width/1.2, app.height/2.05,  app.width/1.2, app.height))
    if app.level == 2:
        app.levelLines.append((app.width/10, app.height/8.5, app.width/10, app.height))
        #Right base line of First Green Rectangle
        app.levelLines.append((app.width/4.5, app.height/8.5, app.width/4.5, app.height))
        #top line of first green rectangle
        app.levelLines.append((app.width/10, app.height/8.5, app.width/4.5, app.height/8.5))
        #left base line of third green rectangle
        app.levelLines.append((app.width/1.6, app.height/8.5, app.width/1.6, app.height))
        #left line of second green rectangle
        app.levelLines.append((app.width/1.6, app.height/8.5, app.width/1.4, app.height/1.35))
        #top line of second base line of third green rectangle
        app.levelLines.append((app.width/1.4, app.height/8.5, app.width/1.4, app.height))
        #right line of second green rectangle
    



##################CLOSED#####################   


def gameMode_redrawAll(app, canvas):
    ###Always draw these###
    backGround(app, canvas)
    score(app, canvas)
    scoreStar(app, canvas)
    drawStar(app, canvas)
   
   
    ###Always draw these closed###
    ### if moving ###
    drawCrayon(app, canvas)
    drawBall(app, canvas)
    if app.moved:
        app.moved = False
    ### if dragging ###
    if not app.moved:
        drawCrayonLines(app, canvas)
        app.moved = True
    if app.level == 2:
        levelTwoTerrain(app, canvas)
    elif app.level == 1:
        levelOneTerrain(app, canvas)
    elif app.level == 3:
        pass


runApp(width=1500, height=860)
