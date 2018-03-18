''' Step 1: Create a graphwin object, draw 5 eyes into it
        -Create an eye class that will easily enable drawing an 'eye' into a window
    Step 2: Get a mouseclick from the user
    Step 3: Move the pupils to 'look' at where the mouse clicked


'''
from graphics import *
class Eyeball:
    def __init__(self, win, centerPoint):
        self.window = win
        
        self.minX = centerPoint.getX() - 10
        self.maxX = centerPoint.getX() + 10
        
        self.minY = centerPoint.getY() - 10
        self.maxY = centerPoint.getY() + 10
        
        ulPt = Point( self.minX, self.minY)
        lrPt = Point( self.maxX, self.maxY)
        
        self.eyeOutline = Rectangle( ulPt, lrPt )
        self.eyeOutline.setFill( 'white' )
        self.eyeOutline.draw(win)
        
        self.pupilMinX = centerPoint.getX() - 5
        self.pupilMaxX = centerPoint.getX() + 5
        pupilMinY = centerPoint.getY() - 5
        pupilMaxY = centerPoint.getY() + 5
        
        pupilUlPt = Point(self.pupilMinX, pupilMinY)
        pupilLrPt = Point(self.pupilMaxX, pupilMaxY)
        
        self.eyePupil = Rectangle(pupilUlPt, pupilLrPt)
        self.eyePupil.setFill('black')
        self.eyePupil.draw(win)
        
    def updatePupil(self, newPoint):
        dX = 0
        if newPoint.getX() <= self.maxX and newPoint.getX() >= self.pupilMaxX:
            dX = newPoint.getX() - self.pupilMaxX
        elif newPoint.getX() >= self.maxX:
            dX = self.maxX - self.pupilMaxX
        elif newPoint.getX() >= self.minX and newPoint.getX() <= self.pupilMinX:
            dX = newPoint.getX() - self.pupilMinX
        elif newPoint.getX() <= self.minX:
            dX = self.minX - self.pupilMinX
        
        self.eyePupil.move(dX,0)
        
def main():
    win = GraphWin('Someones Watching Me', 500, 500)
    newEye1 = Eyeball(win, Point(100,100))
    newEye2 = Eyeball(win, Point(150,150))
    newEye3 = Eyeball(win, Point(200,200))
    newEye4 = Eyeball(win, Point(250,250))
    newEye5 = Eyeball(win, Point(300,300))

    newPoint = win.getMouse()
    newEye1.updatePupil(newPoint)
    newEye2.updatePupil(newPoint)
    newEye3.updatePupil(newPoint)
    newEye4.updatePupil(newPoint)
    newEye5.updatePupil(newPoint)
    
    
main()
