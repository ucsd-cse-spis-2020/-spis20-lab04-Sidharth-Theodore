import turtle
t = turtle.Turtle()
turtle.screensize(1000,1000)


def snowflake(side_length, level, side_count,inv_side_count = 0):
    if side_count == 0:
        return
    else:
        snowflake_side(side_length,level)
        t.right(360//(side_count+inv_side_count))
        snowflake(side_length,level, side_count-1, inv_side_count+1)


def snowflake_side(side_length,level):
    if level == 0:
        t.forward(side_length)
    else:
        snowflake_side(side_length/3, level-1)
        t.left(60)
        snowflake_side(side_length/3, level-1)
        t.right(120)
        snowflake_side(side_length/3, level-1)
        t.left(60)
        snowflake_side(side_length/3, level-1)
