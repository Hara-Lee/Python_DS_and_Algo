import math

# 반복문을 사용해서 찾는 방법_시간복잡도 O(n)
def find_fibonacci_seq_iter(n):
    if n < 2 : return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# 재귀문을 사용해서 찾는 방법_시간복잡도 O(n^2)
def find_fibonacci_seq_rec(n):
    if n < 2 : return n
    return find_fibonacci_seq_rec(n - 1) + find_fibonacci_seq_rec(n - 2)

# 수식을 사용해서 찾는 방법(단, 70번째 이상은 정확치 않음)_시간복잡도 O(1)
def find_fibonacci_seq_form(n):
    sq5 = math.sqrt(5)
    phi = (1 + sq5) / 2
    return int(math.floor(phi ** n / sq5))

def test_find_fib():
    n = 10
    assert(find_fibonacci_seq_rec(n) == 55)
    assert(find_fibonacci_seq_iter(n) == 55)
    assert(find_fibonacci_seq_form(n) == 55)
    print("테스트 통과!")

if __name__ == "__main__":
    test_find_fib()