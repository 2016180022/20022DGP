from pico2d import *
import random
import gfw
import gobj
import rect
from enemy_bullet import *

class WaitingState:
	@staticmethod
	def get(enemy):
		#if not hasattr(WaitingState, 'singleton'):
		WaitingState.singleton = WaitingState()
		WaitingState.singleton.enemy = enemy
		return WaitingState.singleton

	def __init__(self):
		self.wait_image = gfw.image.load(gobj.RES_DIR + 'sprite_soldier_waiting.png')

	def enter(self):
		self.time = 0
		self.frame = 0

	def exit(self):
		pass

	def draw(self):
		clip_width = 30
		clip_height = 40
		sx = self.frame * 30
		self.wait_image.clip_draw(sx, 0, clip_width, clip_height, self.enemy.pos_x, self.enemy.pos_y, self.enemy.sizeup_rate * clip_width, self.enemy.sizeup_rate * clip_height)

	def update(self):
		self.enemy.find_target()
		self.time += gfw.delta_time
		frame_number = 4
		frame = self.time * 6
		self.frame = int(frame) % frame_number
		#print('now wait')

class WalkingState:
	@staticmethod
	def get(enemy):
		#if not hasattr(WalkingState, 'singleton'):
		WalkingState.singleton = WalkingState()
		WalkingState.singleton.enemy = enemy
		return WalkingState.singleton

	def __init__(self):
		self.walk_image = gfw.image.load(gobj.RES_DIR + 'sprite_soldier_walking.png')

	def enter(self):
		self.time = 0
		self.frame = 0

	def exit(self):
		pass

	def draw(self):
		self.walking_rect = rect.ENEMY_WALKING_RECT[self.frame]
		self.walking_size = rect.ENEMY_WALKING_SIZE_RECT[self.frame]
		clip_height = 40
		self.walk_image.clip_draw(*self.walking_rect, self.enemy.pos_x, self.enemy.pos_y, self.walking_size, self.enemy.sizeup_rate * clip_height)

	def update(self):
		self.enemy.check_distance()
		x = self.enemy.pos_x
		dx = self.enemy.delta
		self.time += gfw.delta_time
		frame_number = 12
		frame = self.time * 8
		if frame < frame_number:
			self.frame = int(frame)
		else:
			self.enemy.set_state(WaitingState)
		x += dx * gfw.delta_time
		
		self.enemy.pos_x = x
		#print('now walk')

class KnifeState:
	@staticmethod
	def get(enemy):
		#if not hasattr(KnifeState, 'singleton'):
		KnifeState.singleton = KnifeState()
		KnifeState.singleton.enemy = enemy
		return KnifeState.singleton

	def __init__(self):
		self.knife_image = gfw.image.load(gobj.RES_DIR + 'sprite_soldier_knife.png')

	def enter(self):
		self.time = 0
		self.frame = 0
		self.toggle = True

	def exit(self):
		pass

	def draw(self):
		clip_height = 45
		self.knife_rect = rect.ENEMY_KNIFE_RECT[self.frame]
		self.knife_size = rect.ENEMY_KNIFE_SIZE_RECT[self.frame]
		self.knife_image.clip_draw(*self.knife_rect, self.enemy.pos_x, self.enemy.pos_y + 10, self.knife_size, self.enemy.sizeup_rate * clip_height)

	def update(self):
		self.time += gfw.delta_time
		frame_number = 12
		frame = self.time * 12
		if frame < frame_number:
			self.frame = int(frame)
		else:
			if self.enemy.cool_time(frame, frame_number):
				self.enemy.set_state(WaitingState)

		if self.toggle:
			if self.frame == 8:
				self.enemy.knife_attack(self.enemy.pos_x, self.enemy.pos_y, self.enemy.type)
				self.toggle = False


