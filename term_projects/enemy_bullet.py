#add at 201121
from pico2d import *
from gobj import *
import gfw
import rect

class EnemyBullet:
	def __init__(self, x, y, enemytype):
		self.x, self.y = x, y
		self.type = enemytype
		self.delta = 0.1
		self.granade_image = gfw.image.load(RES_DIR + 'sprite_enemy_granade.png')
		self.time = 0
		self.knife_toggle = True

	def draw(self):
		if self.type == 'granade':
			self.granade_draw()

	def granade_draw(self):
		self.enemy_granade_rect = rect.ENEMY_GRANADE_WEAPON_RECT[self.frame]
		self.enemy_granade_size = rect.ENEMY_GRANADE_WEAPON_SIZE_RECT[self.frame]
		self.granade_image.clip_draw(*self.enemy_granade_rect, self.x, self.y, *self.enemy_granade_size)

	def update(self):
		if self.type == 'granade':
			self.granade_update()
		elif self.type == 'knife':
			self.knife_update()

	def granade_update(self):
		x, y = self.x, self.y
		self.time += gfw.delta_time
		frame_number = 10
		frame = self.time * 8
		if frame < frame_number:
			self.frame = int(frame)
		else:
			self.remove()
		#print('nowframe is ', frame)
		self.go_houbutsusen(x, y, self.frame, self.delta)

	def knife_update(self):
		if self.knife_toggle:
			self.x -= 50
			self.y += 30
			self.knife_toggle = False
		self.time += gfw.delta_time
		frame_number = 5
		frame = self.time * 8
		if frame < frame_number:
			self.frame = int(frame)
		else:
			self.remove()

	def remove(self):
		gfw.world.remove(self)
		print('now removed')

	def get_bb(self):
		size = 50
		hw = size //2
		hh = size //2
		return self.x - hw, self.y - hh, self.x + hw, self.y + hh

	def go_houbutsusen(self, x, y, frame, delta):
		accel = 0.1
		if frame < 5:
			delta += accel
			y += 3
			x -= delta
		else:
			delta -= accel
			y -= 3
			x -= delta
		self.x, self.y = x, y
		self.delta = delta

