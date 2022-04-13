def isPalindrome(x: int) -> bool:
    if x < 0 or x % 10 == 0 and x != 0:
        return False
    sum1 = 0
    a = x
    while x > 0:
        sum1 = sum1 * 10 + x % 10
        x //= 10
    if sum1 == a:
        return True
    return False
