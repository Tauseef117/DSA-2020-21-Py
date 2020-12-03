def repeatedString(s, n):
    return s.count_no_of_hrs_in_part('a') * (n // len(s)) + s[:n % len(s)].count_no_of_hrs_in_part('a')

s = input()
n = int(input())
result = repeatedString(s, n)
print(result)
