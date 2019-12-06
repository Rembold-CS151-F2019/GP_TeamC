import graphics as g
import random
import sched, time
enemycounter = 5
score = 0
class board:
    
    def __init__(self,w):
        self.w = w
        self.create()
        self.instructions()
        self.scorecounters()
        self.deathline()
    def create(self):
        self.area = g.Rectangle(g.Point(50,0), g.Point(750,800))
        self.area.setFill('white')
        self.area.draw(self.w)
    def instructions(self):
        self.welcomemsg = g.Text(g.Point(1000, 100), "Shoot your Shot")
        self.welcomemsg.setFill('white')
        self.instructions = g.Text(g.Point(1000, 200), "Left and Right Arrow keys to move \n Up Arrow key to Fire")
        self.instructions.setFill('white')
        self.instructions.draw(self.w)
        self.welcomemsg.draw(self.w)
    def scorecounters(self):
        global enemycounter
        self.enemy_counter = g.Text(g.Point(1000, 500), f"Lives Remaining: {enemycounter}")
        self.enemy_counter.setFill('red') #enemy_counter is actual object
        self.enemy_counter.setSize(30)    #enemycounter is global variable starting at 10
        self.enemy_counter.draw(self.w)

        self.score = g.Text(g.Point(1000, 400), f"Your Score: {score}")
        self.score.setFill('green') #enemy_counter is actual object
        self.score.setSize(30)    #enemycounter is global variable starting at 10
        self.score.draw(self.w)

    def deathline(self):
        self.line = g.Line(g.Point(50, 700), g.Point(750, 700))
        self.line.setFill('red')
        self.line.draw(self.w)



class Enemy1:
    
    def __init__(self, w, x, y):
        self.w = w
        self.x = x
        self.y = y
        self.create()
        self.enemywin()
        self.move()
        
    def create(self):
        #creating enemy
        self.p = g.Polygon(g.Point(self.x, self.y), g.Point(self.x + 80, self.y), g.Point(self.x + 40, self.y + 80))
        self.e = g.Oval(g.Point(self.x + 15, self.y + 10), g.Point(self.x + 60, self.y + 40))
        self.c = g.Circle(g.Point(self.e.getCenter().getX(), self.e.getCenter().getY()), 10)
        #coloring enemy
        self.p.setFill('blue')
        self.e.setFill('white')
        self.c.setFill('red')
        #draw enemy
        for obj in [self.p, self.e, self.c]:
            obj.draw(self.w)
        
    def get_center(self):
        return self.c.getCenter()

    def move(self):
        import random
        if self.c.getCenter().getY() < 750:
            self.p.move(0, 0.1)
            self.e.move(0, 0.1)
            self.c.move(0, 0.1)
        elif self.c.getCenter().getY() >= 750:
            self.p.undraw()
            self.e.undraw()
            self.c.undraw()
        
        self.p.move(0, 0.1)
        self.e.move(0, 0.1)
        self.c.move(0, 0.1)
        self.w.after(2, self.move)
    
    def hit(self):
        global EnemyList
        global score
        self.p.undraw()
        self.e.undraw()
        self.c.undraw()
        EnemyList.remove(self)
        score += 1
        B.score.undraw()
        B.score.setText(f"Your Score: {score}")
        B.score.draw(self.w)
    def enemywin(self):
        global enemycounter
        global EnemyList
        global E
        
        if self.c.getCenter().getY() >= 700:
            self.hit()
            #EnemyList.remove(E)
            enemycounter -= 1
            B.enemy_counter.undraw()
            B.enemy_counter.setText(f"Lives Remaining: {enemycounter}")
            B.enemy_counter.draw(self.w)






