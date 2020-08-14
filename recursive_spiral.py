import turtle
t = turtle.Turtle()
turtle.screensize(1000,1000)

def spiral(initial_length, angle, multiplier):
    t.pd()
    if multiplier < 1:
        if initial_length <= 1:
            return
    elif multiplier > 1:
        if initial_length >= 200:
            return
    
    t.forward(initial_length)
    t.right(angle)
    spiral(initial_length*multiplier, angle, multiplier)