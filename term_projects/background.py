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
		self.ib = 660

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
		tx -= 500
		#self.target.pos = tx, ty
		self.target.draw_pos = tx, ty
		#enemy의 위치도 스크롤링 해야 함
		print('scroll called')
		#want frame per scroll animation

	def draw(self):
		#left, bottom, image size_x, image size_y, pos_x, pos_y, draw size_x, draw size_y
		#tx, ty = self.target.pos
		tx, ty = self.target.draw_pos
		dty = ty - 490
		self.ib = 680 + int(dty//4)
		sx = self.il + self.cw * 3
		sy = self.ib + self.ch * 3
		px, py = 0, 0
		dx = 4 * sx
		dy = sy
		self.image.clip_draw_to_origin(self.il, self.ib, sx, sy, px, py, dx, dy)

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
		sx = self.il + self.cw * 3
		sy = self.ib + self.ch * 3
		px, py = 0, 0
		dx = 4 * sx
		dy = sy
		self.image.clip_draw_to_origin(self.il, self.ib, sx, sy, px, py, dx, dy)

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
		il = self.il
		if tx > 370:
			tx -= 290
		il = tx - self.spos
		self.il = il
		#print(self.il)
		
	def draw(self):
		#left, bottom, image size_x, image size_y, pos_x, pos_y, draw size_x, draw size_y
		ib = 0
		sx = self.il + self.cw * 3
		sy = ib + self.ch * 3
		px, py = 0, 0
		dx = sx * 3
		dy = sy
		self.image.clip_draw_to_origin(self.il, ib, sx, sy, px, py, dx, dy)