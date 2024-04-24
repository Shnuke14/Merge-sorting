## Функция слияния двух отсортированныых списков
def merge_list(a, b):
  c = []

  N = len(a)
  M = len(b)

  i = 0
  j = 0
  while i < N and j < M:
    if a[i] <= b[j]:
      c.append(a[i])
      i += 1
    else:
      c.append(b[j])
      j += 1

  c += a[i:] + b[j:]
  return c

## Функция деления списка и слияния списков в общий отсортированный список
def split_and_merge_list(a):
  N1 = len(a) // 2
  a1 = a[:N1]
  a2 = a[N1:]

  ## Если длины новых списков больше 1, продолжаем деление
  if len(a1) > 0:
    a1 = split_and_merge_list(a1)
  if len(a2) > 0:
    a1 = split_and_merge_list(a1)

  ## Слияние двух отсортированных списков в один
  return merge_list(a1, a2)

a = [9, 5, -3, 4, 7, 8, -8]
a = split_and_merge_list(a)

print(a)