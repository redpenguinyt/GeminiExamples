from gemini import Scene, Entity, sleep, txtcolours as tc
import random

scene1 = Scene((20,20), is_main_scene=True)

floor = Entity((3,10), (14,1))

direction_range = [3,2,1,-1,-2,-3]

for _ in range(10):
	new_block = Entity((random.randint(4,15),0),(2,1), auto_render=True, collisions=True, colour=random.choice(tc.COLOURS))
	direction = random.choice(direction_range)
	while True:
		is_collided = new_block.move(0,direction)
		if is_collided == 1:
			break
		sleep(.1)

scene2 = Scene((20,20), is_main_scene=True)

floor = Entity((10,3), (1,14))

for _ in range(10):
	new_block = Entity((0,random.randint(4,14)),(2,1), auto_render=True, collisions=True, colour=random.choice(tc.COLOURS))
	direction = random.choice(direction_range)
	while True:
		is_collided = new_block.move(direction,0)
		if is_collided == 1:
			break
		sleep(.1)
