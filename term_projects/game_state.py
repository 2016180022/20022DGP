#game_state
import gfw
from pico2d import *
import gobj
from simon import Simon
from bullet import Bullet
from enemy import Enemy

canvas_width = 1280
canvas_height = 960

def enter():
    gfw.world.init(['stage', 'enemy', 'simon', 'bullet'])
    global simon
    simon = Simon()
    gfw.world.add(gfw.layer.simon, simon)

    stage = gobj.ImageObject('background_demo.png', 720, 392, 1920, 640)
    gfw.world.add(gfw.layer.stage, stage)
    #for i in range (3):
    global enemy
    enemy = Enemy()
    gfw.world.add(gfw.layer.enemy, enemy)

def check_enemy(e):
	if gobj.collides_box(simon, e):
		print('Player Collision', e)
		simon.die()
		return

	for b in gfw.gfw.world.objects_at(gfw.layer.bullet):
			if gobj.collides_box(b, e):
				print('Enemy Collision', e, b)
				#e.remove()
				return

def update():
    gfw.world.update()

    for e in gfw.world.objects_at(gfw.layer.enemy):
    	check_enemy(e)


def draw():
    gfw.world.draw()
    #for b in Bullet.bullets: b.draw()
    gobj.draw_collision_box()

def handle_event(e):
    global simon
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    simon.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
