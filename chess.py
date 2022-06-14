from gemini import Scene, Sprite, txtcolours as tc, Vec2D

# (1,-2) is bottom left
# (-2,-2) is bottom right)

BOARD_HEIGHT = 8
BOARD_WIDTH = 8
nl = '\n'

board = Scene((BOARD_WIDTH+2,BOARD_HEIGHT+2), is_main_scene=True)
walls = Sprite((0,0), image=f"""█{'█'*BOARD_WIDTH}█
{f'█{" "*BOARD_WIDTH}█{nl}'*BOARD_HEIGHT}█{'█'*BOARD_WIDTH}█""", layer=5)

class ChessPiece(Sprite):
	def __init__(self, pos: tuple, image: str, label: str, can_go: dict, is_white: bool):
		colour = tc.RED if is_white else tc.BLUE
		self.move_rules = can_go
		self.is_white = is_white
		self.label = label

		super().__init__(pos,image, colour=colour, layer=0,collisions=[-1])
	def __str__(self):
		return f"{self.label} at {self.pos}"

	def _move(self, pos: tuple, normalised: tuple, simplified: tuple):
		return 1 # This is for the chess piece to decide

	def move(self, pos: Vec2D):
		normalised = tuple(i-abs(i) for i in pos)
		simplified = tuple(abs(i)-min(map(int.__abs__, pos)) for i in pos)
		print(normalised)
		print(simplified)

		if normalised in self.move_rules.keys():
			return self._move(pos, normalised, simplified)
		else:
			return 1

class Rook(ChessPiece):
	def __init__(self, pos: tuple, is_white: bool):
		move_rules = {(1,0):-1,(-1,0):-1,(1,0):-1,(1,0):-1}
		super().__init__(pos, 'R', "Rook", move_rules, is_white)

	def _move(self, pos: tuple, normalised: tuple, simplified: tuple):
		if pos.count(0) < 1:
			return 1

		if pos[0] > 0:
			for x in range(1,pos[0]):
				if self.parent.is_entity_at(self.pos + (x,0)):
					return 1
		elif pos[1] <= 0: return 1

rook = Rook((1,-2), True)
print(rook.move_rules)
rook.move((7,-2))

is_white_turn = False
while True:
	is_white_turn = not is_white_turn
	for c in board.children:
		print(c.layer, type(c.layer))
	board.render()
	print("White turn" if is_white_turn else "Black turn")

	pieces: list[ChessPiece] = []

	while not pieces:
		get_piece: tuple = eval(input("Give the position of the chess piece you want to control (1-8): e.g. 3,8 or 4,2 "))
		pieces = board.get_entities_at(get_piece, 0)
	piece = pieces[0]

	new_pos = (0,0)

	while piece.move(piece.pos + new_pos) == 1:
		new_pos = tuple = eval(input(f"Where do you want the {piece.label} to go (1-8): e.g. 3,8 or 4,2 "))