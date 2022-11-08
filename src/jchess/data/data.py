from src.jchess.model import Entry
from src.jchess.enums import Color
from src.jchess.pgn.parser import chessmove
from parsita.state import ParseError
from typing import Optional


class DataInstance:
    def __init__(self, games: list[Entry]):
        self.games = games

    def select_by_annotations(self, matchers: dict[str, Optional[str]]) -> list[Entry]:
        """
        Selects games by annotation value
        Args:
            matchers: dictionary of matchers

        Returns:
        List of games containing a matching annotation
        """
        pass

    def select_by_username(self, username: str, color: Optional[Color]) -> list[Entry]:
        """
        Selects games by username
        Args:
            username: the username to match
            color: null for both
        Returns:
        list of games for the provided user in the provided color
        """
        # Actually, I'm rethinking this because it will depend on if the annotations are in a specific format.
        # The user will know what her data looks like, so she can use the select_by_annotations method for this.
        pass

    def select_by_opening(self, opening: str) -> list[Entry]:
        """

        Args:
            opening: name of the opening.

        Returns:

        """
        pass

    def select_by_first_move(self, move: str) -> list[Entry]:
        """

        Args:
            move: move notation

        Returns:
        list of games that start with the provided move
        """
        try:
            move = chessmove.parse(move).or_die()
        except ParseError as e:
            print("That's not a valid move")
            return []
        return [x for x in self.games if x.game.turns[0].whitemove.notation == move]
