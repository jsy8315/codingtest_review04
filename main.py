# 그리디 숫자 카드 게임

# 답안 예시01
n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  result = max(result, min_value)

print(result)

# 답안 예시02
n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = 10001
  for a in data:
    min_value = min(min_value, a)
  result = max(result, min_value)
print(result)
