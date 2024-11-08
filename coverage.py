import chess

board = chess.Board()
board.push_san("e4")
board.push_san("d5")

# print(board.parse_san('Nf3'))

for m in board.legal_moves:
    print(m)

# print(chess.PAWN)
# print(chess.piece_symbol(chess.PAWN))
# print(chess.piece_name(chess.PAWN))

pieces = {
    "p": 1,
    "n": 2,
    "b": 3,
    "r": 4,
    "q": 5,
    "k": 6,
}
# for square in chess.SQUARES:
#     color = board.color_at(square)
#     piece = board.piece_at(square)
#     name = '-'
#     if piece:
#         lower = str(piece).lower()
#         index = pieces[lower]
#         name = chess.piece_name(index)
#     print(f"S: {square}, C: {color}, P: {piece}, N: {name}")

# attackers = board.attackers(chess.WHITE, chess.D5)
# print(attackers)

# coverage = {}

# for square in chess.SQUARES:
#     print(square)

# can = chess.Move.from_uci("a2a5") in board.legal_moves
# print(can)
