from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
HEADINGS = {
    "up": 90,
    "down": 270,
    "left": 180,
    "right": 0
}


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for snake_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_num - 1].xcor()
            new_y = self.snake[snake_num - 1].ycor()
            self.snake[snake_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != HEADINGS["down"]:
            self.head.setheading(HEADINGS["up"])

    def down(self):
        if self.head.heading() != HEADINGS["up"]:
            self.head.setheading(HEADINGS["down"])

    def left(self):
        if self.head.heading() != HEADINGS["right"]:
            self.head.setheading(HEADINGS["left"])

    def right(self):
        if self.head.heading() != HEADINGS["left"]:
            self.head.setheading(HEADINGS["right"])

    def add_segment(self, position):
        snake_body = Turtle("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.snake.append(snake_body)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def reset_snake(self):
        for s in self.snake:
            s.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
