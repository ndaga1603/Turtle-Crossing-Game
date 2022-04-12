
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.increase_level()
     

    
    def increase_level(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level {self.level}",align="center", font=FONT)
        self.level += 1
      
      
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER",font=FONT)

     



