import pytest
from src.jchess.gameplay import *
from src.jchess.constants import Piece, Color


def test_board_creation():
    board = Board()
    assert len(board.grid) == 8
    assert len(board.grid[0]) == 8


@pytest.mark.parametrize("position,piece", [('e8', Piece.BLACK_KING),
                                            ('a1', Piece.WHITE_ROOK),
                                            ('a2', Piece.WHITE_PAWN),
                                            ('g1', Piece.WHITE_KNIGHT),
                                            ('f8', Piece.BLACK_BISHOP),
                                            ('h2', Piece.WHITE_PAWN),  # Harry
                                            ('e4', Piece.EMPTY)
                                            ])
def test_initial_position(position, piece):
    board = Board()
    assert board.get_piece_at_position(position) == piece


def test_making_moves():
    board = Board()
    board.make_move("Nf3")
    piece_at_f3 = board.get_piece_at_position("f3")
    assert piece_at_f3 == Piece.WHITE_KNIGHT
    assert board.turn == Color.BLACK


@pytest.mark.parametrize("notation,fromto", [("Nf3", "g1f3"), ("e4", "e2e4"), ("h3", "h2h3")])
def test_notation_to_fromto(notation, fromto):
    board = Board()
    assert board.notation_to_fromto(notation) == fromto


def test_notation_to_fromto_difficult():
    board = Board()
    board.make_move("e3")
    fromto = board.notation_to_fromto("e4")
    assert fromto == "e3e4"


def test_illegal_move():
    board = Board()
    with pytest.raises(IllegalMove):
        board.make_move('0-0')
