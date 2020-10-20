# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = input()
array_in = input().split()
like = set(input().split())
dislike = set(input().split())

happiness = 0

for i in array_in:
  if i in like:
    happiness += 1
  elif i in dislike:
    happiness -= 1
  else:
    pass

print(happiness)