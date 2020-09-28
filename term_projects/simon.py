#Simon
from pico2d import *
from gobj import *
from bullet import Bullet
import gfw_image

class Simon:
	KEY_MAP = {
		(SDL_KEYDOWN, SDLK_LEFT):	(-3, 0),
		(SDL_KEYDOWN, SDLK_RIGHT):	(3, 0),
		(SDL_KEYUP, SDLK_LEFT):		(3, 0),
		(SDL_KEYUP, SDLK_RIGHT):	(-3, 0),
	}
	KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)

	#ACT_STATE
	act_rwait = 988
	#act_lwait = ?
	act_rmove = 909
	#act_lmove = ?
	act_shot = 830

	#FRAME_STATE
	fra_wait = 8
	fra_move = 10
	fra_shot = 10

	image = None
	frame = 0
	clip_x = 100
	clip_y = 40
	now_shoot = False
	shot_frame = 0

	def __init__(self):
		self.pos = get_canvas_width() //2, get_canvas_height() //2 - 130
		self.act = self.act_rwait				#y = 988
		self.delta = 0, 0
		self.fra = self.fra_wait
		if Simon.image == None:
			Simon.image = gfw_image.load("sprite_simon.png")

	def draw(self):
		sx = 7 + self.frame * self.clip_x
		sy = self.act
		self.image.clip_draw(sx, sy, self.clip_x, self.clip_y, *self.pos, 180, 80)

	def shoot(self):
		bullet = Bullet(self.pos)
		Bullet.bullets.append(bullet)
		self.now_shoot = True
		self.frame = 0
		self.fra = self.fra_shot
		self.update_Action(0,0)

	def update(self):
		if self.shot_frame > 8:
			self.now_shoot = False
			self.shot_frame = 0
			self.act = self.act_rwait
			self.fra = self.fra_wait
		if self.now_shoot == True:
			self.shot_frame += 1
		x, y = self.pos
		dx, dy = self.delta
		self.pos = x + dx, y + dy
		self.frame = (self.frame + 1) % self.fra
		delay(0.05)

	def update_Delta(self, ddx, ddy):
		dx, dy = self.delta
		dx += ddx
		if ddx != 0:
			self.update_Action(dx, ddx)
		self.delta = dx, dy

	def update_Action(self, dx, ddx):
		if self.now_shoot == True:
			self.act = self.act_shot
		else:
			self.act = self.act_rmove if dx != 0 else self.act_rwait
				#act_lmove if dx < 0 else\
				#act_rmove if dx > 0 else\
				#act_rwait if ddx > 0 else act_lwait

	def handle_event(self, e):
		pair = (e.type, e.key)
		if pair in Simon.KEY_MAP:
			self.update_Delta(*Simon.KEY_MAP[pair])
		elif pair == Simon.KEYDOWN_SPACE:
			self.shoot()