class hill_climbing:
    def __init__(self, func, iteration_times):
        self.func = func
        self.iteration_times = iteration_times
        pass

    def hill_climbing(self):
        func = self.func
        current = func.initial()
        score = func.evalution(current)
        count = 0
        while count <= self.iteration_times:
            neighbor = func.transition(current)
            neighbor_score = func.evalution(neighbor)
            if neighbor_score >= score:
                current = neighbor
                score = neighbor_score
            count += 1
        return (current, score)
