from pico2d import *
import gfw
import json

def load():
	with open('tile.json') as f:
		objects = json.load(f)

	for d in objects:
		clazz = CLASSES[d["type"]]
		obj = clazz(d)
		gfw.world.add(obj.layer(), obj)

class Obj:
	def __init__(self, d):
		self.pos = d["x"], d["y"]
		self.size = d["width"], d["height"]
		self.name = d["name"]

	def layer(self):
		return gfw.layer.platform

	def update(self):
		pass

	def draw(self):
		pass

class Platform(Obj):
	pass

class Enemy(Obj):
	pass

CLASSES = {
	"Platform": Platform,
	"Enemy": Enemy
}