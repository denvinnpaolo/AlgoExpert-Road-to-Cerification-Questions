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


# Solution 2:
def MinimumWaitingTime(queries):
    queries.sort()
    a = [0] * len(queries)
    time = 0

    for i in range(len(queries) - 1):
        # since we know how much duration the next value is going to be
        # we set the array at next index by
        # adding the value of the query at the same index as the value in the a array
        a[i + 1] = queries[i] + a[i]
        #adding the duration as function move along the query 
        time += a[i+1]

    return time