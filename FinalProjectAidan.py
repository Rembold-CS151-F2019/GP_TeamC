import graphics as g
class Tank:
    def __init__(self,window,x,y):
        self.w=window
        self.x=x
        self.y=y
        self.tank_life=1
        self.drawTank()

    def drawTank(self):
        '''BUILDING THE TANK FROM GROUND UP TO GET THE CORRECT OVERLAPS
        
        '''
        #MAKING THE TRACKs NOW
        
        #LEFT TRACK
        self.left_main_track=g.Rectangle(g.Point(self.x-10,self.y-10),g.Point(self.x+10,self.y+85))
        self.left_main_track.setFill('black')
        self.left_main_track.setOutline('brown')

        #RIGHT TRACK
        self.right_main_track=g.Rectangle(g.Point(self.x+40,self.y-10),g.Point(self.x+60,self.y+85))
        self.right_main_track.setFill('black')
        self.right_main_track.setOutline('brown')

        #MAKING THE BODY PARTS OF THE TANK FROM BOTTOM UP
        
        #MAIN BODY OF THE TANK
        self.tank_main_body_rectangle=g.Rectangle(g.Point(self.x,self.y),g.Point(self.x+50,self.y+75))
        self.tank_main_body_rectangle.setFill('green')
        self.tank_main_body_rectangle.setOutline('black')
        
        #SECOND BODY OF THE TANK THAT GOES ON TOP OF THE MAIN BODY
        self.second_body_rectangle=g.Rectangle(g.Point(self.x+7,self.y+30),g.Point(self.x+43,self.y+68))
        self.second_body_rectangle.setFill('green')
        self.second_body_rectangle.setOutline('black')

        #HATCH ON TOP OF THE SECOND BODY
        self.hatch=g.Circle(g.Point(self.x+25,self.y+49),7)
        self.hatch.setFill('green')
        self.hatch.setOutline('black')
        
        #CANNON PART 1 THAT GOES ON TOP OF MAIN BODY AND HAS THE SECOND BODY DRAW OVER IT
        self.cannon_part1=g.Rectangle(g.Point(self.x+20,self.y+22),g.Point(self.x+30,self.y+35))
        self.cannon_part1.setFill('green')
        self.cannon_part1.setOutline('black')

        #CANNON PART 2 THAT IS LONG AND CONNECTS TO CANNON PART 1
        self.cannon_part2=g.Rectangle(g.Point(self.x+22,self.y-13),g.Point(self.x+28,self.y+25))
        self.cannon_part2.setFill('green')
        self.cannon_part2.setOutline('black')

        #CANNON PART 3 THAT CONNECTS TO THE END OF CANNON PART 2
        self.cannon_part3=g.Rectangle(g.Point(self.x+20,self.y-20),g.Point(self.x+30,self.y-10))
        self.cannon_part3.setFill('green') #9 tall and 
        self.cannon_part3.setOutline('black')

        #DRAWING ALL THE OBJECTS
        #dont change this sequence of code
        self.left_main_track.draw(self.w)
        self.right_main_track.draw(self.w)
        self.tank_main_body_rectangle.draw(self.w)    
        self.cannon_part2.draw(self.w)
        self.cannon_part1.draw(self.w) #has this specific sequence to draw so the tank looks realistic
        self.cannon_part3.draw(self.w)
        self.second_body_rectangle.draw(self.w)
        self.hatch.draw(self.w)

    def tank_controls(self,key):
        #CONTROLS FOR GOING LEFT
        if key=='Left': #ANDREW you will have to change the values for all the parts below to not go outside the border you have put in 
            if self.left_main_track.getCenter().getX()>=90+10:
                self.left_main_track.move(-10,0)
                self.right_main_track.move(-10,0)
                self.tank_main_body_rectangle.move(-10,0)    
                self.cannon_part2.move(-10,0)
                self.cannon_part1.move(-10,0) #has this specific sequence to draw so the tank looks realistic
                self.cannon_part3.move(-10,0)
                self.second_body_rectangle.move(-10,0)
                self.hatch.move(-10,0)

        #CONTROLS FOR GOING RIGHT
        if key=='Right':
            if self.right_main_track.getCenter().getX()<=890-10:
                self.left_main_track.move(10,0)
                self.right_main_track.move(10,0)
                self.tank_main_body_rectangle.move(10,0)    
                self.cannon_part2.move(10,0)
                self.cannon_part1.move(10,0) #has this specific sequence to draw so the tank looks realistic
                self.cannon_part3.move(10,0)
                self.second_body_rectangle.move(10,0)
                self.hatch.move(10,0)
        
        #CONTROLS FOR SHOOTING BULLET IS UP ARROW
        if key=='Up':
            Bullet(self.w,self.cannon_part3.getCenter().getX()-2.45,self.cannon_part3.getCenter().getY()-27.5)

        #ANDREW UNCOMMENT THESE THINGS
        #HIT DETECTION OF ENEMY1 HITTING TANK
        # if (self.enemy1.getCenter().getY()<=self.tank_main_body_rectangle.getCenter().getY()+10) and (self.tank_main_body_rectangle.getCenter().getX()>=self.enemy1.getCenter().getX()-10 and self.tank_main_body_rectangle.getCenter().getX()<=self.enemy1.getCenter().getX()+10):
        #     self.tank_life=0
        #     self.left_main_track.undraw()
        #     self.right_main_track.undraw()
        #     self.tank_main_body_rectangle.undraw()    
        #     self.cannon_part2.undraw()
        #     self.cannon_part1.undraw() #has this specific sequence to draw so the tank looks realistic
        #     self.cannon_part3.undraw()
        #     self.second_body_rectangle.undraw()
        #     self.hatch.undraw()

        #HIT DETECTION OF ENEMY2 HITTING TANK
        # if (self.enemy2.getCenter().getY()<=self.tank_main_body_rectangle.getCenter().getY()+10) and (self.tank_main_body_rectangle.getCenter().getX()>=self.enemy2.getCenter().getX()-10 and self.tank_main_body_rectangle.getCenter().getX()<=self.enemy2.getCenter().getX()+10):
            # self.tank_life=0
            # self.left_main_track.undraw()
            # self.right_main_track.undraw()
            # self.tank_main_body_rectangle.undraw()    
            # self.cannon_part2.undraw()
            # self.cannon_part1.undraw() #has this specific sequence to draw so the tank looks realistic
            # self.cannon_part3.undraw()
            # self.second_body_rectangle.undraw()
            # self.hatch.undraw()

