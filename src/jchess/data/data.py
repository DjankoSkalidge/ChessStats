from src.jchess.model import Entry, File
from src.jchess.enums import Color
from src.jchess.pgn.parser import chessmove
from parsita.state import ParseError
from typing import Optional, List, Dict


class DataInstance:
    def __init__(self, games: List[Entry]):
        self.games = games

    def select_by_annotations(self, matchers: Dict[str, Optional[str]]):
        """
        Selects games by annotation value
        Args:
            matchers: dictionary of matchers

        Returns:
            DataInstance with games containing matching annotations
        """
        return DataInstance([x for x in self.games if matchers.items() <= x.annotations.items()])

    def select_by_username(self, username: str, color: Optional[Color] = None):
        """
        Selects games by username
        Args:
            username: the username to match
            color: null for both
        Returns:
            DataInstance with games for the provided user in the provided color
        """
        # Actually, I'm rethinking this because it will depend on if the annotations are in a specific format.
        # The user will know what her data looks like, so she can use the select_by_annotations method for this.
        if color == Color.BLACK:
            return DataInstance([x for x in self.games if x.annotations["Black"] == username])
        elif color == Color.WHITE:
            return DataInstance([x for x in self.games if x.annotations["White"] == username])
        return DataInstance([x for x in self.games if x.annotations["White"] == username
                             or x.annotations["Black"] == username])

    def select_by_opening(self, opening: str):
        """

        Args:
            opening: name of the opening.

        Returns:

        """
        pass

    def select_by_first_move(self, move: str):
        """

        Args:
            move: move notation

        Returns:
            DataInstance with games that start with the provided move
        """
        try:
            move = chessmove.parse(move).or_die()
        except ParseError:
            print("That's not a valid move")
            return DataInstance([])
        return DataInstance([x for x in self.games if x.game.turns[0].whitemove.notation == move])

    def save(self, name: str):
        with open(name, 'w+') as f:
            f.write(File(entries=self.games).json())
