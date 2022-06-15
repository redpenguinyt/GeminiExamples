from gemini import Scene, Sprite, txtcolours as tc, Input, Vec2D

# Player plays King
# against King and Queen
nl = '\n'
board = Scene((10,10), is_main_scene=True)
walls = Sprite((0,0), image=f"""█{'█'*8}█
{f'█{" "*8}█{nl}'*8}█{'█'*8}█""", layer=5)

player_king = Sprite((5,5), "K", collisions=[5])
player_king.range = 1

enemy_king = Sprite((4,6), "K", colour=tc.RED)
enemy_king.range = 2
enemy_queen = Sprite((6,3), "Q", colour=tc.RED)
enemy_queen.range = -1
enemies = [enemy_king, enemy_queen]

def is_hit(pos, checking_for_white):
	for piece in enemies if checking_for_white else [player_king]:
		print(f"checking for {piece}")
		for d in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
			print(f"Trying {d}")
			i = 0
			while i < piece.range or piece.range == -1:
				i += 1
				direction_change = [j*i for j in d]
				resulting_pos = piece.pos + direction_change
				print(direction_change)
				print(resulting_pos)
				if walls in board.get_entities_at(resulting_pos, [5]):
					print("hit a wall")
					break
				if pos == resulting_pos:
					return True

is_hit((3,3), True)

while True:
	board.render()
	user_direction = input("Which way to go (UDLR): ")
	direction = Vec2D(0,0)
	for k, d in zip("UDLR", Input.direction_keys.values()):
		print("aaaaa: ",k,d)
		if k in user_direction.upper():
			direction += d
	if is_hit(player_king.pos + direction, True):
		player_king.move(direction)