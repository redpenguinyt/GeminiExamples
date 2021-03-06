from gemini import Scene, Entity, Sprite, AnimatedSprite, Input, txtcolours as tc, Vec2D, Camera

age = "49"

player = AnimatedSprite((1,1),['▇','▆','▇','█'], colour=tc.RED, layer=-20, collisions=[0,-5])
player.input = Input() # attach an input class to the player

def new_camera(scene):
	camera = Camera((0,0), (10,5), focus_object=player, scene=scene)
	player.move_functions = [camera.render]
	return camera

def move_player():
	event = player.input.get_key_press()
	if event not in ["w", "a", "s", "d"]:
		return event
	collided = player.move(player.input.direction_keys[event])
	if collided == 0:
		player.next_frame()

# -- Scene 0 -- #
scene0_image = """
██████████████████
█ █              █
█   █ █ ███ ████ █
███   █ █   █  █ █
█   ███   █   █  █
█ ███   █ █ ████ █
█     ███ █      █
█████ █   ███ ████
█                █
█                █
█     Привет
█                █
█                █
██████████████████"""
def scene0():
	scene0 = Scene((18, 14),clear_char=" ",children=[Sprite((0,0),scene0_image)])
	scene0.add_to_scene(player)
	new_camera(scene0)

	scene0.render()
	while True:
		move_player()
		if player.pos == (17,10): break

# -- Scene 1 -- #
scene1_image = """
██████████████████
█                █
█  Сегодня твой  █

█  день рождения █
█                █
██████████████████"""
def scene1():
	scene1 = Scene((18,7),clear_char=" ", children=[Sprite((0,0),scene1_image)])
	scene1.add_to_scene(player)
	new_camera(scene1)
	player.pos = (0,3)

	while True:
		move_player()
		if player.pos == (17,3): break

# -- Scene 2 -- #
scene2_image = """
██████████████████
█                █
      так что
█                █
██████████████████"""
def scene2():
	scene2 = Scene((18,5),clear_char=" ", children=[Sprite((0,0),scene2_image)])
	scene2.add_to_scene(player)
	new_camera(scene2)
	player.pos = (0,2)

	while True:
		move_player()
		if player.pos == (17,2): break

# -- Scene 3 -- #
scene3_image = """
██████████████████

██████████████████"""
def scene3():
	scene3 = Scene((40,4),clear_char=" ", children=[
		Sprite((0,1),scene3_image)
	])
	scene3.add_to_scene(player)
	camera = new_camera(scene3)
	player.pos = (0,2)

	while True:
		move_player()
		if player.pos == (6,2): break

	texts: list[Sprite] = []
	i = -1
	while True:
		if player.input.get_key_press() == "d":
			i += 1
			player.next_frame()
			camera.render()

			for text in texts:
				if text.pos == (0,0):
					if len(text.image) == 0:
						texts.remove(text)
						text.parent = None
					text.image = text.image[1:]
				else:
					text.move((-1,0), collide=False)
			if i == 0:
				texts.append(Sprite((17,0), "Ты почти дошел", parent=scene3))
			elif i == 100:
				texts.append(Sprite((17,0), "У меня хорошо, я текст,", parent=scene3))
			elif i == 124:
				texts.append(Sprite((17,0), "и могу сидеть здесь", parent=scene3))
			elif i == 144:
				texts.append(Sprite((17,0), "сколько хочу", parent=scene3))
			elif i == 200:
				texts.append(Sprite((17,0), "Ладно, иди дальше", parent=scene3))
			elif i == 220:
				break
			elif i == 25:
				texts.append(Sprite((17,0), "еще чуть чуть", parent=scene3))
			elif i == 50:
				texts.append(Sprite((17,0), "Совсем немного", parent=scene3))
			elif i == 75:
				texts.append(Sprite((17,0), "Как дела?", parent=scene3))
	while True:
		move_player()
		if player.pos == (17,2): break

# -- Scene 4 -- #
scene4_image = """
██████████████████████████████
█                            █
      с днем рождения!       █
█                            █
█                            █
█                            █
█                            █
█                            █
█                            █
█                            █
█                            █
█                            █
██████████████████████████████"""
cake = """
     {age[0]} {age[1]}
     | |
/----------\
|----------|
|vegan cake|
|__________|
\__________/""".format(age=age)
def scene4():
	scene4 = Scene((30,13), clear_char=" ", children=[
		Sprite((0,0), scene4_image), Sprite((9,3), cake, layer=1)
	])
	scene4.add_to_scene(player)
	new_camera(scene4)
	player.pos = (0,2)

	while move_player() != " ":
		if scene4.get_entities_at(player.pos, layers=[1]):
			scene4.add_to_scene(Entity(player.pos, (1,1), fill_char=" ", layer=-1))

scene0()
scene1()
scene2()
scene3()
scene4()

print("\n\nС днем рождения папа :D\n\n")