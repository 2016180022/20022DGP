#turtle_make_grid
import turtle as t

#direction def
down = -90
up = 90
right = 0
left = 180

#length def
len = 100

#grid cells
grid_cells_v = 5 #long vertical rantangle
grid_cells_s = 5 #long side rantangle

#move to set position
def goto(a,b):
	t.penup()
	t.goto(a,b)
	t.pendown()

#move to start position
def goto_start():
	goto(-400,300)

#turnabout
def dir(a):
	t.setheading(a)

#end writing
def end():
	a,b = t.pos()
	goto(a,b+0.1*len)
	t.write("2016180022 박찬얼")
	t.hideturtle()
	t.exitonclick()

#draw horizon
def draw_hor():
	a,b = t.pos()
	for i in range(grid_cells_v+1):
		dir(right)
		t.forward(grid_cells_s*len)
		goto(a,b-(i+1)*len)
	goto(a,b)

#draw vertical
def draw_ver():
	a,b = t.pos()
	for i in range(grid_cells_s+1):
		dir(down)
		t.forward(grid_cells_v*len)
		goto(a+(i+1)*len,b)
	goto(a,b)

t.speed(0)
goto_start()
draw_hor()
draw_ver()
end()
