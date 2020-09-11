#turtle_writename
import turtle as t

#natural width adjustment
t.width(5)

#direction def
down = -90
up = 90
right = 0
left = 180

#length def
len = 100

#leading adjust
leading_ad = False

#char leading
def char_leading():
	a,b = t.pos()
	if leading_ad == False:
		goto(a+1.6*len,b)
	else:
		goto(a+1.75*len,b)

#move to set position
def goto(a,b):
	t.penup()
	t.goto(a,b)
	t.pendown()

#move to start position
def goto_start():
	goto(-400,200)

#turnabout
def dir(a):
	t.setheading(a)

#end writing
def end():
	a,b = t.pos()
	goto(a,b-1.6*len)
	t.write("2016180022 박찬얼")
	t.hideturtle()
	t.exitonclick()

#funtion writing ㅂ(q)
def write_q():
	a,b = t.pos()
	dir(down)
	t.forward(len)
	dir(right)
	t.forward(0.7*len)
	dir(up)
	t.forward(len)
	goto(a,b-len/2)
	dir(right)
	t.forward(0.7*len)
	goto(a,b)

#funtion writing ㅏ(k)
def write_k():
	a,b = t.pos()
	if leading_ad == False:
		goto(a+1.05*len,b)
	else:
		goto(a+1.2*len,b)
	x,y = t.pos()
	dir(down)
	t.forward(len)
	goto(x,y-len/2)
	dir(right)
	t.forward(0.3*len)
	goto(a,b)

#funtion writing 받침 ㄱ(last_r)
def write_last_r():
	a,b = t.pos()
	goto(a+0.1*len,b-1.15*len)
	dir(right)
	t.forward(0.95*len)
	dir(down)
	t.forward(0.4*len)
	goto(a,b)

#funtion writing ㅊ(c)
def write_c():
	a,b = t.pos()
	goto(a+0.5*len,b)
	dir(down)
	t.forward(0.35*len)
	x,y = t.pos()
	goto(x-0.5*len, y)
	dir(right)
	t.forward(len)
	goto(x, y)
	t.goto(a,b-len)
	goto(x,y)
	t.goto(a+len,b-len)
	goto(a,b)

#funtion writing 받침 ㄴ(last_s)
def write_last_s():
	a,b = t.pos()
	goto(a+0.25*len,b-1.15*len)
	dir(down)
	t.forward(0.4*len)
	dir(right)
	t.forward(0.95*len)
	goto(a,b)

#funtion writing ㅇ(d)
def write_d():
	a,b = t.pos()
	goto(a+0.3*len, b-0.9*len)
	t.circle(0.4*len)
	goto(a,b)

#funtion writing ㅓ(j)
def write_j():
	a,b = t.pos()
	if leading_ad == False:
		goto(a+1.05*len,b)
	else:
		goto(a+1.2*len,b)
	x,y = t.pos()
	dir(down)
	t.forward(len)
	goto(x,y-len/2)
	dir(left)
	t.forward(0.3*len)
	goto(a,b)

#funtion writing 받침 ㄹ(last f)
def write_last_f():
	a,b = t.pos()
	goto(a+0.25*len,b-1.15*len)
	x,y = t.pos()
	dir(right)
	t.forward(0.95*len)
	t.goto(x,y-0.4*len)
	dir(right)
	t.forward(0.95*len)
	goto(a,b)

#t.speed(0)
goto_start()
write_q()
#leading_ad = False //base setting
write_k()
write_last_r()
char_leading()
write_c()
leading_ad = True
write_k()
write_last_s()
char_leading()
write_d()
#leading_ad = True //Keep leading
write_j()
write_last_f()
char_leading()
end()