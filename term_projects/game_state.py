#game_state
import gfw
from pico2d import *
from gobj import *
from simon import Simon
from bullet import Bullet

def enter():
    global stage, simon
    stage = Stage()
    simon = Simon()

def update():
    simon.update()
    for b in Bullet.bullets: b.update()

def draw():
    stage.draw()
    simon.draw()
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
