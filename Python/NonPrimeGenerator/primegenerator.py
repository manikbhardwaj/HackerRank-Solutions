def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def manipulate_generator(generator, n):
    # Enter your code here
    if is_prime(n + 1):
        next(generator)
        manipulate_generator(generator, n + 1)
    pass


def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1


k = int(raw_input())
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print
    n
    manipulate_generator(g, n)
