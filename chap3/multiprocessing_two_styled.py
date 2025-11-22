#!/usr/bin/env python3
import multiprocessing
import time
from do_something import do_something


def main():
    size = 1000
    manager = multiprocessing.Manager()
    out_list1 = manager.list()
    out_list2 = manager.list()

    # Create processes
    p1 = multiprocessing.Process(
        name='Process 1',
        target=do_something,
        args=(size, out_list1)
    )
    p2 = multiprocessing.Process(
        target=do_something,
        args=(size, out_list2)
    )

    # Start timing
    start_time = time.time()

    # Start processes
    p1.start()
    p2.start()

    # Wait for processes to finish
    p1.join()
    p2.join()

    end_time = time.time()

    print(f'Process 1 output length: {len(out_list1)}')
    print(f'Process 2 output length: {len(out_list2)}')
    print(f'Total execution time: {end_time - start_time:.2f} seconds')


if __name__ == '__main__':
    main()
