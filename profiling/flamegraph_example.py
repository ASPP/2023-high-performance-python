def function_a():
    r = 0
    for i in range(30_000_000):
        r += i
    function_b()


def function_b():
    r = 0
    for i in range(60_000_000):
        r += i


def function_c():
    r = 0
    for i in range(10_000_000):
        r += i


if __name__ == "__main__":
    function_a()
    function_c()
