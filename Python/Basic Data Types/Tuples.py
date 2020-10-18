if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    
    numbers = [i for i in integer_list]
    print(hash(tuple(numbers)))