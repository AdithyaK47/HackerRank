n = int(input())
countries = set()

for i in range(n):
    string = input()
    countries.add(string)
    
print(len(countries))