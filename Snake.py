from random import *
from tkinter import *

global window_width, window_height

window_width = 600
window_height = 600


class Snake():

    def __init__(self, root):
        self.length = 20
        self.width = 20
        self.position = [100, 100]
        #self.position = [randint(10+3*self.length,window_width-10), randint(self.width+10,window_height-10)]                  
        root.bind('<Left>', self.leftKey)
        root.bind('<Right>', self.rightKey)
        root.bind('<Up>', self.upKey)
        root.bind('<Down>', self.downKey)
        self.dx = 1
        self.dy = 0
        self.snake = []
        for i in range(3):
            snake_rect = canvas.create_rectangle(self.position[0] - i*self.length, self.position[1], self.position[0] - (i+1)*self.length, self.position[1] - self.width,  fill='yellow', outline='green')
            self.snake.append(snake_rect)
        
        
    def update(self): 
        for i in reversed(range(1, len(self.snake))):
            x0, y0, x1, y1 = canvas.coords(self.snake[i-1])
            canvas.coords(self.snake[i], x0, y0, x1, y1)
        canvas.coords(self.snake[0], x0+self.dx*self.length, y0+self.dy*self.length, x1+self.dx*self.length, y1+self.dy*self.length)
        x0, y0, x1, y1 = canvas.coords(self.snake[0])
        snake_verge = []
        for i in range(int(x0),int(x1)+1):
            for j in range(int(y0),int(y1)+1):
                    snake_verge.append([i,j])
        if Apple.position in snake_verge:
            snake_rect = canvas.create_rectangle(x0, y0, x1, y1,  fill='yellow', outline='green')         
            self.snake.append(snake_rect)
            Apple.position = [randint(20, window_width-20), randint(20, window_height-20)] 
            canvas.coords(Apple.apple, Apple.position[0],  Apple.position[1], Apple.position[0] + 5, Apple.position[1] + 5)
        if [x1,y1] in Wall.position:
                canvas.create_text(window_width/2, window_height/2, text="GAME OVER", font="Arial 20", fill="green")
        canvas.after(150, self.update)


    def leftKey(self, event):
        self.dx = -1
        self.dy = 0


    def rightKey(self, event):
        self.dx = 1
        self.dy = 0                

    def upKey(self, event):
        self.dx = 0
        self.dy = -1

    def downKey(self, event):
        self.dx = 0
        self.dy = 1          
        
class Apple():

    def __init__(self):
        self.position = [randint(20, window_width-20), randint(20, window_height-20)]
        self.apple = canvas.create_rectangle(self.position[0], self.position[1], self.position[0] + 5, self.position[1] + 5,  fill='red')

class Wall():

    def __init__(self):
        self.position = []
        for i in range(window_width+1):
            for j in range(window_height+1):
                if i == 0 or i == window_width or j == 0 or j == window_height:
                   self.position.append([i,j]) 
        for i in range(window_width+1):
            for j in range(window_height+1):
                if i == 0 and j % 10 == 0 :
                    canvas.create_rectangle(i, j, i + 10, j + 10, fill = 'green')
                if i == window_width and j % 10 == 0:
                    canvas.create_rectangle(i, j, i - 10, j + 10, fill = 'green')
                if i % 10 == 0 and j == 0:
                    canvas.create_rectangle(i, j, i + 10, j + 10, fill = 'green')
                if i % 10 == 0 and j == window_height:
                    canvas.create_rectangle(i, j, i + 10, j - 10, fill = 'green')


root = Tk()
canvas = Canvas(root, width=window_width, height=window_height, bg='white')
canvas.pack()
Snake = Snake(root)
Wall = Wall()
Apple = Apple()
canvas.after(10, Snake.update)
root.mainloop()
