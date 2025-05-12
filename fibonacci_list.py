# fibonacci_list.py

def print_fibonacci_list(n):
    """
    Print the first `n` numbers in the Fibonacci sequence as a list.
    """
    if n <= 0:
        print([])
        return

    fib_list = [0] if n == 1 else [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    
    print(fib_list)


# Example usage
if __name__ == "__main__":
    print_fibonacci_list(10)