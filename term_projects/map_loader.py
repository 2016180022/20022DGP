from pico2d import *
import gfw
import json

def load():
	with open('res/tile.json') as f:
		objects = json.load(f)

	for d in objects:
		clazz = CLASSES[d["type"]]
		obj = clazz(d)
		if "properties" in d:
			props = d["properties"]
			for prop in props:
				obj.__dict__[prop["name"]] = prop["value"]
		gfw.world.add(obj.layer(), obj)
		
class Obj:
	def __init__(self, d):
		self.pos = d["x"], d["y"]
		self.size = d["width"], d["height"]
		self.name = d["name"]
		if "properties" in d:
			for prop in d["properties"]:
				self.__dict__[prop["name"]] = prop["value"]

	def layer(self):
		return gfw.layer.platform

	def update(self):
		pass

	def draw(self):
		pass

class Platform(Obj):
	pass

CLASSES = {
	"Platform": Platform,
}