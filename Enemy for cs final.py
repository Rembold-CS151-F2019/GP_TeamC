            #Enemy cs final code

import graphics as g
import random

class Enemy1:
    def __init__(self, w, x, y):
        self.w = w
        self.x = x
        self.y = y
        Enemy1.create(self)
        
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
        
    def move(self):
        if self.c.getCenter().getY() < 750:
            self.p.move(0, 2)
            self.e.move(0, 2)
            self.c.move(0, 2)
        elif self.c.getCenter().getY() >= 750:
            self.p.undraw()
            self.e.undraw()
            self.c.undraw()
        
        self.p.move(0, 2)
        self.e.move(0, 2)
        self.c.move(0, 2)
        self.w.after(2, self.move)
    
    def hit(self):
        if self.enemy_counter == 1:
            self.p.undraw()
            self.e.undraw()
            self.c.undraw()
    
w = g.GraphWin('Enemy', 1200, 800)
enemy1 = Enemy1(w, random.randint(100, 700), 50)
enemy1.move()

w.getKey()
w.close()    