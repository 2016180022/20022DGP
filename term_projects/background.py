#added at 201122
import gfw
from pico2d import *
from gobj import *
from simon import Simon

class Background:
	def __init__(self, imageName):
		self.imageName = imageName
		self.image = gfw.image.load(RES_DIR + imageName)
		self.target = None
		cw, ch = get_canvas_width(), get_canvas_height()
		self.win_rect = 0, 0, cw, ch
		self.center = self.image.w // 2, self.image.h //2

	def set_target(self, target):
		self.target = target
		self.upadte()

	def draw(self):
		self.image.clip_draw_to_origin(*self.win_rect, 0, 0)

	def update(self):
		if self.target is None:
			return
		tx, ty = self.target.pos
		cw, ch = get_canvas_width(), get_canvas_height()
		sl = round(tx - cw / 2)
		sb = round(ty - ch / 2)
		self.win_rect = sl, sb, cw, ch

class BackgroundScroll:
	def __init__(self, imageName):
		self.imageName = imageName
		self.image = gfw.image.load(RES_DIR + imageName)
		self.cw, self.ch = get_canvas_width()//3, get_canvas_height()//3
		self.il = 0
		self.ib = 680
		self.enemy = None

	def set_target(self, target):
		self.target = target
		self.upadte()

	def set_enemy(self, enemy):
		self.enemy = enemy
		self.update()

	def update(self):
		if self.target is None:
			return
		if self.enemy is None:
			return
		#tx, ty = self.target.pos
		tx, ty = self.target.draw_pos
		ex, ey = self.enemy.pos_x, self.enemy.pos_y
		if tx > get_canvas_width() * 3 // 4:
			self.set_scroll(tx, ty, ex, ey)
		#print('before scrolled, ex ey:', ex, ey)

	def set_scroll(self, tx, ty, ex, ey):
		self.il += 125
		tx -= 500
		ex -= 500
		#self.target.pos = tx, ty
		self.target.draw_pos = tx, ty
		self.enemy.pos_x, self.enemy.pos_y = ex, ey
		#print('scroll called')
		#print('after scrolled, ex ey: ', ex, ey)
		#want frame per scroll animation

	def draw(self):
		#left, bottom, image size_x, image size_y, pos_x, pos_y, draw size_x, draw size_y
		rtx, rty = self.target.pos
		tx, ty = self.target.draw_pos
		dty = ty - 490
		if rtx > 8100:
			self.ib = 400 + int(dty//4)
		elif rtx > 7300:
			self.ib = 500 + int(dty//4)
		elif rtx > 6010:
			self.ib = 600 + int(dty//4)
		else:
			self.ib = 680 + int(dty//4)
		#print(dty)
		sx = self.cw * 3
		sy = self.ch * 6
		px, py = 0, 0
		dx = 4 * sx
		dy = sy
		#ddty = dty
		self.image.clip_draw_to_origin(self.il, self.ib, sx, sy, px, py, dx, dy)

	def reset(self):
		global il, ib
		self.il, self.ib = 0, 680
		il, ib = self.il, self.ib

class FrontgroundScroll:
	def __init__(self, imageName):
		self.imageName = imageName
		self.image = gfw.image.load(RES_DIR + imageName)
		self.cw, self.ch = get_canvas_width()//3, get_canvas_height()//3
		self.il = 0

	def set_target(self, target):
		self.target = target
		self.upadte()

	def update(self):
		if self.target is None:
			return
		#tx, ty = self.target.pos
		tx, ty = self.target.draw_pos
		if tx > get_canvas_width() * 3 // 4:
			self.set_scroll(tx, ty)

	def set_scroll(self, tx, ty):
		self.il += 125
		#tx -= 500
		#self.target.pos = tx, ty
		print('scroll called')
		#want frame per scroll animation

	def draw(self):
		#left, bottom, image size_x, image size_y, pos_x, pos_y, draw size_x, draw size_y
		tx, ty = self.target.draw_pos
		dty = ty - 490
		self.ib = 680 + int(dty//4)
		sx = self.cw * 3
		sy = self.ch * 6
		px, py = 0, 0
		dx = 4 * sx
		dy = sy
		self.image.clip_draw_to_origin(self.il, self.ib, sx, sy, px, py, dx, dy)

	def reset(self):
		global il, ib
		self.il, self.ib = 0, 680
		il, ib = self.il, self.ib

class BiggroundScroll:
	def __init__(self, imageName):
		self.imageName = imageName
		self.image = gfw.image.load(RES_DIR + imageName)
		self.cw, self.ch = get_canvas_width()//3, get_canvas_height()//3
		self.spos = get_canvas_width() //2 - 400
		self.il = 0

	def set_target(self, target):
		self.target = target
		self.upadte()

	def update(self):
		if self.target is None:
			return
		#tx, ty = self.target.pos
		tx, ty = self.target.draw_pos
		self.set_scroll(tx, ty)
		#print('now tx', tx)

	def set_scroll(self, tx, ty):
		#rounding
		il = int((tx - self.spos)//6)
		self.il = il
		#print(self.il)
		
	def draw(self):
		#left, bottom, image size_x, image size_y, pos_x, pos_y, draw size_x, draw size_y
		ib = 0
		sx = int(self.il + self.cw * 3)
		sy = int(ib + self.ch * 3)
		px, py = 0, 0
		dx = sx * 3
		dy = sy
		self.image.clip_draw_to_origin(self.il, ib, sx, sy, px, py, dx, dy)

	def reset(self):
		global il
		self.il = 0
		il = self.il