import chess
# import json

from chess_coverage.coverage import Coverage

board = chess.Board()
board.push_san("e4")
board.push_san("d5")

c = Coverage(board)
cover = c.cover()
# print(json.dumps(cover, indent=2, sort_keys=True))
# print(board)

e4 = cover['e4']
assert e4['color'] == True
assert e4['index'] == 28
assert e4['is_protected_by'] == []
assert e4['is_threatened_by'] == ["d5"]
assert e4['moves'] == ["d5", "e5"]
assert e4['occupant'] == "white pawn"
assert e4['position'] == "e4"
assert e4['protects'] == []
assert e4['symbol'] == "P"
assert e4['threatens'] == ["d5"]

d5 = cover['d5']
assert d5['color'] == False
assert d5['index'] == 35
assert d5['is_protected_by'] == ["d8"]
assert d5['is_threatened_by'] == ["e4"]
assert d5['moves'] == ["e4", "d4"]
assert d5['occupant'] == "black pawn"
assert d5['position'] == "d5"
assert d5['protects'] == []
assert d5['symbol'] == "p"
assert d5['threatens'] == ["e4"]

assert cover['e5']['white_can_move_here'] == ["e4"]
assert cover['e5']['black_can_move_here'] == ["e7"]

assert cover['h8']['protects'] == ["g8", "h7"]
assert cover['h7']['is_protected_by'] == ["h8"]
