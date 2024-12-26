def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    for i in range(a[1] - 1):
        b[i] = b[i] - a[0]
        b[i + 1] = b[i + 1] + max(0, b[i])

    print(max(0, b[a[1] - 1] - a[0])) 

if __name__ == '__main__':
    main()