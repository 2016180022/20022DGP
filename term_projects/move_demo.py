#move_demo
from pico2d import *
import gfw_image

open_canvas(800, 600)

simon = load_image("sprite_simon.png")
back = load_image("background_demo.png")

def handle_events():
	global running
	global dir
	global frame
	global action
	global go_shot
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN:
			if event.key == SDLK_ESCAPE:
				running = False
			elif event.key == SDLK_RIGHT:
				dir += 1
				action = 909
			elif event.key == SDLK_LEFT:
				dir -= 1
				action = 909
			elif event.key == SDLK_SPACE:
				go_shot = True;
		elif event.type == SDL_KEYUP:
			if event.key == SDLK_RIGHT:
				dir -= 1
				action = 988
			elif event.key == SDLK_LEFT:
				dir += 1
				action = 988

running = True
go_shot = False
frame = 0
x, y = 400, 300
dir = 0
action = 988
shot = 0
clip_x, clip_y = float(90),float(40)
while (running):
	clear_canvas()
	back.draw(400,345)
	if go_shot == True:
		shot += 1
		action = 830
		frame = shot
		print ('shot!')
		if shot == 10:
			action = 988
			shot = 0
			go_shot = False
	frame = (frame + 1) % 10
	simon.clip_draw(7 + frame * int(clip_x), action, int(clip_x), int(clip_y), x, y)
	update_canvas()

	x += dir * 5
	delay(0.1)
	handle_events()

close_canvas()