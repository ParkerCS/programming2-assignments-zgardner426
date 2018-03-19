
#Turtle Recursion (33pts)
import turtle
import random


my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_screen = turtle.Screen()
my_screen.bgcolor("lightblue")
my_turtle.shape("turtle")
my_turtle.speed(0)
my_turtle.width(2)
my_turtle.pencolor("black")
color_list = ["white", "black", "yellow", "red", "darkblue", "green", "purple", "pink", "orange"]


#  1)  Using the turtle library, create the H fractal pattern according to the file shown in the data folder. (15pts)
def h_fractal(x, y, size, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + size, y)
        my_turtle.goto(x + size, y + size)
        my_turtle.goto(x + size, y - size)
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x - size, y)
        my_turtle.goto(x - size, y + size)
        my_turtle.goto(x - size, y - size)
        my_turtle.pencolor(color_list[random.randrange(9)])
        h_fractal(x + size, y + size, size / 2, depth - 1)
        h_fractal(x - size, y + size, size / 2, depth - 1)
        h_fractal(x - size, y - size, size / 2,  depth - 1)
        h_fractal(x + size, y - size, size / 2, depth - 1)


h_fractal(0, 0, 150, 4)
my_screen.clear()


'''
2)  Using the turtle library, create any of the other recursive patterns in the data folder. 
Challenge yourself to match your pattern as closely as you can to the image.  (15pts)
Note:  The Koch snowflake shows step by step building of the fractal.  
       The rectangle fractal example shows 4 possible drawings of the same fractal (choose any one)
'''


def escher_fractal(size, depth):
    if depth > 0:
        my_turtle.pencolor("black")
        my_turtle.down()
        my_turtle.forward(size)
        my_turtle.left(90)
        my_turtle.forward(size)
        my_turtle.left(90)
        my_turtle.forward(size)
        my_turtle.left(90)
        my_turtle.forward(size)
        my_turtle.left(90)
        my_turtle.forward(size / 2)
        my_turtle.left(45)
        escher_fractal((((size / 2) ** 2) + ((size / 2) ** 2)) ** .5, depth - 1)


my_turtle.goto(-300, -300)
escher_fractal(600, 15)
my_screen.clear()


'''
3)  Create your own work of art with a repeating pattern of your making.  
It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.  
Take this one as seriously as the points indicate.  Play around.  (3pt) 

Give all your fractals a depth of at least 4.  Ensure the recursive drawing is contained on the screen (at whatever size you set it).
All three recursive drawings can be on the same program.  Just use screen.clear() between problems.
 Have fun!
 
 Resource to help you out >>> https://docs.python.org/3.3/library/turtle
'''


def my_fractal(size, depth):
    my_turtle.pencolor("black")
    my_turtle.down()
    my_turtle.forward(size)
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.left(90)
    my_turtle.forward(size)
    my_turtle.left(90)
    my_turtle.left(45)
    my_fractal(size * .80, depth - 1)


my_turtle.home()
my_fractal(500, 5)



my_screen.exitonclick()

