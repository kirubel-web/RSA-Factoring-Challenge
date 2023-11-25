#!/usr/bin/env python3

import sys

def factorize(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return i, num // i
    return num, 1

def main():
    if len(sys.argv) != 2:
        print("Usage: ./factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        numbers = file.read().splitlines()

    for num in numbers:
        num = int(num)
        p, q = factorize(num)
        print(f"{num}={p}*{q}")

if __name__ == "__main__":
    main()
