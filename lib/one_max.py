import numpy as np


class one_max:
    def __init__(self, lenth) -> None:
        self.lenth = lenth
        pass

    def initial(self):
        return np.random.randint(2,size=self.lenth)

    def evalution(self, arr):
        return sum(arr)

    def transition(self, arr):
        neighbor = np.copy(arr)
        index = np.random.randint(len(neighbor))
        neighbor[index] ^= 1
        return neighbor
