#move character with mouse
from pico2d import *

WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)

grass = load_image('grass.png')
character = load_image('run_animation.png')


#esc handle event
def handle_events():
	global running
	global x, y
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_MOUSEMOTION:
			x, y = event.x, HEIGHT - 1 - event.y
		elif event.type == SDL_KEYDOWN:
			if event.key == SDLK_ESCAPE:
				running = False

running = True
x = WIDTH//2
y = HEIGHT//2
frame = 0
hide_cursor()
while (running):
	clear_canvas()
	#grass.draw(400, 30)
	character.clip_draw(frame * 100, 0, 100, 100, x, y)
	update_canvas()
	frame = (frame + 1) % 8
	delay(0.01)
	handle_events()

close_canvas()