class GranadeState:
	@staticmethod
	def get(enemy):
		#if not hasattr(GranadeState, 'singleton'):
		GranadeState.singleton = GranadeState()
		GranadeState.singleton.enemy = enemy
		return GranadeState.singleton

	def __init__(self):
		self.granade_image = gfw.image.load(gobj.RES_DIR + 'sprite_soldier_granade.png')
		#self.enemy.off_attack()

	def enter(self):
		self.time = 0
		self.frame = 0
		self.toggle = True

	def exit(self):
		pass

	def draw(self):
		clip_height = 50
		self.granade_rect = rect.ENEMY_GRANADE_RECT[self.frame]
		self.granade_size = rect.ENEMY_GRANADE_SIZE_RECT[self.frame]
		self.granade_image.clip_draw(*self.granade_rect, self.enemy.pos_x, self.enemy.pos_y + 10, self.granade_size, self.enemy.sizeup_rate * clip_height)

	def update(self):
		self.time += gfw.delta_time
		frame_number = 14
		frame = self.time * 12
		if frame < frame_number:
			self.frame = int(frame)
		else:
			if self.enemy.cool_time(frame, frame_number):
				self.enemy.set_state(WaitingState)
		if self.toggle:
			if self.frame == 7:
				self.enemy.throw_granade(self.enemy.pos_x, self.enemy.pos_y, self.enemy.type)
				self.toggle = False

class DyingState:
	@staticmethod
	def get(enemy):
		#if not hasattr(DyingState, 'singleton'):
		DyingState.singleton = DyingState()
		DyingState.singleton.enemy = enemy
		return DyingState.singleton

	def __init__(self):
		self.dying_image = gfw.image.load(gobj.RES_DIR + 'sprite_soldier_dying.png')

	def enter(self):
		self.time = 0
		self.frame = 0

	def exit(self):
		print('now dyingstate called')

	def draw(self):
		clip_height = 39
		self.dying_rect = rect.ENEMY_DYING_RECT[self.frame]
		self.dying_size = rect.ENEMY_DYING_SIZE_RECT[self.frame]
		self.dying_image.clip_draw(*self.dying_rect, self.enemy.pos_x, self.enemy.pos_y + 10, self.dying_size, self.enemy.sizeup_rate * clip_height)

	def update(self):
		self.time += gfw.delta_time
		frame_number = 7
		frame = self.time * 12
		if frame < frame_number:
			self.frame = int(frame)
		else:
			self.enemy.remove()
		
class Enemy:
	def __init__(self):
		self.pos_x = random.randint(800, 900)
		self.pos_y = 280
		self.sizeup_rate = 3
		self.delta = 0
		self.state = None
		self.type = random.choice(['knife', 'granade'])
		#self.type = 'knife'
		#self.type = 'granade'
		layer = list(gfw.world.objects_at(gfw.layer.simon))
		self.simon = layer[0]
		self.speed = 80
		self.sight_range = 400
		self.knife_range = 30
		self.granade_range = 200
		self.frame = 0
		self.time = 0
		self.set_state(WaitingState)

	def set_state(self, cls):
		#if self.state != None:
			#self.state.exit()
		self.state = cls.get(self)
		self.state.enter()
		
	def find_target(self):
		x = self.pos_x
		tx, ty = self.simon.pos
		dx = x - tx

		if dx < self.sight_range:
			#print('target rock on')
			self.target_x = tx
			delta = -self.speed
			self.delta = delta
			self.set_state(WalkingState)

	def check_distance(self):
		x = self.pos_x
		tx, ty = self.simon.pos
		dx = x - tx

		if self.type == 'knife':
			if dx < self.knife_range:
				self.set_state(KnifeState)
		elif self.type == 'granade':
			if dx < self.granade_range:
				self.set_state(GranadeState)

	def cool_time(self, frame, frame_number):
		frame = frame
		frame_number = frame_number
		if frame > frame_number + 5:
			return True
		else:
			return

	def throw_granade(self, x, y, enemytype):
		enemy_bullet = EnemyBullet(x, y, enemytype)
		gfw.world.add(gfw.layer.enemy_bullet, enemy_bullet)
		print('now added granade')

	def knife_attack(self, x, y, enemytype):
		enemy_bullet = EnemyBullet(x, y, enemytype)
		gfw.world.add(gfw.layer.enemy_bullet, enemy_bullet)
		print('now added knife')

	def update(self):
		self.state.update()

	def draw(self):
		self.state.draw()

	def remove(self):
		gfw.world.remove(self)
		print('now removed')

	def die(self):
		self.set_state(DyingState)

	def get_bb(self):
		x = self.pos_x
		y = self.pos_y
		width = 40
		height = 60
		return x - width, y - height, x + width, y + height
