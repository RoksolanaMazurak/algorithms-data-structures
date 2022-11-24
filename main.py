from testing import testing

if __name__ == '__main__':
    print("Worst case:")
    testing("resources/worst_case.txt", "bbbbbbbbbbbbbbbbbbb")
    print()
    print("Best case:")
    testing("resources/best_case.txt", "bbbbbbbbbbbbbb")
    print()
    print("Average case:")
    testing("resources/average_case.txt", "abc")


