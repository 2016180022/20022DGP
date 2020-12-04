import json

with open('map.json') as f:
	data = json.load(f)

layer = data["layers"][1]
objs = layer["objects"]

for o in objs:
	#o["y"] = 1000 - o["y"] - 460
	o["x"] = 4* o["x"]
	o["y"] = 4* (540 - o["y"]) - 495

with open('tile.json', 'w') as f:
	json.dump(objs, f, indent = 2)