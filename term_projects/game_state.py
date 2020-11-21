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
    gfw.world.init(['stage', 'enemy', 'simon'])
    global simon
    simon = Simon()
    gfw.world.add(gfw.layer.simon, simon)

    stage = gobj.ImageObject('background_demo.png', 720, 392, 1920, 640)
    gfw.world.add(gfw.layer.stage, stage)
    #for i in range (3):
    global enemy
    enemy = Enemy()
    gfw.world.add(gfw.layer.enemy, enemy)

def update():
    gfw.world.update()
    for b in Bullet.bullets: b.update()

def draw():
    gfw.world.draw()
    for b in Bullet.bullets: b.draw()

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
