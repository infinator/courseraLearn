def get_fibonacci_last_digit_naive(n):
    l = []
    l.append(0)
    l.append(1)
    for i in range(2, n + 1) :
        l.append((l[i - 1] + l[i - 2]) % 10)
    return l[n]

n = int(input())
print(get_fibonacci_last_digit_naive(n))