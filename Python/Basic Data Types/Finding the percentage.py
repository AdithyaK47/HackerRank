if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    target = [v for k,v in student_marks.items() if k == query_name][0]
    avg = sum(target)/len(target)

    print(f'{avg:.2f}')

