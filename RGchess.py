from gemini import Scene, Sprite, txtcolours as tc, Input, Vec2D

DIRECTIONS = [Vec2D(-1,-1),Vec2D(0,-1),Vec2D(-1,0),Vec2D(1,0),Vec2D(0,1),Vec2D(1,1),Vec2D(1,-1),Vec2D(-1,1)]

dots: list[Sprite] = []
def clear_dots():
	global dots
	for d in dots:
		d.parent = None
	dots = []

# Player plays King and Queen
# against King
nl = '\n'
board = Scene((10,10), is_main_scene=True)
board.use_separator = False
walls = Sprite((0,0), image=f"""█{'█'*8}█
{f'█{" "*8}█{nl}'*8}█{'█'*8}█""", layer=5)

player_king = Sprite((5,5), "K", colour=tc.GREEN, collisions=[5])
player_king.type = "king"
player_queen = Sprite((6,3), "Q", colour=tc.GREEN, collisions=[5])
player_queen.type = "queen"
whites = [player_king, player_queen]

enemy_king = Sprite((4,3), "K", colour=tc.PURPLE, collisions=[5])
enemy_king.type = "king"
blacks = [enemy_king]

def get_directions(piece):
	global dots
	results = []
	for d in DIRECTIONS:
		for i in range(1,9 if piece.type == "queen" else 2):
			if board.is_entity_at(piece.pos + d * i, [5]):
				break
			results.append(piece.pos + d * i)

	return results

def possible_postions(moving_piece, enemies):
	global dots
	for piece in enemies:
		for pos in get_directions(piece):
			dots.append(Sprite(pos, ".", colour=tc.RED, layer=5))

	results = get_directions(moving_piece)
	clear_dots()
	return list(results)

while True:
	board.render(show_coord_numbers=True)
	user_piece = [player_king,player_queen][int(input("0: king, 1: queen "))]
	user_chosen_pos = None
	options = possible_postions(user_piece, blacks)
	print(options)
	while user_chosen_pos not in options:
		user_chosen_pos = Vec2D(input("Which coords do you wish to go to? (1-8,1-8)").split(","))
	user_piece.pos = user_chosen_pos
