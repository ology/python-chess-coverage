import chess
import json
import sys

sys.path.append('./src')

from chess_coverage.chess_coverage import Coverage

board = chess.Board(fen="8/1p6/8/8/8/8/1P6/8")
c = Coverage(board)
cover = c.cover()
# print(json.dumps(cover, indent=2, sort_keys=True))
# print(board)

b2 = cover['b2']
assert b2['color'] == True
assert b2['moves'] == ["b3", "b4"]
assert b2['occupant'] == "white pawn"
assert b2['position'] == "b2"
assert b2['symbol'] == "P"
a3 = cover['a3']
assert a3['white_can_capture_here'] == ["b2"]
c3 = cover['c3']
assert c3['white_can_capture_here'] == ["b2"]
b7 = cover['b7']
assert b7['color'] == False
assert b7['moves'] == ["b6", "b5"]
assert b7['occupant'] == "black pawn"
assert b7['position'] == "b7"
assert b7['symbol'] == "p"
a6 = cover['a6']
assert a6['black_can_capture_here'] == ["b7"]
c6 = cover['c6']
assert c6['black_can_capture_here'] == ["b7"]

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

# make sure cells with no occupant have an index & position
assert cover['b4']['index'] == 25
assert cover['b4']['position'] == 'b4'

board = chess.Board()
board.push_san("e4")
# print(board.has_legal_en_passant())
board.push_san("a6")
# print(board.has_legal_en_passant())
board.push_san("e5")
# print(board.has_legal_en_passant())
board.push_san("d5")
assert board.has_legal_en_passant() == True

c = Coverage(board)
cover = c.cover()
# print(json.dumps(cover, indent=2, sort_keys=True))
# print(board)
assert cover['e6']['white_can_move_here'] == ["e5"]

# test check
fen = 'rnbqkbnr/ppp1pppp/3p4/8/Q7/8/PPPPPPPP/RNB1KBNR b - - 0 1'
board = chess.Board(fen=fen)
c = Coverage(board)
cover = c.cover()
# print(json.dumps(cover, indent=2, sort_keys=True))
# print(board)
assert cover['a1']['protects'] == ["a2", "b1"]
assert cover['b1']['is_protected_by'] == ["a1"]
assert cover['h7']['moves'] == ["h6", "h5"]
