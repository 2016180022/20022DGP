from pico2d import *
import random
import gfw
import gobj

class Enemy:
	ACTIONS = ['waiting', 'walking', 'knife_attack', 'granade_attack']
	images = {}
	FPS = 4
	#FCOUNT = 10
	def __init__(self):
		self.pos = 1040, 280
		self.delta = 0
		self.find_nearest_player()
		char = random.choice(['Knife', 'Granade'])
		self.attack(char)
		self.action = 'Wait'
		self.speed = 10
		self.fidx = 0
		self.frame = 0
		self.time = 0
		self.wait_image = gfw.image.load(gobj.RES_DIR + '/sprite_soldier_waiting.png')
		self.walk_image = gfw.image.load(gobj.RES_DIR + '/sprite_soldier_walking.png')

	def find_nearest_player(self):
		pass

	def set_target(self, target):
		pass

	# def load_images(self):
	# 	images = {}
	# 	file_fmt = '%s/sprite_soldier_%s.png'
	# 	while True:
	# 		fn = file_fmt % (gobj.RES_DIR, action)
	# 		try:
	# 			images.append(gfw.image.load(fn))
	# 		except IOError:
	# 			break;
	# 	self.images = images

	def attack(self, char):
		pass

	def update(self):
		frame_number = 4
		self.time += gfw.delta_time
		#self.fidx = round(self.time * Enemy.FPS)
		x,y = self.pos
		dx = self.delta

		if self.delta == 0:
			frame_number = 4
		else:
			frame_number = 12
		frame = self.time * 2
		self.frame = int(frame) % frame_number

		x += dx * self.speed * gfw.delta_time
		# print(self.pos, self.delta, x, y, dx)

		done = False

		# tx, ty = self.target
		# if dx > 0 and x >= tx or dx < 0 aand x <= tx:
		# 	x = tx
		# 	done = True

		self.pos = x, y

		if done:
			pass

	def draw(self):
		image = self.wait_image
		sx = self.frame * 30
		image.clip_draw(sx, 0, 30, 40, *self.pos, 87, 116)