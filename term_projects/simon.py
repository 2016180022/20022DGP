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

	def __init__(self):
		self.wait_image = gfw_image.load(RES_DIR + '/sprite_simon_waiting.png')
		self.walk_image = gfw_image.load(RES_DIR + '/sprite_simon_walking.png')

	def enter(self):
		self.time = 0
		self.frame = 0

	def exit(self):
		pass

	def draw(self):
		clip_width = 100
		clip_height = 40
		sx = self.frame * clip_width
		if self.simon.delta != (0, 0):
			self.walk_image.clip_draw(sx, 0, clip_width, clip_height, *self.simon.pos, 180, 80)
		else:
			self.wait_image.clip_draw(sx, 0, clip_width, clip_height, *self.simon.pos, 180, 80)

	def update(self):
		frame_number = 8
		self.time += gfw.delta_time
		move_obj(self.simon)
		if self.simon.delta == (0, 0):
			frame_number = 8
		else:
			frame_number = 10
		frame = self.time * 10
		self.frame = int(frame) % frame_number

	def handle_event(self, e):
		pair = (e.type, e.key)
		if pair in Simon.KEY_MAP:
			self.simon.delta = point_add(self.simon.delta, Simon.KEY_MAP[pair])
			if e.type == SDL_KEYUP: return			
		elif pair == Simon.KEYDOWN_SPACE:
			self.simon.shoot()
			self.simon.set_state(FireState)
		elif pair == Simon.KEYDOWN_C:
			self.simon.set_state(BackState)
		elif pair == Simon.KEYDOWN_X:
			self.simon.set_state(DyingState)

class FireState:
	@staticmethod
	def get(simon):
		if not hasattr(FireState, 'singleton'):
			FireState.singleton = FireState()
			FireState.singleton.simon = simon
		return FireState.singleton

	def __init__(self):
		self.image = gfw_image.load(RES_DIR + '/sprite_simon_firing.png')
		self.sfx_image = gfw_image.load(RES_DIR + '/sprite_simon_sfx.png')		

	def enter(self):
		self.time = 0
		self.frame = 0

	def exit(self):
		pass

	def draw(self):
		clip_width = 110
		clip_height = 40
		sx = self.frame * clip_width
		x, y = self.simon.pos
		self.image.clip_draw(sx, 0, clip_width, clip_height, *self.simon.pos, 180, 80)
		self.sfx_image.clip_draw(*self.src_rect, x + 85, y + 5, *self.src_large)
		self.sfx_image.clip_draw(*self.src_rect2, x + 55, y + 5, *self.src_large2)
		
	def update(self):
		self.time += gfw.delta_time
		frame = self.time * 10
		if frame < 10:
			self.frame = int(frame)
			self.src_rect = Simon.MUZZLE_RECT[int(frame)]
			self.src_large = Simon.MUZZLE_LARGE[int(frame)]
			self.src_rect2 = Simon.SMOKE_RECT[int(frame)]
			self.src_large2 = Simon.SMKOE_LARGE[int(frame)]
		else:
			self.simon.set_state(WaitingState)

	def handle_event(self, e):
		pair = (e.type, e.key)
		if pair in Simon.KEY_MAP:
			self.simon.delta = point_add(self.simon.delta, Simon.KEY_MAP[pair])
			if e.type == SDL_KEYUP: return

class DyingState:
	@staticmethod
	def get(simon):
		if not hasattr(DyingState, 'singleton'):
			DyingState.singleton = DyingState()
			DyingState.singleton.simon = simon
		return DyingState.singleton

	def __init__(self):
		self.image = gfw_image.load(RES_DIR + '/sprite_simon_dying.png')

	def enter(self):
		self.time = 0
		self.frame = 0

	def exit(self):
		pass

	def draw(self):
		clip_width = 60
		clip_height = 80
		x, y = self.simon.pos
		sx = self.frame * clip_width
		self.image.clip_draw(*self.src_rect, x - 50, y + 40, 120, 160)

	def update(self):
		self.time += gfw.delta_time
		frame = self.time * 10
		x, y = self.simon.pos
		if frame < 16:
			self.frame = int(frame)
			self.src_rect = Simon.DYING_RECT[int(frame)]
			x -= 0.1
		else:
			self.simon.set_state(WaitingState)
		self.simon.pos = x,y

	def handle_event(self, e):
		pair = (e.type, e.key)
		if pair in Simon.KEY_MAP:
			self.simon.delta = point_add(self.simon.delta, Simon.KEY_MAP[pair])
			if e.type == SDL_KEYUP: return

