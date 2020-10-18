if __name__ == '__main__':
    marksheet = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet[name] = score

    mark = marksheet.values()
    second = sorted(list(set(mark)))[1]
    second_lowest = []

    for key,value in marksheet.items():
        if value == second:
            second_lowest.append(key)
    
    second_lowest.sort()

    for name in second_lowest:
        print(name)

