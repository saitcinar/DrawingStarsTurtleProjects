import turtle
drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Stars Python Turtle")
turtle_instance = turtle.Turtle()
for i in range(60):
    turtle_instance.forward(200)
    turtle_instance.backward(200)
    turtle_instance.left(6)
turtle.done()
