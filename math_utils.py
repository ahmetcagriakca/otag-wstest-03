def modulo_sum(a, b, m): return (a+b)%m

if __name__ == "__main__":
    assert modulo_sum(3, 4, 5) == 2
    assert modulo_sum(0, 0, 1) == 0
    assert modulo_sum(10, 15, 7) == 4
