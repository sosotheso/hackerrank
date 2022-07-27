import statistics as stat


def average(array):
    # your code goes here
    # convert list to set
    my_set = set(array)
    return stat.mean(my_set)

