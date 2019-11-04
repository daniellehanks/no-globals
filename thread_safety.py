from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor

from database import Database


def threads():
    print("threads")
    d = Database()
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(d.insert, ['a', 'b', 'c', 'd', 'e'])

    print(d._db)


def processes():
    # This results in an empty list and id still at 0 because
    # ProcessPoolExecutor pickles the function and arguments and sends them
    # to separate interpreter processes, leaving the original object
    # unaffected.
    print("processes")
    d = Database()
    with ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(d.insert, ['a', 'b', 'c', 'd', 'e'])

    print(d._db)
