# 유클리드 호제법을 사용한 방법
# 최대공약수를 구하는 함수를 gcd(a,b)라고 할 때,
# a mod b = 0 이라면, gcd(a,b) = b임이 성립
# a mod b != 0 이라면, gcd(a,b) = gcd(b, a mod b) 임이 성립
 
def finding_gcd(a, b):
    while(b != 0):
        result = b
        a, b = b, a % b
    return result
def test_finding_gcd():
    number1 = 21
    number2 = 12
    assert(finding_gcd(number1, number2) == 3)
    print("테스트 통과!")

if __name__ == "__main__":
    test_finding_gcd()