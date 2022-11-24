import time

from boyer_moore import boyer_moore_search


def testing(file_name: str, pattern: str):
    with open(file_name) as file:
        text = file.read()

    start = time.time()

    print(boyer_moore_search(text, pattern))

    print(f"Time taken:  {(time.time()-start)}")



