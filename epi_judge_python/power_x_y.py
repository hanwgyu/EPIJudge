from test_framework import generic_test


def power(x: float, y: int) -> float:
        """
        2진수로 표현해 계산 횟수를 줄임

        O(logN) / O(1)
        """
        if y < 0:
            x, y = 1.0/x, -y
        res = 1
        while y:
            if y & 1:
                res *= x
            x, y = x*x, y >> 1
        return res


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
