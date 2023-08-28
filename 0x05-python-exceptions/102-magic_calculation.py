#!/usr/bin/python3
def magic_calculation(a, b):
    resultng = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                resultng += a ** b / i
        except Exception:
            resultng = b + a
            break
    return resultng
