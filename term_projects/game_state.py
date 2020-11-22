#game_state
import gfw
from pico2d import *
import gobj
from simon import Simon
from bullet import Bullet
from enemy import Enemy
from enemy_bullet import EnemyBullet
from background import BackgroundScroll
from background import FrontgroundScroll
from background import BiggroundScroll

canvas_width = 960
canvas_height = 720

def enter():
    #gfw.world.init(['bigground','background', 'enemy', 'simon', 'bullet', 'enemy_bullet', 'frontground'])
    gfw.world.init(['background', 'enemy', 'simon', 'bullet', 'enemy_bullet', 'frontground'])

    global simon
    simon = Simon()
    gfw.world.add(gfw.layer.simon, simon)
    # global bigground
    # bigground = BiggroundScroll('bigground_demo.png')
    # gfw.world.add(gfw.layer.bigground, bigground)
    global background
    background = BackgroundScroll('background.png')
    gfw.world.add(gfw.layer.background, background)    
    global frontground
    frontground = FrontgroundScroll('frontground.png')
    gfw.world.add(gfw.layer.frontground, frontground)
    #simon.pos = stage.center
    background.target = simon
    frontground.target = simon
    #bigground.target = simon
    #for i in range (3):
    global enemy
    #enemy = Enemy()
    #gfw.world.add(gfw.layer.enemy, enemy)

def check_enemy(e):
	if gobj.collides_box(simon, e):
		print('Player Collision', e)
		simon.die()
		return

	for eb in gfw.world.objects_at(gfw.layer.enemy_bullet):
		if gobj.collides_box(eb, simon):
			print('Enemy Attack Collision', eb, simon)
			simon.die()
			eb.remove()
			return

	for b in gfw.world.objects_at(gfw.layer.bullet):
		if gobj.collides_box(b, e):
			print('Enemy Collision', e, b)
			e.die()
			b.remove()
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
