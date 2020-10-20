n1 = int(input())
set1 = set(input().split())
n2 = int(input())
set2 = set(input().split())

d1 = set2.difference(set1)
d2 = set1.difference(set2)
differ = d1.union(d2)

print ('\n'.join(sorted(differ, key=int)))