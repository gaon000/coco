
def solution(n, data):
  data = data.split(' ')
  if len(data) % (n*10) != 0:
    return 0

  hobbies = [[] for _ in range(n)]
  answer = {}
  for i in range(len(data)):
    hobbies[i//10].append(data[i])
  for i in range(n):
    for j in range(i+1, n):
      answer[f'{i+1}-{j+1}'] = 20 - len(set(hobbies[i]+hobbies[j]))

  return [key for key, value in answer.items() if max(answer.values()) == value]


n = int(input())
data = input()

print(solution(n,data))