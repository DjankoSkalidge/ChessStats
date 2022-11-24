class OpeningNode:
    def __init__(self, moveorder: list, name=None):
        self.name = name
        self.continuations = dict()
        self.moveorder = moveorder

    def has_continuation(self, move):
        return move in self.continuations.keys()

    def get_or_add_continuation(self, move):
        if move not in self.continuations.keys():
            self.continuations[move] = OpeningNode(self.moveorder + [move])
        return self.continuations[move]
