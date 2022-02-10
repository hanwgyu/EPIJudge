from test_framework import generic_test


def parity(x: int) -> int:
    """
        XOR 연산을 하면 0^1 일때만 1이 나온다. 
        따라서 64bit를 반씩 접어서 XOR 연산을 해나아가면 마지막에 값이 1이면 전체 1이 홀수개 있는 것.

        O(logN) / O(1)
    """
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


def parity_2(x: int) -> int:
    """
        x&(x-1) 연산을 통해 가장 마지막 1을 없앨 수 있음 
        ex) x=(00101100), x&(x-1) = (00101000)

        O(K) / O(1) (K는 1의 갯수)
    """
    res = 0
    while x:
        res ^= 1
        x = x&(x-1)
    return res

def parity_1(x: int) -> int:
    """
    brute-force
    
    O(N) / O(1)
    """
    res = 0
    while x:
        res ^= x & 1
        x >>= 1
    return res


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
