n1 = int(input())
set1 = set(input().split())
n2 = int(input())
set2 = set(input().split())

differ = sorted(set1.symmetric_difference(set2))

for i in differ:
  print(i)
