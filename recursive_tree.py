import turtle
t = turtle.Turtle()
turtle.screensize(10000,10000)
t.setheading(90)
t.speed(0)
t.pd()
t.hideturtle()

def tree(trunk_length, height):
    """if(height == -1):
        t.setposition(0,0)
        t.setheading(90)
        t.backward()"""
    if height  == 0:
        return
    else:
        #making a Y
        t.width(1)
        angle = t.heading()
        t.pu()
        t.backward(trunk_length)
        t.pd()
        t.forward(trunk_length)
        t.left(40)
        t.forward(trunk_length)
        tree(trunk_length/1.5, height-1)
        t.backward(trunk_length)
        t.right(80)
        t.forward(trunk_length)
        tree(trunk_length/1.5, height-1)
        t.backward(trunk_length)
        t.setheading(angle)


'''def treeAngle(trunk_length, height, angle = 0):
    
    if height  == 0:
        return
    else:
        #making a v
        angleX = t.heading()
        t.left(angle)
        t.forward(trunk_length)
        treeAngle(trunk_length//2, height-1,angle//2+30)
        t.backward(trunk_length)
        t.right(2*angle)
        t.forward(trunk_length)
        treeAngle(trunk_length//2, height-1,angle//2+30)
        t.backward(trunk_length)
        t.setheading(angleX)

def treeHeight(trunk_length, height, initHeight = 0):
    if height  == 0:
            return
    else:
        #making a v
        angle = t.heading()
        t.left(30)
        t.forward(trunk_length)
        tree(trunk_length//2, height-1, initHeight+1)
        t.backward(trunk_length)
        t.right(90)
        t.forward(trunk_length)
        tree(trunk_length//2, height-1 , initHeight+1)
        t.backward(trunk_length)
        t.setheading(angle)
    '''
