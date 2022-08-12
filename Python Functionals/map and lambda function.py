cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    fib = [0] * n
    if n == 0: return []
    if n == 1: return [0]
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i - 2] + fib[i - 1]
    return fib


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