class Tank:
    def __init__(self,window,x,y):
        self.w = window
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
            if self.left_main_track.getCenter().getX()>=65+2:
                self.left_main_track.move(-7,0)
                self.right_main_track.move(-7,0)
                self.tank_main_body_rectangle.move(-7,0)    
                self.cannon_part2.move(-7,0)
                self.cannon_part1.move(-7,0) #has this specific sequence to draw so the tank looks realistic
                self.cannon_part3.move(-7,0)
                self.second_body_rectangle.move(-7,0)
                self.hatch.move(-7,0)

        #CONTROLS FOR GOING RIGHT
        if key=='Right':
            if self.right_main_track.getCenter().getX()<=736.8-2:
                self.left_main_track.move(7,0)
                self.right_main_track.move(7,0)
                self.tank_main_body_rectangle.move(7,0)    
                self.cannon_part2.move(7,0)
                self.cannon_part1.move(7,0) #has this specific sequence to draw so the tank looks realistic
                self.cannon_part3.move(7,0)
                self.second_body_rectangle.move(7,0)
                self.hatch.move(7,0)
        
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
        



        for enemy in EnemyList:

            #ANDREW UNCOMMENT THESE THINGS
            #BULLET HITTING ENEMY1
                #THESE ENEMY NAMES MIGHT NEED TO BE CHANGED 
            if (enemy.get_center().getY()-25 <=self.bullet_body.getCenter().getY()<=enemy.get_center().getY()+25) and (self.bullet_body.getCenter().getX()>=enemy.get_center().getX()-25 and self.bullet_body.getCenter().getX()<=enemy.get_center().getX()+25):
                self.bullet_body.undraw() 
                self.bullet_shell.undraw() 
                enemy.hit()


class Two_Life_Enemy:    
    #This is an enemy that requires two shots to kill
    def __init__(self, w, x, y,is_big = True):
           
        self.w = w
        self.x = x
        self.y = y 
        self.speed = 1.5
        self.direction = 1
        self.enemy_counter = 1
        self.is_big = is_big
        if self.is_big:
            self.create_big()
        else:
            self.create_small()
        self.move()
    def create_big(self):
        #This creates the first life of the enemy
        self.body = g.Rectangle(g.Point(self.x, self.y), g.Point(self.x + 100, self.y + 100))
        self.body.setFill('lavender')
        self.body.draw(self.w)
    
    def create_small(self):
        #This creates the second life of the enemy
        self.body = g.Rectangle(g.Point(self.x, self.y), g.Point(self.x + 50, self.y + 50))
        self.body.setFill('teal')
        self.body.draw(self.w)
        
    def move(self):
        #This is the move function for the big square it moves diagonally while the little square moves straight down 
        if self.is_big == True:
            
            if self.body.getCenter().getX() <= 100:
                self.direction = 1
            elif self.body.getCenter().getX() >= 700:
                self.direction = -1
            self.body.move(self.direction * self.speed, .5)
        else:             
            self.body.move(0, .5)
        self.w.after(10, self.move)
    def hit(self):
        #This function respawns the little square after getting hit with a bullet
        global score
        self.body.undraw()
        if self.is_big == True:
            x = self.body.getCenter().getX()
            y = self.body.getCenter().getY()
            EnemyList.append(Two_Life_Enemy(self.w, x, y-40, False))
            
        EnemyList.remove(self)
        score += 1
        B.score.undraw()
        B.score.setText(f"Your Score: {score}")
        B.score.draw(self.w)
    def enemywin(self):
        #This is the function that removes a life and the enemy if it gets to the line of death
        global enemycounter
        global EnemyList
        global E
        if self.body.getCenter().getY() >= 700:
            self.hit()
            #EnemyList.remove(self)
            enemycounter -= 1
            B.enemy_counter.undraw()
            B.enemy_counter.setText(f"Lives Remaining: {enemycounter}")
            B.enemy_counter.draw(self.w)
    def get_center(self):
        return self.body.getCenter()


def spawnenemy():
    #This is the function that spawns 4 enemies every 15 seconds
    global EnemyList
    global Q
    global E
    global enemycounter
    global w
    listcounter = 0
    
    while enemycounter > 0 and listcounter < 4:
        
        E = Enemy1(w, random.randint(100,700), 50)
        EnemyList.append(E)
        Q = Two_Life_Enemy(w, random.randint(100,700), 50)
        EnemyList.append(Q)
        listcounter += 2
        
    w.after(15000,spawnenemy)

def main():
    #The function to actually run the game
    global EnemyList, B, enemycounter, E, Q, w
    w = g.GraphWin('GAME!!', 1200,800)
    w.setBackground('black')
    B = board(w)
    T=Tank(w,475,710)
    # c = Two_Life_Enemy(w,rand.randint(80,940), 100)
    # c.move()

    EnemyList = []
    
    spawnenemy()
    key=None
    
    while key != 'q':
        for enemy in EnemyList:
            enemy.enemywin()
        key = w.checkKey()
        T.tank_controls(key)
        if enemycounter <= 0:
                w.close()
    w.close()
if __name__ == "__main__":
    main()
