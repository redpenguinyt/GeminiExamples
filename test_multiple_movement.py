from gemini import Scene, Entity, sleep, Camera

scene = Scene((50,12), is_main_scene=True)
block0 = Entity((0,0), (4,2))
block1 = Entity((0,2), (4,2))
block2 = Entity((0,4), (4,2))
block3 = Entity((0,6), (4,2))
block4 = Entity((0,8), (4,2))
block5 = Entity((0,10),(4,2))
camera = Camera((0,0), (6,10), block2)

i = 0
while True:
	i += 1
	camera.render(show_coord_numbers=True)
	sleep(.1)
	block0.move(1,0)
	if i % 2 == 0:
		block1.move(1,0)
	if i % 4 == 0:
		block2.move(1,0)
	if i % 8 == 0:
		block3.move(1,0)
	if i % 16 == 0:
		block4.move(1,0)
	if i % 32 == 0:
		block5.move(1,0)

		looped = all(child.pos[0] == 0 for child in scene.children)
		if looped:
			scene.render()
			sleep(5)