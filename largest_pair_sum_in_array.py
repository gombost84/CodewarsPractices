def largest_pair_sum(numbers):
    x = sorted(numbers)
    return x[-1] + x[-2]
