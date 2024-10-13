#Task-9.3
#Using a python Lambda function create a fibonacci series from 1 to 50 elements?

def fibonacci(count):
    fib_list = [0, 1]

    any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
             range(2, count)))

    return fib_list[:count]

print(fibonacci(50))
