def process(**kwargs):
    def fibonacci(n):
        a = 0
        b = 1
        if n <= 0:
            print("Incorrect input")
            x = []
        elif n == 1:
            x = [b]
        else:
            x = [a, b]
            for i in range(2, n):
                c = a + b
                x += [c]
                a = b
                b = c
        return x
    fibo = fibonacci(1000)
    if "filters" in kwargs.keys():
        for f in kwargs["filters"]:
            fibo = list(filter(f, fibo))
        print(fibo)
    if "offset" in kwargs.keys():
        fibo = fibo[kwargs["offset"]:]
        print(fibo)
    if "limit" in kwargs.keys():
        fibo = fibo[:kwargs["limit"]]
        print(fibo)



def sum_digits(x):

    return sum(map(int, str(x)))
process(
    filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
    limit=2,
    offset=2
)


process()