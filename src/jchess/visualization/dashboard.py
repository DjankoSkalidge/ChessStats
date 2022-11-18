import matplotlib.pyplot as plt
from src.jchess.visualization.visualization import Visualization


class Dashboard:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.school = []

    def add_visualization(self, vis: Visualization):
        if len(self.school) == self.x*self.y:
            print("No more visualizations can be added to current dashboard")
        else:
            self.school.append(vis)

    def export(self, output: str):
        fig, axs = plt.subplots(self.x, self.y)
        ax_number = 0
        for vis in self.school:
            vis.visualize(axs[ax_number])
            axs[ax_number].set_title(vis.get_title())
            ax_number += 1
        # plt.show()
        plt.savefig(output)


