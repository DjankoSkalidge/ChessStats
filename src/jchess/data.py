from src.jchess.model import Entry, File
from src.jchess.constants import Color
from src.jchess.pgn.parser import chessmove
from parsita.state import ParseError
from typing import Optional, List, Dict
from src.jchess.pgn.parser import file
import json


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


class DataLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath
        if not filepath.endswith('.pgn') and not filepath.endswith('.json'):
            print(".pgn or .json file extension expected. Will try to parse this as a PGN.")

    def load(self):
        if self.filepath.endswith('.json'):
            print(f"Parsing json file {self.filepath}")
            with open(self.filepath, 'r') as f:
                obj = json.load(f)
                data = File(entries=obj["entries"])
        else:
            print(f"Parsing pgn file {self.filepath}")
            with open(self.filepath, 'r') as f:
                data = File(entries=file.parse(f.read()).or_die())
        return DataInstance(data.entries)
