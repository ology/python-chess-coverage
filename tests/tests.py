import chess
import json

from coverage import Coverage

board = chess.Board()
board.push_san("e4")
board.push_san("d5")
c = Coverage(board)
cover = c.cover()
# print(json.dumps(cover, indent=2, sort_keys=True))
# print(board)

assert cover['e4']['color'] == True
assert cover['e4']['index'] == 28
assert cover['e4']['is_protected_by'] == []
assert cover['e4']['is_threatened_by'] == ["d5"]
assert cover['e4']['moves'] == ["d5", "e5"]
assert cover['e4']['occupant'] == "white pawn"
assert cover['e4']['position'] == "e4"
assert cover['e4']['protects'] == []
assert cover['e4']['symbol'] == "p"
assert cover['e4']['threatens'] == ["d5"]
assert cover['e5']['white_can_move_here'] == ["e4"]
assert cover['e5']['black_can_move_here'] == ["e7"]
assert cover['d5']['is_threatened_by'] == ["e4"]
assert cover['h8']['protects'] == ["g8", "h7"]
assert cover['h7']['is_protected_by'] == ["h8"]
