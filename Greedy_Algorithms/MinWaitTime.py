# Minimum Wait Time
# Easy
# Greedy Algorithm

# Solution 1:

def MinumumWaitingTime(queries):
    # sorts the query for optimal order for min waiting time
    q = queries.sorted()
    # min wait time variable
    time = 0

    # take the index and val of sorted query
    for i, val in enumerate(q):
        queriesLeft = len(q) - (i - 1)
        time += val * queriesLeft


    return time