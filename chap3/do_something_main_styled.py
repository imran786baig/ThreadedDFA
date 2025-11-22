#!/usr/bin/env python3
import math


def do_something(size, out_list):
    """Compute squares of square roots to simulate CPU-bound work."""
    for i in range(size):
        result = (math.sqrt(i)) ** 2
        out_list.append(result)


def main():
    results = []
    do_something(10000, results)
    print(f"Computed {len(results)} results.")


if __name__ == "__main__":
    main()
