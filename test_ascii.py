from gemini import Scene, Sprite, AnimatedSprite, sleep, txtcolours as tc

scene1 = Scene((30,10))
bob = AnimatedSprite((10,3),["¯\_(ツ)_/¯","_/¯(ツ)¯\_"], parent=scene1, colour=tc.BOLD, extra_characters=[1])

test_image = """
  ______
 /|_||_\`.__
(¶¶¶_¶¶¶¶_¶_\\
=`-(_)--(_)-'
"""

scene2 = Scene((32,10), bg_colour=tc.CYAN)
scene2.use_seperator = False
car = Sprite((5,5), test_image, parent=scene2, colour=tc.GREEN)

while True:
	for direction in [(0,1),(-1,-1),(0,1),(1,-1)]:
		for _ in range(4):
			bob.move(direction[0],direction[1])
			car.move(1,0)
			r1 = scene1.render(is_display=False)
			r2 = scene2.render(is_display=False)

			# Scene.render can be a complex process, so when it comes to rendering multiple scenes at once, you should 'bake' them as shown above then render them with Scene._render_stage.
			print(scene1.get_separator(True, len(r1)+len(r2)))
			print(scene1._render_stage(r1,show_coord_numbers=True))
			print(scene2._render_stage(r2, show_coord_numbers=True))

			sleep(.1)
		bob.next_frame()