class Bullet(Tank):
    def __init__(self,window,x,y):
        self.w=window
        self.x=x
        self.y=y
        self.drawBullet()
        self.fireBullet()

    def drawBullet(self):
        #RED OVAL THAT IS THE HEAD OF THE BULLET
        self.bullet_body=g.Oval(g.Point(self.x,self.y),g.Point(self.x+5,self.y+15))
        self.bullet_body.setFill('red')
        self.bullet_body.setOutline('black')

        #THIS IS THE BLACK RECTANGLE ON TOP OF THE RED OVAL (SHELL)
        self.bullet_shell=g.Rectangle(g.Point(self.x,self.y+7.5),g.Point(self.x+5,self.y+22))
        self.bullet_shell.setFill('black')
        
        #DRAWING THE BULLET
        self.bullet_body.draw(self.w)
        self.bullet_shell.draw(self.w)

    def fireBullet(self):
        #MOVING THE HEAD AND SHELL 
        self.bullet_body.move(0,-10)#making the bullet go up
        self.bullet_shell.move(0,-10)
        self.w.after(10,self.fireBullet)#making the bullet move every 10 milliseconds
        if self.bullet_body.getCenter().getY()<=0+10:
            self.bullet_body.undraw()
            self.bullet_shell.undraw()
            
            #ANDREW UNCOMMENT THESE THINGS
            #BULLET HITTING ENEMY1
                #THESE ENEMY NAMES MIGHT NEED TO BE CHANGED 
            # if (self.bullet_body.getCenter().getY()<=self.enemy1.getCenter().getY()+10) and (self.bullet_body.getCenter().getX()>=self.enemy1.getCenter().getX()-10 and self.bullet_body.getCenter().getX()<=self.enemy1.getCenter().getX()+10):
            #     self.bullet_body.undraw() 
            #     self.bullet_shell.undraw() 
            #     #Assuming that charles and eric's code with have the result that is the counter ==0 to undraw() the enemy othersise add that under the decreased counter lines with another if statement
            #     self.enemy1_counter-=1 #THIS ENEMY NAME MIGHT NEED TO BE CHANGED
            #     self.hit_count+=1 #THIS NAME MIGHT NEED TO BE CHANGED

        #BULLET HITTING ENEMY2
            #THESE ENEMY NAMES MIGHT NEED TO BE CHANGED  
            # if (self.bullet_body.getCenter().getY()<=self.enemy2.getCenter().getY()+10) and (self.bullet_body.getCenter().getX()>=self.enemy2.getCenter().getX()-10 and self.bullet_body.getCenter().getX()<=self.enemy2.getCenter().getX()+10):
            #     self.bullet_body.undraw() 
            #     self.bullet_shell.undraw() 
            #     #Assuming that charles and eric's code with have the result that is the counter ==0 to undraw() the enemy othersise add that under the decreased counter lines with another if statement
            #     self.enemy2_counter-=1 #THIS ENEMY NAME MIGHT NEED TO BE CHANGED
            #     self.hit_count+=1 #THIS NAME MIGHT NEED TO BE CHANGED

w=g.GraphWin('Final Project',1000,1000) # ANDREW YOU CAN DELETE THIS STUFF ONCE YOU HAVE YOUR OWN assigning the window size
w.setBackground('white')
T=Tank(w,475,600)
key=None #NEED EVERYTHING BELOW HERE FOR THE KEYS TO WORK
while key != 'q':
    key=w.checkKey()
    T.tank_controls(key)
w.close()