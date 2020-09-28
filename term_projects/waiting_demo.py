#waiting demo
from pico2d import *

open_canvas(800, 600)

simon = load_image("sprite_simon.png")
back = load_image("background_demo.png")

def handle_events():
	global running
	global x, y
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN:
			if event.key == SDLK_ESCAPE:
				running = False

running = True
frame = 0
x, y = 400, 300
clip_x, clip_y = float(86),float(40)
while (running):
	clear_canvas()
	back.draw(400,345)
	simon.clip_draw(7 + frame * int(clip_x), 988, int(clip_x), int(clip_y), x, y)
	update_canvas()
	frame = (frame + 1) % 8
	delay(0.3)
	handle_events()

close_canvas()