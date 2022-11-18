from abc import ABC, abstractmethod

from typing import List

from src.jchess.model import Entry
import matplotlib.pyplot as plt
import numpy as np


class Visualization(ABC):
    def __init__(self, games: List[Entry]):
        self.games = games

    @abstractmethod
    def visualize(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_title(self):
        raise NotImplementedError


class WinsByColorPie(Visualization):
    def get_title(self):
        return "Distribution of wins by color"

    def visualize(self, ax: plt.Axes, **kwargs):
        black_win = 0
        white_win = 0
        tie = 0
        for game in self.games:
            if game.game.result == '1-0':
                white_win += 1
            elif game.game.result == '0-1':
                black_win += 1
            elif game.game.result == '1/2-1/2':
                tie += 1
        ax.pie(np.array([white_win, tie, black_win]), labels=['White', 'Tie', 'Black'])


class TerminationMethodPie(Visualization):
    def get_title(self):
        return "Distribution of termination methods"

    def visualize(self, ax: plt.Axes, **kwargs):
        termination_dict = dict()
        for game in self.games:
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
        plt.pie(sizes, labels=labels)
