def palindrome(n):
    rev = 0
    while n != 0:
        x = n % 10
        rev  = rev * 10 + x
        n = n // 10
    return rev 


print(palindrome(8827283))

# 121 2332