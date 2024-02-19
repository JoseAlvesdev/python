t = int(input())

while t > 0:
  
  t -= 1

  n, k = input().split()
  n, k = int(n), int(k)
  total = n % k + n // k

  print(total)