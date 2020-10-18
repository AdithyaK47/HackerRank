if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    maximum = max(arr)
    diff_list = []

    for i in range(0,n):
        temp = maximum - arr[i]
        if temp != 0:
            diff_list.append(temp)
    
    s_max = maximum - min(diff_list) 
    
    print(s_max)
