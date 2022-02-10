from test_framework import generic_test


def reverse(x: int) -> int:
    """
    brute-force

    O(N) / O(1)
    """
    neg = False
    if x < 0:
        neg, x = True, -x
    res = 0
    while x:
        res, x = 10*res+x%10, x//10
    return res if not neg else -res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
