from gemini import Scene, Entity, sleep, txtcolours as tc, Input, Vec2D
import math

colours = tc.ALL_COLOURS

scene = Scene((30,15), is_main_scene=True)

brick = Entity((14,7), (2,1))

i = 0
while True:
	sleep(.02)
	if Input().pressed_key == " ":
		break
	i += 0.05*math.pi
	# new_brick = Entity(brick.pos, (2,1), colour=colours[int(i%len(colours))])
	brick.pos = Vec2D(14,7) + Vec2D(round(10*math.cos(i)), round(5*math.sin(i)))
	scene.render()