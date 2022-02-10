from test_framework import generic_test


def reverse_bits(x: int) -> int:
    """
    reverse한 값을 미리 계산해 계산량을 줄일 수 있다.

    O(64/n) / O(2^n)
    """
    d = {0:0,1:8,2:4,3:12,4:2,5:10,6:6,7:14,8:1,9:9,10:5,11:13,12:3,13:11,14:7,15:15}
    m, n = 1, 4
    mask = 0xF
    res = 0
    while x:
        res |= d[x & mask] << (64-n*m)
        x, m = x>>n, m+1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
