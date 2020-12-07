#game_state
import gfw
import random
from pico2d import *
import gobj
from simon import Simon
from bullet import Bullet
from enemy import Enemy
from enemy_bullet import EnemyBullet
from background import BackgroundScroll
from background import FrontgroundScroll
from background import BiggroundScroll
import map_loader

canvas_width = 960
canvas_height = 720

STATE_IN_GAME, STATE_GAME_OVER = range(2)

def start_game():
	global state
	# if state != STATE_GAME_OVER:
	# 	return
	# 	print('not gameover')
	print('start game')
	simon.reset()
	background.reset()
	frontground.reset()
	bigground.reset()
	gfw.world.clear_at(gfw.layer.platform)
	gfw.world.clear_at(gfw.layer.enemy)
	gfw.world.clear_at(gfw.layer.bullet)
	gfw.world.clear_at(gfw.layer.enemy_bullet)

	state = STATE_IN_GAME
	
	map_loader.load()
	generate_enemy()

	music_bg.repeat_play()

def end_game():
	print('dead')
	global state
	state = STATE_GAME_OVER
	music_bg.stop()

def enter():
    gfw.world.init(['bigground','background', 'enemy', 'abigail', 'simon', 'bullet', 'enemy_bullet', 'frontground', 'ui', 'platform'])
    map_loader.load()

    global simon
    simon = Simon()
    gfw.world.add(gfw.layer.simon, simon)
    global bigground
    bigground = BiggroundScroll('bigground_demo.png')
    gfw.world.add(gfw.layer.bigground, bigground)
    global background
    background = BackgroundScroll('background.png')
    gfw.world.add(gfw.layer.background, background)    
    global frontground
    frontground = FrontgroundScroll('frontground.png')
    gfw.world.add(gfw.layer.frontground, frontground)
    background.target = simon
    frontground.target = simon
    bigground.target = simon

    global music_bg, wav_simon_dead, wav_enemy_dead1, wav_enemy_dead2

    music_bg = load_music('res/Midnight Wandering.mp3')
    wav_simon_dead = load_wav('res/P_EriDeath_old.wav')
    wav_enemy_dead1 = load_wav('res/P_ClarkDeath.wav')
    wav_enemy_dead2 = load_wav('res/P_MarcoDeath_old.wav')

    global enemy_die
    enemy_die = random.choice([wav_enemy_dead1, wav_enemy_dead2])

    music_bg.set_volume(30)
    wav_simon_dead.set_volume(10)
    enemy_die.set_volume(10)

    global game_over_image
    game_over_image = gfw.image.load('res/gameover.png')

    global state
    state = STATE_IN_GAME
    start_game()
    print('init')

def generate_enemy():
	count = 0
	for p in gfw.world.objects_at(gfw.layer.platform):
		if p.name == 'e':
			px, py = p.pos
			global enemy
			enemy = Enemy(px, py)
			background.set_enemy(enemy)
			gfw.world.add(gfw.layer.enemy, enemy)
			count += 1
			print(count)

def exit():
     global music_bg, wav_simon_dead, wav_enemy_dead1, wav_enemy_dead2

     del music_bg
     del wav_simon_dead
     del wav_enemy_dead1
     del wav_enemy_dead2

def check_enemy(e):
	if gobj.collides_box(simon, e):
		print('Player Collision', e)
		simon.die()
		wav_simon_dead.play()
		return

	for eb in gfw.world.objects_at(gfw.layer.enemy_bullet):
		if gobj.collides_box(eb, simon):
			print('Enemy Attack Collision', eb, simon)
			simon.die()
			wav_simon_dead.play()
			eb.remove()
			end_game()
			return

	for b in gfw.world.objects_at(gfw.layer.bullet):
		if gobj.collides_box(b, e):
			print('Enemy Collision', b, e)
			e.die()
			enemy_die.play()
			b.remove()
			return

def update():
    if simon.simon_die == True:
        print('simon_dead')
        end_game()
    #print(simon.simon_die)

    if state != STATE_IN_GAME:
        #print('not in game')
        return

    global enemy_count
    enemy_count = 0

    gfw.world.update()

    for e in gfw.world.objects_at(gfw.layer.enemy):
         check_enemy(e)
         enemy_count += 1
    #print('now enemy: ', enemy_count)

def draw():
    gfw.world.draw()
    #for b in Bullet.bullets: b.draw()
    #gobj.draw_collision_box()
    if state == STATE_GAME_OVER:
    	x = get_canvas_width() // 2
    	y = get_canvas_height() // 2
    	game_over_image.draw(x,y)

def handle_event(e):
    global simon
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        elif e.key == SDLK_RETURN:
        	start_game()
        	print('restart')

    simon.handle_event(e)

if __name__ == '__main__':
    gfw.run_main()
