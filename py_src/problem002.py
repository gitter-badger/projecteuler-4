# Project Euler Problem 2 Solution
#
# Problem statement:
# Each new term in the Fibonacci sequence is generated by adding
# the previous two terms. By starting with 1 and 2, the first 10
# terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.
#
# Solution description:
# --
#
# Author: Daniel Schuette, Tom Praschan
# Date: 2018/09/24
# License: MIT (see ../LICENSE.md)
import time


def slow_fibonacci(n):
    """
    This function calculates the fibonacci sequence up to the n'th
    member.
    """
    x = 0
    y = 1
    if n == 1:
        return 1
    for i in range(n):
        _tmp = x  # the current `x' is stored in a tmp variable
        x = y  # `x' becomes the previous `y'
        y = _tmp + x  # `y' becomes the sum of the previous `x' and `y'
    return y


def fast_fibonacci(target):
    """
    Return a list containing all Fibonacci numbers whose values do not exceed
    the target.
    """

    # Generate list with all Fibonacci numbers below target
    if target == 1:
        return 1
    fib = [1, 2]
    i = 2
    while True:
        next = fib[i-1] + fib[i-2]

        # Check if the next number would exceeds our target value
        if next > target:
            break

        # Append the sum of the previous two terms to our list
        fib.append(next)
        i += 1

    # Starting from 2, every 3rd Fibonacci number is even
    return sum(fib[1::3])


if __name__ == "__main__":
    # start timing
    start = time.time()

    # define looping variables
    i, s = 0, 0
    target = 4000000

    # loop until `fibonacci()' returns an integer > target
    while True:
        i += 1
        _tmp = slow_fibonacci(i)
        if _tmp > target:
            break
        if (_tmp % 2) == 0:
            s += _tmp

    # stop timing and print results
    end = time.time()
    print("result: {}".format(s))
    print("elapsed: {}s".format(end - start))

    # Fast solution begins here!
    start = time.time()
    fast_result = fast_fibonacci(target)
    end = time.time()

    print("fast result: {}".format(fast_result))
    print("elapsed: {}s".format(end - start))
