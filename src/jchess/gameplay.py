from src.jchess.constants import Color, Piece, COLUMNS


def _parse_move(move):
    piece = 1
    destination = ''
    return piece, destination


class Board:
    def __init__(self):
        self.grid = [[Piece.WHITE_ROOK, Piece.WHITE_PAWN, Piece.EMPTY, Piece.EMPTY, Piece.EMPTY, Piece.EMPTY, Piece.BLACK_PAWN, Piece.BLACK_ROOK],
                     [Piece.WHITE_KNIGHT, Piece.WHITE_PAWN, Piece.EMPTY, Piece.EMPTY, Piece.EMPTY, Piece.EMPTY, Piece.BLACK_PAWN, Piece.BLACK_KNIGHT],
                     [Piece.WHITE_BISHOP, Piece.WHITE_PAWN, Piece.EMPTY, Piece.EMPTY, Piece.EMPTY, Piece.EMPTY, Piece.BLACK_PAWN, Piece.BLACK_BISHOP],
                     [Piece.WHITE_QUEEN, Piece.WHITE_PAWN, Piece.EMPTY, Piece.EMPTY, Piece.EMPTY, Piece.EMPTY, Piece.BLACK_PAWN, Piece.BLACK_QUEEN],
                     [Piece.WHITE_KING, Piece.WHITE_PAWN, Piece.EMPTY, Piece.EMPTY, Piece.EMPTY, Piece.EMPTY, Piece.BLACK_PAWN, Piece.BLACK_KING],
                     [Piece.WHITE_BISHOP, Piece.WHITE_PAWN, Piece.EMPTY, Piece.EMPTY, Piece.EMPTY, Piece.EMPTY, Piece.BLACK_PAWN, Piece.BLACK_BISHOP],
                     [Piece.WHITE_KNIGHT, Piece.WHITE_PAWN, Piece.EMPTY, Piece.EMPTY, Piece.EMPTY, Piece.EMPTY, Piece.BLACK_PAWN, Piece.BLACK_KNIGHT],
                     [Piece.WHITE_ROOK, Piece.WHITE_PAWN, Piece.EMPTY, Piece.EMPTY, Piece.EMPTY, Piece.EMPTY, Piece.BLACK_PAWN, Piece.BLACK_ROOK]]
        self.turn = Color.WHITE

    def make_move(self, move):
        pass

    def notation_to_fromto(self, notation):
        pass

    def get_piece_at_position(self, position):
        assert len(position) == 2, "that's not a valid position"
        column, file = position[0], position[1]
        return self.grid[COLUMNS.index(column)][int(file)-1]


class IllegalMove(Exception):
    pass
