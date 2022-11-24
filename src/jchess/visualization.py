from abc import ABC, abstractmethod

from typing import Optional

from jchess.data.data import DataInstance
import matplotlib.pyplot as plt
import numpy as np


class Visualization(ABC):
    def __init__(self, data_instance: DataInstance, name: Optional[str] = None):
        self.data_instance = data_instance
        self.name = name

    @abstractmethod
    def visualize(self, ax: plt.Axes, **kwargs):
        raise NotImplementedError

    def get_title(self):
        return self.name or self.Meta.name

    class Meta:
        name = "visualization"


class WinsByColorPie(Visualization):
    def visualize(self, ax: plt.Axes, **kwargs):
        black_win = 0
        white_win = 0
        tie = 0
        for game in self.data_instance.games:
            if game.game.result == '1-0':
                white_win += 1
            elif game.game.result == '0-1':
                black_win += 1
            elif game.game.result == '1/2-1/2':
                tie += 1
        ax.pie(np.array([white_win, tie, black_win]), labels=['White', 'Tie', 'Black'], colors=['white', 'grey', 'black'])

    class Meta:
        name = "Distribution of wins by color"


class TerminationMethodPie(Visualization):
    def visualize(self, ax: plt.Axes, **kwargs):
        termination_dict = dict()
        for game in self.data_instance.games:
            if "Termination" in game.annotations.keys():
                method = game.annotations["Termination"]
            else:
                method = "Unknown"
            termination_dict[method] = 1 if method not in termination_dict.keys() else termination_dict[method] + 1
        labels = []
        sizes = []
        for x, y in termination_dict.items():
            labels.append(x)
            sizes.append(y)

        # Plot
        ax.pie(sizes, labels=labels)

    class Meta:
        name = "How did your games end?"


class LengthOfGamesHistogram(Visualization):

    def visualize(self, ax: plt.Axes, **kwargs):
        lengths = []
        for game in self.data_instance.games:
            nmoves = len(game.game.turns) - 1
            lengths.append(nmoves)
        ax.hist(lengths)

    class Meta:
        name = "Length of games (Turns)"


class DurationOfMovesHistogram(Visualization):

    def visualize(self, ax: plt.Axes, **kwargs):
        pass

    class Meta:
        name = "Duration of moves"
