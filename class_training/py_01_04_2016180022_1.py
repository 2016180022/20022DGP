#character moves
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

#game loop
x = 0
while (x < 800):
	#game rendering
	clear_canvas_now()
	grass.draw_now(400, 30)
	character.draw_now(x, 85)
	#game logic
	x = x + 2
	
	delay(0.01)

close_canvas()