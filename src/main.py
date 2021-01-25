import time
from my_poetry_sample.greeting import Greeting
from my_poetry_sample import fib
from fib_c import fibonacci

def main():
    print("start")
    g = Greeting()
    g.japanese()
    g.english()

    start_time = time.time()
    fib_fib = [fib.fib(i) for i in range(40)]
    print(fib_fib)
    elapsed_time = time.time() - start_time
    print(elapsed_time)

    start_time = time.time()
    fib_fib = [fibonacci.fibonacci(i) for i in range(40)]
    print(fib_fib)
    elapsed_time = time.time() - start_time
    print(elapsed_time)

main()