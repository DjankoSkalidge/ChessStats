import matplotlib.pyplot as plt
from jchess.visualization import Visualization


class Dashboard:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.school = []

    def add_visualization(self, vis: Visualization):
        if len(self.school) == self.x * self.y:
            print("No more visualizations can be added to current dashboard")
        else:
            self.school.append(vis)

    def export(self, output: str):
        fig, axes = plt.subplots(self.x, self.y)
        for i, ax in enumerate(axes.flat):
            if i < len(self.school):
                self.school[i].visualize(ax)
                ax.set_title(self.school[i].get_title())
            else:
                img = plt.imread("data/pawn.png")
                ax.imshow(img)
                ax.set_title("jChess")
        # plt.show()
        plt.savefig(output)
