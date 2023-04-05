def solution(array_a, array_b):
    squares = [(array_a[i] - array_b[i]) ** 2 for i in range(len(array_a))]
    return sum(squares) / len(squares)