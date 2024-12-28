def main():
    n = int(input())
    lst = list(map(int, input().split()))
    mx, p = 0, 0

    for i in range(0, n - 2):
        current_sum = lst[i] + lst[i + 1] + lst[i + 2]
        if current_sum > mx:
            mx = current_sum
            p = i + 2

    print(mx, p)
    
if __name__ == '__main__':
    main()
