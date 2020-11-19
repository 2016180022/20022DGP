from pico2d import *
import random
import gfw
import gobj
import rect

class Enemy:
	ACTIONS = ['waiting', 'walking', 'knife_attack', 'granade_attack']
	images = {}
	
	#FCOUNT = 10
	def __init__(self):
		self.pos_x = 1040
		self.delta = 0
		#self.type = random.choice(['knife', 'granade'])
		self.type = 'granade'
		self.action = 'waiting'
		layer = list(gfw.world.objects_at(gfw.layer.simon))
		self.simon = layer[0]
		self.speed = 80
		self.sight_range = 400
		self.knife_range = 50
		self.granade_range = 100
		self.frame = 0
		self.time = 0
		self.wait_image = gfw.image.load(gobj.RES_DIR + '/sprite_soldier_waiting.png')
		self.walk_image = gfw.image.load(gobj.RES_DIR + '/sprite_soldier_walking.png')
		self.knife_image = gfw.image.load(gobj.RES_DIR + '/sprite_soldier_knife.png')
		self.granade_image = gfw.image.load(gobj.RES_DIR + '/sprite_soldier_granade.png')

	def find_target(self):
		x = self.pos_x
		tx, ty = self.simon.pos
		dx = x - tx

		if self.action == 'waiting':
			if dx < self.sight_range:
				self.action = 'walking'
				self.target_x = tx
				delta = -self.speed
				self.delta = delta

		if self.action == 'walking':
			if self.type == 'knife':
				if dx < self.knife_range:
					self.action = 'knife_attack'
					self.frame = 0
					self.attack()
			elif self.type == 'granade':
				if dx < self.granade_range:
					self.action = 'granade_attack'
					self.frame = 0
					self.attack()

	def attack(self):
		self.delta = 0

	def frame_over(self, frame):
		type_frame = frame
		if self.type == 'knife':
			if type_frame > 12:
				self.action == 'waiting'
		elif self.type == 'granade':
			if type_frame > 14:
				self.action == 'waiting'

	def frame_check(self):
		if self.action == 'waiting':
			frame_number = 4
			frame = self.time * 2
		elif self.action == 'walking':
			frame_number = 12
			frame = self.time * 8
		elif self.action == 'knife_attack':
			frame_number = 12
			frame = self.time * 8
		elif self.action == 'granade_attack':
			frame_number = 14
			frame = self.time * 10

		self.frame_over(int(frame))
		self.frame = int(frame) % frame_number
		#print("nowframe is ", frame)


	def fill_rect(self):
		if self.action == 'walking':
			self.walking_rect = rect.ENEMY_WALKING_RECT[self.frame]
			self.walking_size = rect.ENEMY_WALKING_SIZE_RECT[self.frame]
		elif self.action == 'knife_attack':
			self.knife_rect = rect.ENEMY_KNIFE_RECT[self.frame]
			self.knife_size = rect.ENEMY_KNIFE_SIZE_RECT[self.frame]
		elif self.action == 'granade_attack':
			self.granade_rect = rect.ENEMY_GRANADE_RECT[self.frame]
			self.granade_size = rect.ENEMY_GRANADE_SIZE_RECT[self.frame]

	def update(self):
		self.find_target()
		self.time += gfw.delta_time
		#self.fidx = round(self.time * Enemy.FPS)
		x = self.pos_x
		dx = self.delta

		self.frame_check()
		self.fill_rect()
		x += dx * gfw.delta_time
		# print(self.pos, self.delta, x, y, dx)

		self.pos_x = x


	def draw(self):
		if self.action == 'waiting':
			image = self.wait_image
			sx = self.frame * 30
			image.clip_draw(sx, 0, 30, 40, self.pos_x, 280, 87, 116)
		elif self.action == 'walking':
			image = self.walk_image
			image.clip_draw(*self.walking_rect, self.pos_x, 280, self.walking_size, 110)
		elif self.action == 'knife_attack':
			image = self.knife_image
			image.clip_draw(*self.knife_rect, self.pos_x, 280, self.knife_size, 130)
		elif self.action == 'granade_attack':
			image = self.granade_image
			image.clip_draw(*self.granade_rect, self.pos_x, 280, self.granade_size, 150)