import random
import turtle
import time

class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawself(self, turtle):
        turtle.goto(self.x - 9, self.y - 9)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(18)
            turtle.left(90)
        turtle.end_fill()

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = "ON"

    def changelocation(self):
        self.x = random.randint(0, 20)*20 - 200
        self.y = random.randint(0, 20)*20 - 200

    def drawself(self, turtle):
        if self.state == "ON":
            turtle.goto(self.x - 9, self.y - 9)
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(18)
                turtle.left(90)
            turtle.end_fill()

    def changestate(self):
        # controls the blinking
        self.state = "OFF" if self.state == "ON" else "ON"

class Snake:
    def __init__(self):
        self.headposition = [20, 0]
        self.body = [Square(-20, 0), Square(0, 0), Square(20, 0)]
        self.nextX = 1 
        self.nextY = 0
        self.crashed = False
        self.nextposition = [self.headposition[0] + 20*self.nextX,
                             self.headposition[1] + 20*self.nextY]

    def moveOneStep(self):
        if Square(self.nextposition[0], self.nextposition[1]) not in self.body: 
            self.body.append(Square(self.nextposition[0], self.nextposition[1])) 
            del self.body[0]
            self.headposition[0], self.headposition[1] = self.body[-1].x, self.body[-1].y
            self.nextposition = [self.headposition[0] + 20*self.nextX,
                                 self.headposition[1] + 20*self.nextY]
        else:
            self.crashed = True

    def moveup(self):
        self.nextX = 0
        self.nextY = 1

    def moveleft(self):
        self.nextX = -1
        self.nextY = 0

    def moveright(self):
        self.nextX = 1
        self.nextY = 0

    def movedown(self):
        self.nextX = 0
        self.nextY = -1

    def eatFood(self):
        self.body.append(Square(self.nextposition[0], self.nextposition[1]))
        self.headposition[0], self.headposition[1] = self.body[-1].x, self.body[-1].y
        self.nextposition = [self.headposition[0] + 20*self.nextX,
                             self.headposition[1] + 20*self.nextY]

    def drawself(self, turtle):
        for segment in self.body:
            segment.drawself(turtle)


class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.artist = turtle.Turtle()
        self.artist.up()
        self.artist.hideturtle()
        self.snake = Snake()
        self.food = Food(100, 0)
        self.counter = 0
        self.commandpending = False

    def nextFrame(self):
        while True:
            game.screen.listen()
            game.screen.onkey(game.snakedown, "Down")
            game.screen.onkey(game.snakeup, "Up")
            game.screen.onkey(game.snakeleft, "Left")
            game.screen.onkey(game.snakeright, "Right")
            turtle.tracer(0)
            self.artist.clear()
            if self.counter == 5: 
                if (self.snake.nextposition[0], self.snake.nextposition[1]) == (self.food.x, self.food.y):
                    self.snake.eatFood()
                    self.food.changelocation()
                else:
                    self.snake.moveOneStep()
                self.counter = 0
            else:
                self.counter += 1
            self.food.changestate()
            self.food.drawself(self.artist)
            self.snake.drawself(self.artist)
            turtle.update()
            self.commandpending = False
            time.sleep(0.05)

    def snakeup(self):
        print("going up")
        if not self.commandpending: 
            self.snake.moveup()
            self.commandpending = True

    def snakedown(self):
        print("going down")
        if not self.commandpending:
            self.snake.movedown()
            self.commandpending = True

    def snakeleft(self):
        print("going left")
        if not self.commandpending:
            self.snake.moveleft()
            self.commandpending = True

    def snakeright(self):
        print("going right")
        if not self.commandpending:
            self.snake.moveright()
            self.commandpending = True


game = Game()
game.nextFrame()
print("game over!")

game.screen.mainloop()
