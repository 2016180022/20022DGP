#Simon
from pico2d import *
from gobj import *
from bullet import Bullet
import gfw_image
import gfw

class WaitingState:
	@staticmethod
	def get(simon):
		if not hasattr(WaitingState, 'singleton'):
			WaitingState.singleton = WaitingState()
			WaitingState.singleton.simon = simon
		return WaitingState.singleton

	def draw(self):
		clip_width = 100
		clip_height = 40
		sx = self.simon.frame * clip_width
		self.simon.wait_image.clip_draw(sx, 0, clip_width, clip_height, *self.simon.pos, 180, 80)

	def update(self):
		self.simon.time += gfw.delta_time
		self.simon.pos = point_add(self.simon.pos, self.simon.delta)
		frame = self.simon.time * 10
		self.simon.frame = int(frame) % 8

	def handle_event(self, e):
		pair = (e.type, e.key)
		if pair in Simon.KEY_MAP:
			self.simon.delta = point_add(self.simon.delta, Simon.KEY_MAP[pair])
		elif pair == Simon.KEYDOWN_SPACE and self.simon.shot_ready == True:
			self.simon.shoot()
			self.nowstate = 'fire'

class WalkingState:
	@staticmethod
	def get(simon):
		if not hasattr(WalkingState, 'singleton'):
			WalkingState.singleton = WalkingState()
			WalkingState.singleton.simon = simon
		return WalkingState.singleton

	def draw(self):
		clip_width = 100
		clip_height = 40
		sx = self.simon.frame * clip_width
		self.simon.walk_image.clip_draw(sx, 0, clip_width, clip_height, *self.simon.pos, 180, 80)

	def update(self):
		self.simon.time += gfw.delta_time
		self.simon.pos = point_add(self.simon.pos, self.simon.delta)
		frame = self.simon.time * 10
		self.simon.frame = int(frame) % 10
		if self.simon.delta == (0, 0):
			self.simon.state = WaitingState.get(self.simon)
			self.simon.nowstate = 'wait'

	def handle_event(self, e):
		pair = (e.type, e.key)
		if pair in Simon.KEY_MAP:
			self.simon.delta = point_add(self.simon.delta, Simon.KEY_MAP[pair])
		elif pair == Simon.KEYDOWN_SPACE and self.simon.shot_ready == True:
			self.simon.shoot()
			self.nowstate = 'fire'

class FireState:
	@staticmethod
	def get(simon):
		if not hasattr(FireState, 'singleton'):
			FireState.singleton = FireState()
			FireState.singleton.simon = simon
		return FireState.singleton

	def draw(self):
		clip_width = 110
		clip_height = 40
		sx = self.simon.frame * clip_width
		self.simon.fire_image.clip_draw(sx, 0, clip_width, clip_height, *self.simon.pos, 180, 80)

	def update(self):
		self.simon.coolTime()
		self.simon.time += gfw.delta_time
		frame = self.simon.time * 8
		if frame < 8:
			self.simon.frame = int(frame)
		else:
			self.simon.time = 0
			self.simon.state = WaitingState.get(self.simon)

	def handle_event(self, e):
		pass

class Simon:
	KEY_MAP = {
		(SDL_KEYDOWN, SDLK_LEFT):	(-1, 0),
		(SDL_KEYDOWN, SDLK_RIGHT):	(1, 0),
		(SDL_KEYUP, SDLK_LEFT):		(1, 0),
		(SDL_KEYUP, SDLK_RIGHT):	(-1, 0),
	}
	KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)

	# #ACT_STATE
	# act_rwait = 988
	# #act_lwait = ?
	# act_rmove = 909
	# #act_lmove = ?
	# act_shot = 830

	##FRAME_STATE
	#fra_wait = 8
	#fra_move = 10
	#fra_shot = 10

	#image = None
	#frame = 0
	#clip_x = 100
	#clip_y = 40
	#now_shoot = False
	shot_ready = True
	#shot_frame = 0
	cooltime_frame = 0
	

	def __init__(self):
		self.pos = get_canvas_width() //2, get_canvas_height() //2 - 130
		#self.act = self.act_rwait				#y = 988
		self.delta = 0, 0
		#self.fra = self.fra_wait
		self.time = 0
		self.state = WaitingState.get(self)
		self.nowstate = 'wait'
		self.wait_image = gfw_image.load(RES_DIR + '/sprite_simon_waiting.png')
		self.walk_image = gfw_image.load(RES_DIR + '/sprite_simon_walking.png')
		self.fire_image = gfw_image.load(RES_DIR + '/sprite_simon_firing.png')
		#if Simon.image == None:
		#	Simon.image = gfw_image.load("sprite_simon.png")

	def draw(self):
		#sx = 7 + self.frame * self.clip_x
		#sy = self.act
		#self.image.clip_draw(sx, sy, self.clip_x, self.clip_y, *self.pos, 180, 80)
		self.state.draw()

	def shoot(self):
		self.state = FireState.get(self)
		bullet = Bullet(self.pos)
		Bullet.bullets.append(bullet)
		
		#self.now_shoot = True
		#self.frame = 0
		#self.fra = self.fra_shot
		#self.update_Action(0,0)

	def coolTime(self):
		if self.state == WaitingState:
		#if self.nowstate != 'fire':
			self.shot_ready = False
			print('now cooltime')
		if self.cooltime_frame > 20:
			self.shot_ready = True
			self.cooltime_frame = 0
			print('shot ready')
		self.cooltime_frame += 1

	# def update_Shootframe(self):
	# 	if self.shot_frame > 8:
	# 		self.now_shoot = False
	# 		self.shot_frame = 0
	# 		self.act = self.act_rwait
	# 		self.fra = self.fra_wait
	# 	if self.now_shoot == True:
	# 		self.shot_frame += 1
	# 	self.coolTime()

	def update(self):
		# self.update_Shootframe()
		# self.time += gfw.delta_time
		# self.pos = point_add(self.pos, self.delta)
		# self.frame = (self.frame + 1) % self.fra
		# delay(0.05)
		self.state.update()

	# def update_Delta(self, ddx, ddy):
	# 	dx, dy = self.delta
	# 	dx += ddx
	# 	if ddx != 0:
	# 		self.update_Action(dx, ddx)
	# 	self.delta = dx, dy

	# def update_Action(self, dx, ddx):
	# 	if self.now_shoot == True:
	# 		self.act = self.act_shot
	# 	else:
	# 		self.act = self.act_rmove if dx != 0 else self.act_rwait
	# 			#act_lmove if dx < 0 else\
	# 			#act_rmove if dx > 0 else\
	# 			#act_rwait if ddx > 0 else act_lwait

	def handle_event(self, e):
		# pair = (e.type, e.key)
		# if pair in Simon.KEY_MAP:
		# 	self.update_Delta(*Simon.KEY_MAP[pair])
		# elif pair == Simon.KEYDOWN_SPACE and self.shot_ready == True:
		# 	self.shoot()
		self.state.handle_event(e)