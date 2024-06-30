from lib import hill_climbing
from lib import one_max

func = one_max.one_max(lenth= 100)
HC = hill_climbing.hill_climbing(func,100)
solution , score =HC.hill_climbing()
print(solution,score)