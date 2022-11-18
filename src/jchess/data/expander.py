from abc import ABC, abstractmethod

from typing import List

from src.jchess.model import Entry


class DataExpander(ABC):
    def __init__(self, games: List[Entry]):
        self.games = games

    @abstractmethod
    def expand(self, **kwargs):
        raise NotImplementedError
