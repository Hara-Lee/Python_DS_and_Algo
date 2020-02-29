import math

# iter() 함수의 시간복잡도는 O(n)
def find_fibonacchi_seq_iter(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# rec() 함수의 시간복잡도는 O(n^2)
def find_fibonacchi_seq_rec(n):
    if n < 2:
        return n
    return find_fibonacchi_seq_rec(n - 1) + find_fibonacchi_seq_rec(n - 2)

# form() 함수의 시간복잡도는 O(1), 단 70번째 이상의 결과는 정확하지 않다.
def find_fibonacchi_seq_form(n):
    sq5 = math.sqrt(5)
    phi = (1 + sq5) / 2
    return int(math.floor(phi ** n / sq5))

def test_find_fib():
    n = 10
    assert(find_fibonacchi_seq_rec(n) == 55)
    assert(find_fibonacchi_seq_iter(n) == 55)
    assert(find_fibonacchi_seq_form(n) == 55)
    print("테스트 통과!")

if __name__ == "__main__":
    test_find_fib()