from abc import ABC, abstractmethod
import pickle

from src.jchess.model import Entry
from src.jchess.data.data import DataInstance
from src.jchess.opening_detector import OpeningNode


class DataExpander(ABC):
    def __init__(self):
        pass

    def expand(self, data_instance: DataInstance, **kwargs) -> None:
        for entry in data_instance.games:
            self.classify(entry)

    @abstractmethod
    def classify(self, entry: Entry) -> Entry:
        raise NotImplementedError


class LastPositionEval(DataExpander):
    """
    Uses an engine to evaluate the final position on the board.
    Useful for games that ended by time forfeit.
    """

    def __init__(self, path_to_engine: str):
        super().__init__()
        self.path_to_engine = path_to_engine

    def classify(self, entry: Entry) -> Entry:
        pass


class EngineEvaluationExpander(DataExpander):
    """
    Uses an engine to evaluate entire games.
    """

    def __init__(self, path_to_engine: str):
        super().__init__()
        self.path_to_engine = path_to_engine

    def classify(self, entry: Entry) -> Entry:
        pass


class OpeningDetectorExpander(DataExpander):
    """
    Uses an opening structure to detect openings of games.
    Adds the name of the opening as an annotation.
    """

    def __init__(self, path_to_opening_graph: str):
        super().__init__()
        with open(path_to_opening_graph, 'rb') as f:
            self.tree_like_dictionary_graph: OpeningNode = pickle.load(f)

    def classify(self, entry: Entry) -> Entry:
        current_node = self.tree_like_dictionary_graph
        for turn in entry.game.turns:
            if current_node.has_continuation(turn.whitemove.notation):
                current_node = current_node.continuations[turn.whitemove.notation]
            else:
                break
            if current_node.has_continuation(turn.blackmove.notation):
                current_node = current_node.continuations[turn.blackmove.notation]
            else:
                break
        entry.annotations["Detected Opening"] = current_node.name
        return entry


