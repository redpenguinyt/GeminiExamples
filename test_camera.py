from gemini import Scene, Entity, Sprite, Camera, sleep, txtcolours as tc

scene = Scene((20,10), is_main_scene=True)

sash = '\n'.join([' '*i*4+"█"*5 for i in range(10)])
for i in range(2):
	sash_sprite1 = Sprite((i*2,i*3),sash, layer=10, colour=tc.COLOURS[i])

block = Entity((2,2),(5,5))
camera = Camera((0,0),(9,9), focus_object=block)

def multirender():
	bake1 = scene.render(is_display=False)
	bake2 = camera.render(is_display=False)

	print(scene.get_separator() + scene._render_stage(bake1))
	print(scene._render_stage(bake2, ))

block.move_functions = [multirender]

while True:
	for direction in [(1,0),(0,1),(-1,0),(0,-1)]:
		block.move(direction)
		sleep(0.2)
