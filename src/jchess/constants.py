from enum import Enum


class Color(Enum):
    WHITE = 1
    BLACK = 2


class Piece(Enum):
    EMPTY = 0
    WHITE_PAWN = 1
    WHITE_KNIGHT = 2
    WHITE_BISHOP = 3
    WHITE_ROOK = 4
    WHITE_QUEEN = 5
    WHITE_KING = 6
    BLACK_PAWN = 7
    BLACK_KNIGHT = 8
    BLACK_BISHOP = 9
    BLACK_ROOK = 10
    BLACK_QUEEN = 11
    BLACK_KING = 12


COLUMNS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
