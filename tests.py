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

assert c['h8']['occupant'] == "black rook"