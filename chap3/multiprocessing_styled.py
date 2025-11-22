#!/usr/bin/env python3
import multiprocessing
import time
from do_something import do_something


def run_task():
    """Run a CPU-bound task in a separate process."""
    print('Process started...')
    manager = multiprocessing.Manager()
    out_list = manager.list()
    do_something(10, out_list)
    print(f'Process finished with {len(out_list)} results.')


def main():
    process = multiprocessing.Process(target=run_task)

    print('Before start:', process, process.is_alive())
    process.start()
    print('Running:', process, process.is_alive())

    time.sleep(2)  # simulate some delay before termination

    process.terminate()
    print('Terminated:', process, process.is_alive())

    process.join()
    print('Joined:', process, process.is_alive())
    print('Exit code:', process.exitcode)


if __name__ == '__main__':
    main()
