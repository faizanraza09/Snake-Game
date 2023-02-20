add_library('minim')
import os
import random
import copy


path = os.getcwd()


class Node:
    def __init__(self,x,y,r,c=None):
        self.x=x
        self.y=y
        self.r=r
        self.c=c
        self.previous=None
        
class Head(Node):
    def __init__(self,x,y,r):
        Node.__init__(self,x,y,r)
        self.orientations=[loadImage(path + "/images/" + "head_right" + ".png"),loadImage(path + "/images/" + "head_left" + ".png"),loadImage(path + "/images/" + "head_up" + ".png"),loadImage(path + "/images/" + "head_down" + ".png")]
    
        
        
    
class Snake(list):
    def __init__(self,w,h,x,y,r):
        self.w=w
        self.h=h
        self.x=x
        self.y=y
        self.r=r
        self.head=Head(self.x,self.y,self.r)
        self.append(self.head)
        x_cord=self.head.x-self.r
        self.handler=[1,0]
        self.fruit=random.choice(['apple','banana'])
        (self.food_x,self.food_y)=self.create_food()
        self.pg=True
        
        
    def move(self):
        
        for i in self:
            if self[0] == i:
                tempx = i.x
                tempy = i.y
                i.x+=15
                i.y+=15
                #i.x = i.x + self.handler[0]*self.r
                #i.y = i.y + self.handler[1]*self.r
            else:
                temp1x = i.x
                temp1y = i.y
                i.x = tempx
                i.y = tempy
                tempx = temp1x
                tempy = temp1y
                
    def create_food(self):
        food_x=random.randint(0,self.w-3*self.r)
        food_y=random.randint(0,self.h-3*self.r)
        
        free=False
        
        while free==False:
            food_x=random.randint(0,self.w-self.r)
            food_y=random.randint(0,self.h-self.r)
            free=True
            for i in self:
                if food_x in range(i.x-self.r/2,i.x+self.r/2+1):
                    free=False
                elif food_y in range(i.y-self.r/2,i.y+self.r/2+1):
                    free=False 
                    
        
        
        return (food_x,food_y)
                    
                
        
    
    def grow(self):
        if self.head.x in range(self.food_x,self.food_x+self.r+1) and self.head.y in range(self.food_y,self.food_y+self.r+1):
            if self.fruit=='apple':
                c=[173, 48, 32]
            else:
                c=[251, 226, 76]
                
            

                
            if len(self)==1:
                c= [80, 153, 32]

                if self.handler==[1,0]:
                    self.append(Node(self[-1].x-self.r,self[-1].y,self.r,c))
                elif self.handler==[-1,0]:
                    self.append(Node(self[-1].x+self.r,self[-1].y,self.r,c))
                elif self.handler==[0,-1]:
                    self.append(Node(self[-1].x,self[-1].y-self.r,self.r,c))
                elif self.handler==[0,1]:
                    self.append(Node(self[-1].x,self[-1].y+self.r,self.r,c))
                    
            
                    
            else:
                if len(self)==2:
                    c= [80, 153, 32]

                if self[-1].x==self[-2].x:
                    if self[-1].x-self[-2].x>0:
                        self.append(Node(self[-1].x+self.r,self[-1].y,self.r,c))
                    else:
                        self.append(Node(self[-1].x-self.r,self[-1].y,self.r,c))
                else:
                    if self[-1].y-self[-2].y>0:
                        self.append(Node(self[-1].x,self[-1].y+self.r,self.r,c))
                    else:
                        self.append(Node(self[-1].x,self[-1].y-self.r,self.r,c))
                 
            self.fruit=random.choice(['apple','banana'])       
            (self.food_x,self.food_y)=self.create_food()
            
                
                    
    def check_end(self):
        pass
        
        
        
       
    def check_crash(self):
        if self.head.x>=self.w or self.head.x<=0:
            self.pg=False
        elif self.head.y<=0 or self.head.y>=self.h:
            self.pg=False
        
        else:
            for i in range(1,len(self)):
                if self[i].x==self.head.x and self[i].y==self.head.y:
                    self.pg=False
                    
            
                    
        
            
            


    def display(self):
        textSize(30)
        fill(255,0,0)
        text('Score: '+ str(len(game.snake)),self.w/2-50,50)

        if self.handler==[1,0]:
            image(self.head.orientations[0],self.head.x-self.r/2,self.head.y-self.r/2,self.r,self.r)        
        elif self.handler==[-1,0]:
            image(self.head.orientations[1],self.head.x-self.r/2,self.head.y-self.r/2,self.r,self.r)
        elif self.handler==[0,-1]:
            image(self.head.orientations[2],self.head.x-self.r/2,self.head.y-self.r/2,self.r,self.r)
        else:
            image(self.head.orientations[3],self.head.x-self.r/2,self.head.y-self.r/2,self.r,self.r)
            
    
        
        for i in range(1,len(self)):
            fill(self[i].c[0],self[i].c[1],self[i].c[2])
            ellipse(self[i].x,self[i].y,self.r,self.r)
            
            
        img2=loadImage(path + "/images/" + self.fruit + ".png")
        
        
        image(img2,self.food_x,self.food_y,self.r,self.r)
            
        

            
        
    '''def movesnake(self):
        for elements in self:
            if game[0] = element:
                tempx = element.x
                tempy = element.y
                element.x = element.x + keyhandler
                element.y = element.y + keyhandler
            else:
                temp1x = element.x
                temp1y = element.y
                element.x = tempx
                element.y = tempy
                tempx = temp1x
                tempy = temp1y'''
                

                
            
        
            


class Game:
    def __init__(self,w,h):
        self.w=w
        self.h=h    
        self.snake=Snake(self.w,self.h,self.w/2,self.h/2,25)
        
    
    def display(self):
        self.snake.check_crash()
        self.snake.display()
        self.snake.move()
        self.snake.grow()
        

    


game=Game(600,600)
def setup():
    size(game.w,game.h)
    
def draw():
    if frameCount%6 == 0:
        background(205)
        #this calls the display method of the game class
        if game.snake.pg==True:
            game.display()
        else:
            background(0)
            fill(255,0,0)
            textSize(30)
            text('YOUR GAME IS OVER, YOUR SCORE IS '+str(len(game.snake)),10,250)
            text('PRESS ENTER TO PLAY AGAIN',10,300)
            
            

    
def keyPressed():
    if keyCode==RIGHT:
        if len(game.snake)==1:
            game.snake.handler=[1,0]
        elif game.snake.head.y!=game.snake[1].y:
            game.snake.handler=[1,0]
    elif keyCode==LEFT:
        if len(game.snake)==1:
            game.snake.handler=[-1,0]
        elif game.snake.head.y!=game.snake[1].y:
            game.snake.handler=[-1,0]
    elif keyCode==UP:
        if len(game.snake)==1:
            game.snake.handler=[0,-1]
        elif game.snake.head.x!=game.snake[1].x:
            game.snake.handler=[0,-1]
    elif keyCode==DOWN:
        if len(game.snake)==1:
            game.snake.handler=[0,1]
        elif game.snake.head.x!=game.snake[1].x:
            game.snake.handler=[0,1]
            
def mouseClicked():
    if game.snake.pg==False:
        global game
        game=Game(600,600)
        