class BackState:
	@staticmethod
	def get(simon):
		if not hasattr(BackState, 'singleton'):
			BackState.singleton = BackState()
			BackState.singleton.simon = simon
		return BackState.singleton

	def __init__(self):
		self.image = gfw_image.load(RES_DIR + '/sprite_simon_backstep.png')

	def enter(self):
		self.time = 0
		self.frame = 0

	def exit(self):
		pass

	def draw(self):
		clip_width = 90
		clip_height = 60
		x, y = self.simon.pos
		sx = self.frame * clip_width
		self.image.clip_draw(sx, 0, clip_width, clip_height, x, y + 20, 180, 120)

	def update(self):
		self.time += gfw.delta_time
		x, y = self.simon.pos
		frame = self.time * 10
		if frame < 3:
			self.frame = int(frame)
			x -= 1
			y += 0.5
		elif frame < 6:
			self.frame = int(frame)
			x -= 1
			y -= 0.5
		else:
			self.simon.set_state(WaitingState)
		self.simon.pos = x, y

	def handle_event(self, e):
		pair = (e.type, e.key)
		if pair in Simon.KEY_MAP:
			self.simon.delta = point_add(self.simon.delta, Simon.KEY_MAP[pair])
			if e.type == SDL_KEYUP: return

class Simon:
	KEY_MAP = {
		(SDL_KEYDOWN, SDLK_LEFT):	(-1, 0),
		(SDL_KEYDOWN, SDLK_RIGHT):	(1, 0),
		(SDL_KEYUP, SDLK_LEFT):		(1, 0),
		(SDL_KEYUP, SDLK_RIGHT):	(-1, 0),
	}
	KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
	KEYDOWN_C = (SDL_KEYDOWN, SDLK_c)
	KEYDOWN_X = (SDL_KEYDOWN, SDLK_x)

	DYING_RECT = [
		(0, 0, 60, 80),
		(60, 0, 55, 80),
		(115, 0, 60, 80),
		(175, 0, 60, 80),
		(235, 0, 60, 80),
		(295, 0, 60, 80),
		(355, 0, 50, 80),
		(405, 0, 50, 80),
		(455, 0, 45, 80),
		(510, 0, 55, 80),
		(565, 0, 50, 80),
		(615, 0, 50, 80),
		(665, 0, 50, 80),
		(715, 0, 55, 80),
		(770, 0, 55, 80),
		(825, 0, 55, 80),
	]
	MUZZLE_RECT = [
		(0, 160, 14, 20),
		(14, 160, 28, 20),
		(42, 160, 50, 20),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0)
	]
	SMOKE_RECT = [
		(0, 100, 10, 50),
		(10, 100, 12, 50),
		(22, 100, 24, 50),
		(46, 100, 28, 50),
		(74, 100, 32, 50),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0),
		(0, 0, 0, 0)
	]
	MUZZLE_LARGE = [
		(21, 30),
		(42, 30),
		(75, 40),
		(0, 0),
		(0, 0),
		(0, 0),
		(0, 0),
		(0, 0),
		(0, 0),
		(0, 0)
	]
	SMKOE_LARGE = [
		(15, 75),
		(18, 75),
		(36, 75),
		(42, 75),
		(48, 75),
		(0, 0),
		(0, 0),
		(0, 0),
		(0, 0),
		(0, 0)
	]
	def __init__(self):
		self.pos = get_canvas_width() //2, get_canvas_height() //2 - 130
		self.delta = 0, 0
		self.time = 0
		self.state = None
		self.src_rect = []
		self.src_rect2 = []
		self.src_large = []
		self.src_large2 = []
		self.set_state(WaitingState)

	def set_state(self, cls):
		if self.state != None:
			self.state.exit()
		self.state = cls.get(self)
		self.state.enter()

	def draw(self):
		self.state.draw()

	def shoot(self):
		bullet = Bullet(self.pos)
		Bullet.bullets.append(bullet)


	def update(self):
		self.state.update()

	def handle_event(self, e):
		self.state.handle_event(e)